from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from sqlalchemy import JSON, Column

from models import *

class Recipe(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    title: str
    description: Optional [str] =None
    image_url: str
    category: str

    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Store ordered steps as JSON (list of strings)
    steps: Optional[list[str]] = Field(default_factory=list, sa_column=Column(JSON))

    #owner
    user_id: int = Field(foreign_key="user.id")
    author: "User" = Relationship(back_populates="recipes")

    # back refs
    ingredients: List["Ingredient"] = Relationship(back_populates="recipe")
    reviews: List["Review"] = Relationship(back_populates="recipe")
    favorites: List["Favorite"] = Relationship(back_populates="recipe")
    tags: List["RecipeTag"] = Relationship(back_populates="recipe")