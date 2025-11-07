from datetime import datetime, UTC
from pydantic import BaseModel, ValidationError, Field
from functools import partial
from typing import Literal

# User pydantic class
class User(BaseModel):
    uid: int
    username: str
    email: str

    bio: str = ""                       # Default values for bio  ---> optional fields in the user object below
    is_active: bool = True              # Default value for is_active.    ---> optional fields in the user object below

    full_name: str | None = None
    verified_at: datetime | None = None

# BlogPost Pydantic Class
class BlogPost(BaseModel):
    title: str
    content: str
    author_id: str | int
    view_count: int = 0
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)     # or []
    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    status: Literal["draft", "published", "archived"] = 'draft'

post = BlogPost(
    title="Getting Started with Python",
    content="Here's how to begin...",
    author_id="12345",
)

print(post.model_dump_json(indent=2))