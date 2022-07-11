"""Schemas for geometric display objects in 3D space."""
from pydantic import Field, constr

from .base import DisplayBaseModel, Color
from .geometry3d import Vector3D


class DisplayVector3D(DisplayBaseModel):

    type: constr(regex='^DisplayVector3D$') = 'DisplayVector3D'

    geometry: Vector3D = Field(
        ...,
        description='Vector3D for the geometry.'
    )

    color: Color = Field(
        ...,
        description='Color for the geometry.'
    )
