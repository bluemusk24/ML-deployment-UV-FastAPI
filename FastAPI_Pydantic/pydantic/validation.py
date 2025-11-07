from datetime import datetime
from pydantic import BaseModel, ValidationError

# Create a pydantic class
class User(BaseModel):
    uid: int
    username: str
    email: str

    bio: str = ""                       # Default values for bio  ---> optional fields in the user object below
    is_active: bool = True              # Default value for is_active.    ---> optional fields in the user object below

    full_name: str | None = None
    verified_at: datetime | None = None


user = User(
    uid=1234,
    username='emmanuel',
    email='emmanueleigbedion@gmail.com',
)

print('All fields:', user, '\n')

# get a field from the Pydatic Basemodel
print('Username field:',user.username, '\n')

# Change user_bio from empty string
user.bio = 'Pydantic Validation Schema'
print('Bio field:', user.bio, '\n')

# Dictionary for Pydantic
print('Dictionary Format:', user.model_dump(), '\n')

# json format Pydantic
print('Json_format:', user.model_dump_json(indent=2), '\n')