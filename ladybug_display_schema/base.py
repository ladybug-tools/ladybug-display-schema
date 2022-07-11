"""Base class for all objects requiring a valid names for all engines."""
from pydantic import BaseModel, Field, Extra, constr


class DisplayBaseModel(BaseModel):
    """Base class for all Geometric Display objects."""

    class Config:
        extra = Extra.forbid

    user_data: dict = Field(
        default=None,
        description='Optional dictionary of user data associated with the object.'
        'All keys and values of this dictionary should be of a standard data '
        'type to ensure correct serialization of the object (eg. str, float, '
        'int, list).'
    )


class Color(BaseModel):

    class Config:
        extra = Extra.forbid

    type: constr(regex='^Color$') = 'Color'

    r: int = Field(
        ...,
        ge=0,
        le=255,
        description='Value for red channel.'
    )

    g: int = Field(
        ...,
        ge=0,
        le=255,
        description='Value for green channel.'
    )

    b: int = Field(
        ...,
        ge=0,
        le=255,
        description='Value for blue channel.'
    )

    a: int = Field(
        default=255,
        ge=0,
        le=255,
        description='Value for the alpha channel, which defines the opacity as a '
        'number between 0 (fully transparent) and 255 (fully opaque).'
    )
