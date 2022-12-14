from typing import List, Optional
from app.models.common import DateTimeModelMixin, IDModelMixin, ImageModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.rwmodel import RWModel


class Item(ImageModelMixin, IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    tags: List[str]
    seller: Profile
    favorited: bool
    favorites_count: int
    body: Optional[str]