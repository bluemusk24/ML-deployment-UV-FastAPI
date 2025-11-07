from datetime import datetime, UTC
from pydantic import BaseModel, ValidationError, Field
from functools import partial
from typing import Annotated, Literal

# User pydantic class
class User(BaseModel):
    uid: Annotated[int, Field(gt=0)]
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: str
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


### Invalid User
try:
    user = User(
        uid=0,
        username="cs",
        email="CoreyMSchafer@gmail.com",
        age=12,
    )
    print(user)
except ValidationError as e:
    print(e)