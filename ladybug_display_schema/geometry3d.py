"""Schemas for geometry objects in 3D space."""
from pydantic import BaseModel, Field, constr


class Vector3D(BaseModel):

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
