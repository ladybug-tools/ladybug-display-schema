"""Schemas for geometry objects in 3D space."""
from pydantic import BaseModel, Field, constr


class Vector3D(BaseModel):

    type: constr(regex='^Vector3D$') = 'Vector3D'

    x_coord: float = Field(
        ...,
        description='Number for X coordinate.',
        alias='x'
    )

    y_coord: float = Field(
        ...,
        description='Number for Y coordinate.',
        alias='y'
    )

    z_coord: float = Field(
        ...,
        description='Number for Z coordinate.',
        alias='z'
    )
