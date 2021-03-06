"""generate openapi docs."""
import json
import argparse
from pkg_resources import get_distribution

from pydantic_openapi_helper.core import get_openapi
from pydantic_openapi_helper.inheritance import class_mapper
from ladybug_display_schema.geometry3d import Vector3D
from ladybug_display_schema.display3d import DisplayVector3D

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

modules = [
    {'module': [Vector3D], 'name': 'Geometry'},
    {'module': [DisplayVector3D], 'name': 'Display'},
]


def _process_name(name):
    """Process module name."""
    new_name = '-'.join(n.lower() for n in name.split())
    return new_name


for module in modules:
    # generate Recipe open api schema
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
