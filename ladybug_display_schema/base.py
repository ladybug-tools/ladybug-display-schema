"""Base class for all objects requiring a valid names for all engines."""
from enum import Enum
from typing import Union, Literal, Annotated
from pydantic import BaseModel, Field, ConfigDict


class NoExtraBaseModel(BaseModel):
    """Base class for all objects that are not extensible with additional keys."""

    model_config = ConfigDict(extra='forbid')


class Color(NoExtraBaseModel):
    """A RGB color."""

    type: Literal['Color'] = 'Color'

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


class Default(NoExtraBaseModel):
    """Object to signify when the default value of a visual interface should be used."""

    type: Literal['Default'] = 'Default'


class LineTypes(str, Enum):
    continuous = 'Continuous'
    dashed = 'Dashed'
    dots = 'Dotted'
    dash_dot = 'DashDot'


class DisplayModes(str, Enum):
    surface = 'Surface'
    surface_with_edges = 'SurfaceWithEdges'
    wireframe = 'Wireframe'
    points = 'Points'


class HorizontalAlignments(str, Enum):
    left = 'Left'
    center = 'Center'
    right = 'Right'


class VerticalAlignments(str, Enum):
    top = 'Top'
    middle = 'Middle'
    bottom = 'Bottom'


class DisplayBaseModel(NoExtraBaseModel):
    """Base class for all Geometric Display objects."""

    user_data: Union[dict, None] = Field(
        default=None,
        description='Optional dictionary of user data associated with the object.'
        'All keys and values of this dictionary should be of a standard data '
        'type to ensure correct serialization of the object (eg. str, float, '
        'int, list).'
    )


class SingleColorBase(DisplayBaseModel):
    """Base class for all Geometric Display objects with a single color."""

    color: Color = Field(
        ...,
        description='Color for the geometry.'
    )


class LineCurveBase(SingleColorBase):
    """Base class for all Geometric Display objects with a line like properties."""

    line_width: Union[Default, Annotated[float, Field(ge=0)]] = Field(
        Default(),
        description='Number for line width in pixels (for the screen) or '
        'millimeters (in print). Set to zero to hide the geometry.'
    )

    line_type: LineTypes = Field(
        LineTypes.continuous,
        description='Text to indicate the type of line to display (dashed, dotted, '
        'etc.). The LineTypes enumeration contains all acceptable types.'
    )
