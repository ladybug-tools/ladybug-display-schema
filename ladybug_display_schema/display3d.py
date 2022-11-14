"""Schemas for geometric display objects in 3D space."""
from typing import Union
from pydantic import Field, constr

from .base import SingleColorBase, LineCurveBase, DisplayModes, \
    HorizontalAlignments, VerticalAlignments, Default
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

    radius: Union[Default, float] = Field(
        Default(),
        ge=0,
        description='Number for the radius with which the point should be displayed '
        'in pixels (for the screen) or millimeters (in print).'
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
        DisplayModes.surface,
        description='Text to indicate the display mode (surface, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )


class DisplayMesh3D(SingleColorBase):
    """A mesh in 3D space with display properties."""

    type: constr(regex='^DisplayMesh3D$') = 'DisplayMesh3D'

    geometry: Mesh3D = Field(
        ...,
        description='Mesh3D for the geometry.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.surface,
        description='Text to indicate the display mode (surface, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )


class DisplayPolyface3D(SingleColorBase):
    """A Polyface in 3D space with display properties."""

    type: constr(regex='^DisplayPolyface3D$') = 'DisplayPolyface3D'

    geometry: Polyface3D = Field(
        ...,
        description='Polyface3D for the geometry.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.surface,
        description='Text to indicate the display mode (surface, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )


class DisplaySphere(SingleColorBase):
    """A sphere object with display properties."""

    type: constr(regex='^DisplaySphere$') = 'DisplaySphere'

    geometry: Sphere = Field(
        ...,
        description='Sphere for the geometry.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.surface,
        description='Text to indicate the display mode (surface, wireframe, '
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
        DisplayModes.surface,
        description='Text to indicate the display mode (surface, wireframe, '
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
        DisplayModes.surface,
        description='Text to indicate the display mode (surface, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )


class DisplayText3D(SingleColorBase):
    """A text object in 3D space with display properties."""

    type: constr(regex='^DisplayText3D$') = 'DisplayText3D'

    text: str = Field(
        ...,
        description='A text string to be displayed in the 3D scene.'
    )

    plane: Plane = Field(
        ...,
        description='A ladybug-geometry Plane object to locate and orient the '
        'text in the 3D scene.'
    )

    height: float = Field(
        ...,
        gt=0,
        description='A number for the height of the text in the 3D scene.'
    )

    font: str = Field(
        'Arial',
        description='A text string for the font in which to draw the text. '
        'Note that this field may not be interpreted the same on all machines and '
        'in all interfaces, particularly when a machine lacks a given font.'
    )

    horizontal_alignment: HorizontalAlignments = Field(
        HorizontalAlignments.left,
        description='String to specify the horizontal alignment of the text.'
    )

    vertical_alignment: VerticalAlignments = Field(
        VerticalAlignments.bottom,
        description='String to specify the vertical alignment of the text.'
    )
