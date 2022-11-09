import datetime

from pydantic import BaseModel, Field, validator

from app.core.config import get_app_settings


class DateTimeModelMixin(BaseModel):
    created_at: datetime.datetime = None  # type: ignore
    updated_at: datetime.datetime = None  # type: ignore

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(
        cls,  # noqa: N805
        value: datetime.datetime,  # noqa: WPS110
    ) -> datetime.datetime:
        return value or datetime.datetime.now()


class IDModelMixin(BaseModel):
    id_: int = Field(0, alias="id")


class ImageModelMixin(BaseModel):
    image: str

    _placeholder_setting = "placeholder_image"

    @validator("image", pre=True)
    def default_image(cls, value: str) -> str:  # noqa: N805
        app_settings = get_app_settings()
        return value or getattr(app_settings, cls._placeholder_setting)
