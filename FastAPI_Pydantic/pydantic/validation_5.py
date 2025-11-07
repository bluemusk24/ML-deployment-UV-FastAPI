print('Using Pydantic Built-in Constraints: eg EmailStr, SecretStr \n')

from datetime import datetime, UTC
from pydantic import BaseModel, ValidationError, Field, EmailStr, HttpUrl, SecretStr
from functools import partial
from typing import Annotated, Literal
from uuid import UUID, uuid4

# User Pydantic class
class User(BaseModel):
    uid: UUID = Field(alias="id", default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr
    password: SecretStr                     # this hides the secret password when printed out
    website: HttpUrl | None = None
    age: Annotated[int, Field(ge=13, le=130)]
    bio: str = ""                       # Default values for bio  ---> optional fields in the user object below
    is_active: bool = True              # Default value for is_active.    ---> optional fields in the user object below
    full_name: str | None = None
    verified_at: datetime | None = None

# BlogPost Pydantic Class
class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    author_id: str | int
    view_count: int = 0
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)     # or []
    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    status: Literal["draft", "published", "archived"] = 'draft'
    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]


### Valid User
user = User(
    username="Emmanuel",
    email="emmanueleigbedion@gmail.com",
    age=39,
    password="secret123",
)
print(user.model_dump_json(indent=2))

print('_'*50)

print('Get Password Secret:', user.password.get_secret_value())