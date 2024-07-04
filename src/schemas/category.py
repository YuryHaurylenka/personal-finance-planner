from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryUpdatePartial(CategoryCreate):
    name: str | None = None


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    category_id: int
