"""Schemas for geometry objects in 2D space."""
import math
from typing import List
from pydantic import Field, conlist, constr, conint

from .base import NoExtraBaseModel, Color


class Vector2D(NoExtraBaseModel):
    """A vector object in 2D space."""

    type: constr(regex='^Vector2D$') = 'Vector2D'

    x: float = Field(
        ...,
        description='Number for X coordinate.'
    )

    y: float = Field(
        ...,
        description='Number for Y coordinate.'
    )


class Point2D(NoExtraBaseModel):
    """A point object in 2D space."""

    type: constr(regex='^Point2D$') = 'Point2D'

    x: float = Field(
        ...,
        description='Number for X coordinate.'
    )

    y: float = Field(
        ...,
        description='Number for Y coordinate.'
    )


class Ray2D(NoExtraBaseModel):
    """A ray object in 2D space."""

    type: constr(regex='^Ray2D$') = 'Ray2D'

    p: List[float] = Field(
        ...,
        description="Ray base point as 2 (x, y) values.",
        min_items=2,
        max_items=2
    )

    v: List[float] = Field(
        ...,
        description="Ray direction vector as 2 (x, y) values.",
        min_items=2,
        max_items=2
    )


class LineSegment2D(NoExtraBaseModel):
    """A single line segment face in 2D space."""

    type: constr(regex='^LineSegment2D$') = 'LineSegment2D'

    p: List[float] = Field(
        ...,
        description="Line segment base point as 2 (x, y) values.",
        min_items=2,
        max_items=2
    )

    v: List[float] = Field(
        ...,
        description="Line segment direction vector as 2 (x, y) values.",
        min_items=2,
        max_items=2
    )


class Polyline2D(NoExtraBaseModel):
    """A polyline in 2D space."""

    type: constr(regex='^Polyline2D$') = 'Polyline2D'

    vertices: List[conlist(float, min_items=2, max_items=2)] = Field(
        ...,
        min_items=3,
        description='A list of points representing the the vertices of the polyline. '
        'The list should include at least 3 points and each point '
        'should be a list of 2 (x, y) values.'
    )

    interpolated: bool = Field(
        False,
        description='A boolean to note whether the polyline should be interpolated '
        'between the input vertices when it is translated to other interfaces.'
    )


class Arc2D(NoExtraBaseModel):
    """A single arc or circle in 2D space."""

    type: constr(regex='^Arc2D$') = 'Arc2D'

    c: List[float] = Field(
        ...,
        description="Center of the arc as 2 (x, y) values.",
        min_items=2,
        max_items=2
    )

    r: float = Field(
        ...,
        description='A number representing the radius of the arc.'
    )

    a1: float = Field(
        default=0,
        ge=0,
        le=math.pi * 2,
        description='A number between 0 and 2 * pi for the start angle of the arc.'
    )

    a2: float = Field(
        default=math.pi * 2,
        ge=0,
        le=math.pi * 2,
        description='A number between 0 and 2 * pi for the end angle of the arc.'
    )


class Polygon2D(NoExtraBaseModel):
    """A polygon in 2D space (without holes)."""

    type: constr(regex='^Polygon2D$') = 'Polygon2D'

    vertices: List[conlist(float, min_items=2, max_items=2)] = Field(
        ...,
        min_items=3,
        description='A list of points representing the vertices of the polygon. '
        'The list should include at least 3 points and each point should be a '
        'list of 2 (x, y) values.'
    )


class Mesh2D(NoExtraBaseModel):
    """A mesh in 2D space."""

    type: constr(regex='^Mesh2D$') = 'Mesh2D'

    vertices: List[conlist(float, min_items=2, max_items=2)] = Field(
        ...,
        min_items=3,
        description='A list of points representing the vertices of the mesh. '
        'The list should include at least 3 points and each point '
        'should be a list of 2 (x, y) values.'
    )

    faces: List[conlist(conint(ge=0), min_items=3, max_items=4)] = Field(
        ...,
        min_items=1,
        description='A list of lists with each sub-list having either 3 or 4 '
        'integers. These integers correspond to indices within the list of vertices.'
    )

    colors: List[Color] = Field(
        None,
        description='An optional list of colors that correspond to either the faces '
        'of the mesh or the vertices of the mesh.'
    )
