"""generate openapi docs."""
import json
import argparse
from pkg_resources import get_distribution

from pydantic_openapi_helper.core import get_openapi
from pydantic_openapi_helper.inheritance import class_mapper
from ladybug_display_schema.geometry2d import Vector2D, Point2D, Ray2D, LineSegment2D, \
    Polyline2D, Arc2D, Polygon2D, Mesh2D
from ladybug_display_schema.geometry3d import Vector3D, Point3D, Ray3D, Plane, \
    LineSegment3D, Polyline3D, Arc3D, Face3D, Mesh3D, Polyface3D, Sphere, Cone, Cylinder
from ladybug_display_schema.display2d import DisplayVector2D, DisplayPoint2D, \
    DisplayRay2D, DisplayLineSegment2D, DisplayPolyline2D, DisplayArc2D, \
    DisplayPolygon2D, DisplayMesh2D
from ladybug_display_schema.display3d import DisplayVector3D, DisplayPoint3D, \
    DisplayRay3D, DisplayPlane, DisplayLineSegment3D, DisplayPolyline3D, DisplayArc3D, \
    DisplayFace3D, DisplayMesh3D, DisplayPolyface3D, DisplaySphere, DisplayCone, \
    DisplayCylinder
from ladybug_display_schema.visualization import VisualizationSet, VisualizationMetaData

parser = argparse.ArgumentParser(description='Generate OpenAPI JSON schemas')

parser.add_argument('--version', help='Set the version of the new OpenAPI Schema')

args = parser.parse_args()

if args.version:
    VERSION = args.version.replace('v', '')
else:
    VERSION = '.'.join(get_distribution('ladybug_display_schema').version.split('.')[:3])
lic_url = "https://github.com/ladybug-tools/ladybug-display-schema/blob/master/LICENSE"

info = {
    "description": "",
    "version": VERSION,
    "title": "",
    "contact": {
        "name": "Ladybug Tools",
        "email": "info@ladybug.tools",
        "url": "https://github.com/ladybug-tools/ladybug-display-core"
    },
    "x-logo": {
        "url": "https://www.ladybug.tools/assets/img/ladybug-large.png",
        "altText": "Ladybug logo"
    },
    "license": {
        "name": "MIT",
        "url": lic_url
    }
}

all_geo = [
    Vector2D, Point2D, Ray2D, LineSegment2D, Polyline2D, Arc2D, Polygon2D, Mesh2D,
    Vector3D, Point3D, Ray3D, Plane, LineSegment3D, Polyline3D, Arc3D, Face3D, Mesh3D,
    Polyface3D, Sphere, Cone, Cylinder
]

all_dis = [
    DisplayVector2D, DisplayPoint2D, DisplayRay2D, DisplayLineSegment2D,
    DisplayPolyline2D, DisplayArc2D, DisplayPolygon2D, DisplayMesh2D,
    DisplayVector3D, DisplayPoint3D, DisplayRay3D, DisplayPlane, DisplayLineSegment3D,
    DisplayPolyline3D, DisplayArc3D, DisplayFace3D, DisplayMesh3D,
    DisplayPolyface3D, DisplaySphere, DisplayCone, DisplayCylinder
]

modules = [
    {'module': [VisualizationSet, VisualizationMetaData], 'name': 'Visualization'},
    {'module': all_geo, 'name': 'Geometry'},
    {'module': all_dis, 'name': 'Display'}
]


def _process_name(name):
    """Process module name."""
    new_name = '-'.join(n.lower() for n in name.split())
    return new_name


for module in modules:
    # generate open api schema
    print(f'Generating {module["name"]} documentation...')

    external_docs = {
        "description": "OpenAPI Specification with Inheritance",
        "url": f"./{_process_name(module['name'])}_inheritance.json"
    }

    openapi = get_openapi(
        module['module'],
        title=f'Ladybug {module["name"]} Schema',
        description=f'Ladybug {_process_name(module["name"])} schema.',
        version=VERSION, info=info,
        external_docs=external_docs
    )

    # write out the base openAPI schema
    with open(f'./docs/{_process_name(module["name"])}.json', 'w') as out_file:
        json.dump(openapi, out_file, indent=2)

    # with inheritance
    openapi = get_openapi(
        module['module'],
        title=f'Ladybug {module["name"]} Schema',
        description=f'Documentation for Ladybug {_process_name(module["name"])} schema',
        version=VERSION, info=info,
        inheritance=True,
        external_docs=external_docs
    )

    # write out the OpenAPI with inheritance
    with open(f'./docs/{_process_name(module["name"])}_inheritance.json', 'w') \
            as out_file:
        json.dump(openapi, out_file, indent=2)

    # add the mapper file
    with open(f'./docs/{_process_name(module["name"])}_mapper.json', 'w') as out_file:
        json.dump(class_mapper(module['module']), out_file, indent=2)

# generate schema for mode with inheritance but without descriminator
# we will use this file for generating redocly - the full model is too big, and the
# model with inheritance and discriminators is renders incorrectly
external_docs = {
    "description": "OpenAPI Specification with Inheritance",
    "url": "./visualization_inheritance.json"
}

openapi = get_openapi(
    [VisualizationSet, VisualizationMetaData],
    title='Ladybug Visualization Schema',
    description='Documentation for Honeybee model schema',
    version=VERSION, info=info,
    inheritance=True,
    external_docs=external_docs,
    add_discriminator=False
)

with open('./docs/visualization_redoc.json', 'w') as out_file:
    json.dump(openapi, out_file, indent=2)
