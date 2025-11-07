from datetime import datetime
from pydantic import BaseModel, ValidationError

# User pydantic class
class User(BaseModel):
    uid: int
    username: str
    email: str

    bio: str = ""                       # Default values for bio  ---> optional fields in the user object below
    is_active: bool = True              # Default value for is_active.    ---> optional fields in the user object below

    full_name: str | None = None
    verified_at: datetime | None = None

print('Topic: Adding try-except block to the User Class for Errors, \n')

try:
    
    user = User(
        uid='test',
        username=None,
        email=123,
    )
    print('All fields:', user.model_dump_json(indent=2), '\n')
except ValidationError as e:
    print(e)