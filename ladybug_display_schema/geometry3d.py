"""Schemas for geometry objects in 3D space."""
import math
from typing import List
from pydantic import Field, conlist, constr, conint

from .base import NoExtraBaseModel, Color


class Vector3D(NoExtraBaseModel):
    """A vector object in 3D space."""

    type: constr(regex='^Vector3D$') = 'Vector3D'

    x: float = Field(
        ...,
        description='Number for X coordinate.'
    )

    y: float = Field(
        ...,
        description='Number for Y coordinate.'
    )

    z: float = Field(
        ...,
        description='Number for Z coordinate.'
    )


class Point3D(NoExtraBaseModel):
    """A point object in 3D space."""

    type: constr(regex='^Point3D$') = 'Point3D'

    x: float = Field(
        ...,
        description='Number for X coordinate.'
    )

    y: float = Field(
        ...,
        description='Number for Y coordinate.'
    )

    z: float = Field(
        ...,
        description='Number for Z coordinate.'
    )


class Ray3D(NoExtraBaseModel):
    """A ray object in 3D space."""

    type: constr(regex='^Ray3D$') = 'Ray3D'

    p: List[float] = Field(
        ...,
        description="Ray base point as 3 (x, y, z) values.",
        min_items=3,
        max_items=3
    )

    v: List[float] = Field(
        ...,
        description="Ray direction vector as 3 (x, y, z) values.",
        min_items=3,
        max_items=3
    )


class Plane(NoExtraBaseModel):
    """A plane object."""

    type: constr(regex='^Plane$') = 'Plane'

    n: List[float] = Field(
        ...,
        description="Plane normal as 3 (x, y, z) values.",
        min_items=3,
        max_items=3
    )

    o: List[float] = Field(
        ...,
        description="Plane origin as 3 (x, y, z) values",
        min_items=3,
        max_items=3
    )

    x: List[float] = Field(
        default=None,
        description="Plane x-axis as 3 (x, y, z) values. If None, it is autocalculated.",
        min_items=3,
        max_items=3
    )


class LineSegment3D(NoExtraBaseModel):
    """A single line segment face in 3D space."""

    type: constr(regex='^LineSegment3D$') = 'LineSegment3D'

    p: List[float] = Field(
        ...,
        description="Line segment base point as 3 (x, y, z) values.",
        min_items=3,
        max_items=3
    )

    v: List[float] = Field(
        ...,
        description="Line segment direction vector as 3 (x, y, z) values.",
        min_items=3,
        max_items=3
    )


class Polyline3D(NoExtraBaseModel):
    """A polyline in 3D space."""

    type: constr(regex='^Polyline3D$') = 'Polyline3D'

    vertices: List[conlist(float, min_items=3, max_items=3)] = Field(
        ...,
        min_items=3,
        description='A list of points representing the the vertices of the polyline. '
        'The list should include at least 3 points and each point '
        'should be a list of 3 (x, y, z) values.'
    )

    interpolated: bool = Field(
        False,
        description='A boolean to note whether the polyline should be interpolated '
        'between the input vertices when it is translated to other interfaces.'
    )


class Arc3D(NoExtraBaseModel):
    """A single arc or circle in 3D space."""

    type: constr(regex='^Arc3D$') = 'Arc3D'

    plane: Plane = Field(
        ...,
        description='A Plane in which the arc lies with an origin representing the '
        'center of the circle for the arc.'
    )

    radius: float = Field(
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


class Face3D(NoExtraBaseModel):
    """A single planar face in 3D space."""

    type: constr(regex='^Face3D$') = 'Face3D'

    boundary: List[conlist(float, min_items=3, max_items=3)] = Field(
        ...,
        min_items=3,
        description='A list of points representing the outer boundary vertices of '
        'the face. The list should include at least 3 points and each point '
        'should be a list of 3 (x, y, z) values.'
    )

    holes: List[conlist(conlist(float, min_items=3, max_items=3), min_items=3)] = Field(
        default=None,
        description='Optional list of lists with one list for each hole in the face.'
        'Each hole should be a list of at least 3 points and each point a list '
        'of 3 (x, y, z) values. If None, it will be assumed that there are no '
        'holes in the face.'
    )

    plane: Plane = Field(
        default=None,
        description='Optional Plane indicating the plane in which the face exists.'
        'If None, the plane will usually be derived from the boundary points.'
    )


class Mesh3D(NoExtraBaseModel):
    """A mesh in 3D space."""

    type: constr(regex='^Mesh3D$') = 'Mesh3D'

    vertices: List[conlist(float, min_items=3, max_items=3)] = Field(
        ...,
        min_items=3,
        description='A list of points representing the vertices of the mesh. '
        'The list should include at least 3 points and each point '
        'should be a list of 3 (x, y, z) values.'
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


class PolyfaceEdgeInfo(NoExtraBaseModel):
    """Optional edge information for Polyface."""

    edge_indices: List[conlist(conint(ge=0), min_items=2, max_items=2)] = Field(
        ...,
        min_items=3,
        description='An array objects that each contain two integers. These integers '
        'correspond to indices within the vertices list and each tuple represents '
        'a line segment for an edge of the polyface.'
    )

    edge_types: List[conint(ge=0)] = Field(
        ...,
        min_items=3,
        description='An array of integers for each edge that parallels the edge_indices '
        'list. An integer of 0 denotes a naked edge, an integer of 1 denotes an '
        'internal edge. Anything higher is a non-manifold edge.'
    )


class Polyface3D(NoExtraBaseModel):
    """A Polyface in 3D space."""

    type: constr(regex='^Polyface3D$') = 'Polyface3D'

    vertices: List[conlist(float, min_items=3, max_items=3)] = Field(
        ...,
        min_items=3,
        description='A list of points representing the vertices of the polyface. '
        'The list should include at least 3 points and each point '
        'should be a list of 3 (x, y, z) values.'
    )

    face_indices: List[
        conlist(conlist(conint(ge=0), min_items=3), min_items=1)
    ] = Field(
        ...,
        min_items=1,
        description='A list of lists with one list for each face of the polyface. '
        'Each face list must contain at least one sub-list of integers corresponding '
        'to indices within the vertices list. Additional sub-lists of integers may '
        'follow this one such that the first sub-list denotes the boundary of the '
        'face while each subsequent sub-list denotes a hole in the face.'
    )

    edge_information: PolyfaceEdgeInfo = Field(
        default=None,
        description='Optional edge information, which will speed up the '
        'creation of the Polyface object if it is available but should be left '
        'as None if it is unknown. If None, edge_information will be computed '
        'from the vertices and face_indices inputs.'
    )


class Sphere(NoExtraBaseModel):
    """A sphere object."""

    type: constr(regex='^Sphere$') = 'Sphere'

    center: List[float] = Field(
        ...,
        description='The center of the sphere as 3 (x, y, z) values.',
        min_items=3,
        max_items=3
    )

    radius: float = Field(
        ...,
        gt=0,
        description='A number representing the radius of the sphere.'
    )


class Cone(NoExtraBaseModel):
    """A cone object."""

    type: constr(regex='^Cone$') = 'Cone'

    vertex: List[float] = Field(
        ...,
        description='The point at the tip of the cone as 3 (x, y, z) values.',
        min_items=3,
        max_items=3
    )

    axis: List[float] = Field(
        ...,
        description='The vector representing the direction of the cone as 3 (x, y, z) '
        'values. The vector extends from the vertex to the center of the base.',
        min_items=3,
        max_items=3
    )

    angle: float = Field(
        ...,
        gt=0,
        lt=math.pi / 2,
        description='An angle in radians representing the half angle between '
        'the axis and the surface.'
    )


class Cylinder(NoExtraBaseModel):
    """A cylinder object."""

    type: constr(regex='^Cylinder$') = 'Cylinder'

    center: List[float] = Field(
        ...,
        description='The center of the bottom base of the cylinder as '
        '3 (x, y, z) values.',
        min_items=3,
        max_items=3
    )

    axis: List[float] = Field(
        ...,
        description='The vector representing the direction of the cylinder as '
        '3 (x, y, z) values. The vector extends from the bottom base center to '
        'the top base center.',
        min_items=3,
        max_items=3
    )

    radius: float = Field(
        ...,
        gt=0,
        description='A number representing the radius of the cylinder.'
    )
