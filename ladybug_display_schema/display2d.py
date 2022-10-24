"""Schemas for geometric display objects in 2D space."""
from typing import List, Union
from pydantic import Field, constr, root_validator

from .base import DisplayBaseModel, SingleColorBase, LineCurveBase, \
    Color, DisplayModes, Default
from .geometry2d import Vector2D, Point2D, Ray2D, LineSegment2D, \
    Polyline2D, Arc2D, Polygon2D, Mesh2D


class DisplayVector2D(SingleColorBase):
    """A point object in 2D space with display properties."""

    type: constr(regex='^DisplayVector2D$') = 'DisplayVector2D'

    geometry: Vector2D = Field(
        ...,
        description='Vector2D for the geometry.'
    )


class DisplayPoint2D(SingleColorBase):
    """A point object in 2D space with display properties."""

    type: constr(regex='^DisplayPoint2D$') = 'DisplayPoint2D'

    geometry: Point2D = Field(
        ...,
        description='Point2D for the geometry.'
    )

    radius: Union[Default, float] = Field(
        Default(),
        ge=0,
        description='Number for the radius with which the point should be displayed '
        'in pixels (for the screen) or millimeters (in print).'
    )


class DisplayRay2D(SingleColorBase):
    """A ray object in 2D space with display properties."""

    type: constr(regex='^DisplayRay2D$') = 'DisplayRay2D'

    geometry: Ray2D = Field(
        ...,
        description='Ray2D for the geometry.'
    )


class DisplayLineSegment2D(LineCurveBase):
    """A single line segment face in 2D space with display properties."""

    type: constr(regex='^DisplayLineSegment2D$') = 'DisplayLineSegment2D'

    geometry: LineSegment2D = Field(
        ...,
        description='LineSegment2D for the geometry.'
    )


class DisplayPolyline2D(LineCurveBase):
    """A polyline in 2D space with display properties."""

    type: constr(regex='^DisplayPolyline2D$') = 'DisplayPolyline2D'

    geometry: Polyline2D = Field(
        ...,
        description='Polyline2D for the geometry.'
    )


class DisplayArc2D(LineCurveBase):
    """A single arc or circle in 2D space with display properties."""

    type: constr(regex='^DisplayArc2D$') = 'DisplayArc2D'

    geometry: Arc2D = Field(
        ...,
        description='Arc2D for the geometry.'
    )


class DisplayPolygon2D(LineCurveBase):
    """A single polygon in 2D space with display properties."""

    type: constr(regex='^DisplayPolygon2D$') = 'DisplayPolygon2D'

    geometry: Polygon2D = Field(
        ...,
        description='Polygon2D for the geometry.'
    )


class DisplayMesh2D(DisplayBaseModel):
    """A mesh in 2D space with display properties."""

    type: constr(regex='^DisplayMesh2D$') = 'DisplayMesh2D'

    geometry: Mesh2D = Field(
        ...,
        description='Mesh2D for the geometry.'
    )

    colors: List[Color] = Field(
        ...,
        description='A list of colors that correspond to either the faces '
        'of the mesh or the vertices of the mesh. It can also be a single color '
        'for the entire mesh.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.surface,
        description='Text to indicate the display mode (surface, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )

    @root_validator
    def check_colors_align(cls, values):
        """Check that there are an acceptable number of colors for the mesh."""
        colors, geo = values.get('colors'), values.get('geometry')
        if colors is None:
            return values
        if len(colors) in (1, len(geo.faces), len(geo.vertices)):
            return values
        else:
            raise ValueError(
                'Number of colors ({}) does not match the number of mesh faces '
                '({}) nor the number of vertices ({}).'.format(
                    len(colors), len(geo.faces), len(geo.vertices))
            )
