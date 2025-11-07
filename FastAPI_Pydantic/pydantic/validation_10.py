print('Nested Models with JSON Data: \n')
from pydantic import BaseModel, ValidationError, ValidationInfo, Field, EmailStr, HttpUrl, SecretStr, computed_field, field_validator, model_validator
from functools import partial
from typing import Annotated, Literal
from datetime import datetime, UTC
from uuid import UUID, uuid4
import json


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
    first_name: str = ""
    last_name: str = ""
    follower_count: int = 0
    verified_at: datetime | None = None

    # Validating Username
    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()
    
    # Validating Website
    @field_validator("website", mode="before")     # add mode before validating website field, else you will get an error
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v

    # Computed Field
    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower_count >= 10000

### Comment Model
class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0

class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    author: User             # Pydantic User model here from above
    view_count: int = 0
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)     # or []
    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    status: Literal["draft", "published", "archived"] = 'draft'
    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]
    comments: list[Comment] = Field(default_factory=list)


### BlogPost Dictionary
post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": {
        "username": "emmanuel",
        "email": "emmanueleigbedion@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

post = BlogPost.model_validate_json(json.dumps(post_data))    # use this json.dump if data is in json format from an API, and not a dictionary.

print(post.model_dump_json(indent=2))