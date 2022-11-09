from typing import List, Optional
from pydantic import validator

from app.core.config import get_app_settings
from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.rwmodel import RWModel


class Item(IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    tags: List[str]
    seller: Profile
    favorited: bool
    favorites_count: int
    image: str
    body: Optional[str]

    @validator("image", pre=True)
    def default_image(cls, value: str) -> str:  # noqa: N805
        app_settings = get_app_settings()
        return value or app_settings.placeholder_image
