"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogpost" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List


class Contactsubmission(BaseModel):
    """
    Contact form submissions
    Collection name: "contactsubmission"
    """
    name: str = Field(..., description="Sender full name", min_length=2)
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., description="Message body", min_length=5, max_length=5000)
    source: Optional[str] = Field(None, description="Source page or referrer")


class Blogpost(BaseModel):
    """
    Blog posts schema
    Collection name: "blogpost"
    """
    title: str
    slug: str
    excerpt: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None
    published: bool = True
