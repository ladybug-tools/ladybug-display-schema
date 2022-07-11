"""Schemas for geometric display objects in 3D space."""
from typing import List
from pydantic import Field, constr, root_validator

from .base import DisplayBaseModel, SingleColorBase, LineCurveBase, \
    Color, DisplayModes
from .geometry3d import Vector3D, Point3D, Ray3D, Plane, LineSegment3D, \
    Polyline3D, Arc3D, Face3D, Mesh3D, Polyface3D, Sphere, Cone, Cylinder


class DisplayVector3D(SingleColorBase):
    """A point object in 3D space with display properties."""

    type: constr(regex='^DisplayVector3D$') = 'DisplayVector3D'

    geometry: Vector3D = Field(
        ...,
        description='Vector3D for the geometry.'
    )


class DisplayPoint3D(SingleColorBase):
    """A point object in 3D space with display properties."""

    type: constr(regex='^DisplayPoint3D$') = 'DisplayPoint3D'

    geometry: Point3D = Field(
        ...,
        description='Point3D for the geometry.'
    )


class DisplayRay3D(SingleColorBase):
    """A ray object in 3D space with display properties."""

    type: constr(regex='^DisplayRay3D$') = 'DisplayRay3D'

    geometry: Ray3D = Field(
        ...,
        description='Ray3D for the geometry.'
    )


class DisplayPlane(SingleColorBase):
    """A plane object with display properties."""

    type: constr(regex='^DisplayPlane$') = 'DisplayPlane'

    geometry: Plane = Field(
        ...,
        description='Plane for the geometry.'
    )

    show_axes: bool = Field(
        False,
        description='A boolean to note whether the plane should be displayed '
        'with XY axes instead of just an origin point and a normal vector.'
    )

    show_grid: bool = Field(
        False,
        description='A boolean to note whether the plane should be displayed '
        'with a grid.'
    )


class DisplayLineSegment3D(LineCurveBase):
    """A single line segment face in 3D space with display properties."""

    type: constr(regex='^DisplayLineSegment3D$') = 'DisplayLineSegment3D'

    geometry: LineSegment3D = Field(
        ...,
        description='LineSegment3D for the geometry.'
    )


class DisplayPolyline3D(LineCurveBase):
    """A polyline in 3D space with display properties."""

    type: constr(regex='^DisplayPolyline3D$') = 'DisplayPolyline3D'

    geometry: Polyline3D = Field(
        ...,
        description='Polyline3D for the geometry.'
    )


class DisplayArc3D(LineCurveBase):
    """A single arc or circle in 3D space with display properties."""

    type: constr(regex='^DisplayArc3D$') = 'DisplayArc3D'

    geometry: Arc3D = Field(
        ...,
        description='Arc3D for the geometry.'
    )


class DisplayFace3D(SingleColorBase):
    """A single planar face in 3D space with display properties."""

    type: constr(regex='^DisplayFace3D$') = 'DisplayFace3D'

    geometry: Face3D = Field(
        ...,
        description='Face3D for the geometry.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.shaded,
        description='Text to indicate the display mode (shaded, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )


class DisplayMesh3D(DisplayBaseModel):
    """A mesh in 3D space with display properties."""

    type: constr(regex='^DisplayMesh3D$') = 'DisplayMesh3D'

    geometry: Mesh3D = Field(
        ...,
        description='Mesh3D for the geometry.'
    )

    colors: List[Color] = Field(
        ...,
        description='A list of colors that correspond to either the faces '
        'of the mesh or the vertices of the mesh. It can also be a single color '
        'for the entire mesh.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.shaded,
        description='Text to indicate the display mode (shaded, wireframe, '
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


class DisplayPolyface3D(DisplayBaseModel):
    """A Polyface in 3D space with display properties."""

    type: constr(regex='^DisplayPolyface3D$') = 'DisplayPolyface3D'

    geometry: Polyface3D = Field(
        ...,
        description='Polyface3D for the geometry.'
    )

    colors: List[Color] = Field(
        ...,
        description='A list of colors that correspond to either the faces of the '
        'polyface or the vertices of the polyface. It can also be a single color '
        'for the entire polyface.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.shaded,
        description='Text to indicate the display mode (shaded, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )

    @root_validator
    def check_colors_align(cls, values):
        """Check that there are an acceptable number of colors for the mesh."""
        colors, geo = values.get('colors'), values.get('geometry')
        if colors is None:
            return values
        if len(colors) in (1, len(geo.face_indices), len(geo.vertices)):
            return values
        else:
            raise ValueError(
                'Number of colors ({}) does not match the number of mesh faces '
                '({}) nor the number of vertices ({}).'.format(
                    len(colors), len(geo.face_indices), len(geo.vertices))
            )


class DisplaySphere(SingleColorBase):
    """A sphere object with display properties."""

    type: constr(regex='^DisplaySphere$') = 'DisplaySphere'

    geometry: Sphere = Field(
        ...,
        description='Sphere for the geometry.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.shaded,
        description='Text to indicate the display mode (shaded, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )


class DisplayCone(SingleColorBase):
    """A cone object with display properties."""

    type: constr(regex='^DisplayCone$') = 'DisplayCone'

    geometry: Cone = Field(
        ...,
        description='Cone for the geometry.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.shaded,
        description='Text to indicate the display mode (shaded, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )


class DisplayCylinder(SingleColorBase):
    """A cylinder object with display properties."""

    type: constr(regex='^DisplayCylinder$') = 'DisplayCylinder'

    geometry: Cylinder = Field(
        ...,
        description='Cylinder for the geometry.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.shaded,
        description='Text to indicate the display mode (shaded, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )
