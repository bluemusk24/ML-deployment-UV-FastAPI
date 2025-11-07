print('Using Pydantic Custom Validator: Model_Validator \n')
from pydantic import BaseModel, ValidationError, ValidationInfo, Field, EmailStr, HttpUrl, SecretStr, computed_field, field_validator, model_validator
from functools import partial
from typing import Annotated, Literal


### Model Validator: 
class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str
    
    @model_validator(mode='after')       # if two classes (passwords) match
    def passwords_match(self) -> 'UserRegistration':
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self

try:
    registration = UserRegistration(
        email="CoreyMSchafer@gmail.com",
        password="secret123",
        confirm_password="secret456"
    )
except ValidationError as e:
    print(e)