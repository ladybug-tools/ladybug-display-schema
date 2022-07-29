import os
from ladybug_display_schema.graphic import GraphicContainer

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'samples')


def test_graphic_container():
    file_path = os.path.join(target_folder, 'graphic.json')
    GraphicContainer.parse_file(file_path)
