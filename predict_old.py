import pickle

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

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

def main():
    result = pipeline.predict_proba(datapoint)[0, 1]
    print(f'Probability of churn: {result:.3f}')

    if result >= 0.5:
        print('send email with promo')
    else:
        print('do not do anything')
if __name__ == "__main__":
    main()