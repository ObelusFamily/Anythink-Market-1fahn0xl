from app.models.common import ImageModelMixin
from app.models.domain.rwmodel import RWModel


class Profile(ImageModelMixin, RWModel):
    username: str
    bio: str = ""
    following: bool = False

    _placeholder_setting = "placeholder_avatar"

