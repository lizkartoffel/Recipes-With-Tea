from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

from models import *


class Ingredient(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    quantity: Optional[str] = None   # e.g. "2 cups", "1 tsp"
    ord: Optional[int] = None        # ordering within recipe (optional)

    recipe_id: int = Field(foreign_key="recipe.id")
    recipe: "Recipe" = Relationship(back_populates="ingredients")