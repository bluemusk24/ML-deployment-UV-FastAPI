#!/usr/bin/env python
# coding: utf-8

# This is a starter notebook for an updated module 5 of ML Zoomcamp
# 
# The code is based on the modules 3 and 4. We use the same dataset: [telco customer churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

# In[11]:


import pandas as pd
import numpy as np
import sklearn


# In[12]:


print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')


# In[13]:


from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression


# In[14]:


data_url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv'

df = pd.read_csv(data_url)

df.columns = df.columns.str.lower().str.replace(' ', '_')

# df

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)

df.churn = (df.churn == 'yes').astype(int)


# In[15]:


y_train = df.churn


# In[16]:


numerical = ['tenure', 'monthlycharges', 'totalcharges']

categorical = [
    'gender',
    'seniorcitizen',
    'partner',
    'dependents',
    'phoneservice',
    'multiplelines',
    'internetservice',
    'onlinesecurity',
    'onlinebackup',
    'deviceprotection',
    'techsupport',
    'streamingtv',
    'streamingmovies',
    'contract',
    'paperlessbilling',
    'paymentmethod',
]


# In[17]:


dv = DictVectorizer()

train_dict = df[categorical + numerical].to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)


# In[18]:


datapoint = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}


# In[12]:


X = dv.transform(datapoint)


# In[13]:


model.predict_proba(X)[0, 1]


# * the probability of datapoint churn is 66%

# In[1]:


import pickle


# In[15]:


with open('model.bin', 'wb') as f_out:
    pickle.dump((dv, model), f_out)


# In[16]:


get_ipython().system('ls -lh')


# In[2]:


with open('model.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)


# In[3]:


dv


# * Note: After pickle.dump and pickle.load, restart kernel to confirm if dv was saved with the model. Run import pickle, pickle.load, then dv again

# In[9]:


# Test Dictvectorizer and model

customer = {
    'gender': 'male',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 129.85
}

X = dv.transform(customer)
churn = model.predict_proba(X)[0,1]

if churn >= 0.5:
    print(f'the probability of churn is: {churn:.2f}')
    print('send email with promo')
else:
    print('do not do anything')


# ### Using Pipeline to combine bith DictVectorizer and Model

# In[10]:


from sklearn.pipeline import make_pipeline


# In[19]:


pipeline = make_pipeline(
    DictVectorizer(),
    LogisticRegression(solver='liblinear')
)


# In[20]:


pipeline.fit(train_dict, y_train)


# * Saving the and loading pipeline with pickle

# In[22]:


with open('model.bin', 'wb') as f_out:
    pickle.dump(pipeline, f_out)


# In[24]:


with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


# In[26]:


churn = pipeline.predict_proba(customer)[0, 1]

if churn >= 0.5:
    print(f'the probability of churn is: {churn:.2f}')
    print('send email with promo')
else:
    print('do not do anything')


# In[27]:


pipeline


# In[33]:


import requests


# In[36]:


url = 'http://localhost:9696/predict'

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

response = requests.post(url, json=customer)


# In[38]:


predictions = response.json()


# In[39]:


if predictions['churn']:
    print('accept loan application')
else:
    print('reject loan application')


# In[46]:


for n in numerical:
    print(df[n].describe())
    print()

for c in categorical:
    print(df[c].value_counts())
    print()


# In[ ]:




