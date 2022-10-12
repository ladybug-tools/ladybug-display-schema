import os
from ladybug_display_schema.visualization import VisualizationSet

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'samples')


def test_visualization_set():
    file_path = os.path.join(target_folder, 'visualization.json')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_detailed():
    file_path = os.path.join(target_folder, 'visualization_detailed.json')
    VisualizationSet.parse_file(file_path)
