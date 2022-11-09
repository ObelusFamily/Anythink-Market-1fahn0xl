from app.models.common import DateTimeModelMixin, IDModelMixin, ImageModelMixin
from app.models.domain.rwmodel import RWModel
from app.services import security


class User(ImageModelMixin, RWModel):
    username: str
    email: str
    bio: str = ""

    _placeholder_setting = "placeholder_avatar"


class UserInDB(IDModelMixin, DateTimeModelMixin, User):
    salt: str = ""
    hashed_password: str = ""

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.hashed_password)

    def change_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_password = security.get_password_hash(self.salt + password)
