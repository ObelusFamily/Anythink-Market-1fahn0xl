from typing import Optional
from pydantic import validator

from app.core.config import get_app_settings
from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel
from app.services import security


class User(RWModel):
    username: str
    email: str
    bio: str = ""
    image: str = ""

    @validator("image", pre=True)
    def default_image(cls, value: str) -> str:  # noqa: N805
        app_settings = get_app_settings()
        return value or app_settings.placeholder_avatar


class UserInDB(IDModelMixin, DateTimeModelMixin, User):
    salt: str = ""
    hashed_password: str = ""

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.hashed_password)

    def change_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_password = security.get_password_hash(self.salt + password)
