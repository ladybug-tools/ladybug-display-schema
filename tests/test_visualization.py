import os
from ladybug_display_schema.visualization import VisualizationSet

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'samples', 'vsf')


def test_visualization_set():
    file_path = os.path.join(target_folder, 'simple_vis.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_detailed():
    file_path = os.path.join(target_folder, 'detailed_vis.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_model():
    file_path = os.path.join(target_folder, 'model.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_model_face_attr():
    file_path = os.path.join(target_folder, 'model_face_attr.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_model_room_attr():
    file_path = os.path.join(target_folder, 'model_room_attr.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_model_text_attr():
    file_path = os.path.join(target_folder, 'model_text_attr.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_sunpath():
    file_path = os.path.join(target_folder, 'sunpath.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_sunpath2d():
    file_path = os.path.join(target_folder, 'sunpath2d.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_wind_profile():
    file_path = os.path.join(target_folder, 'wind_profile.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_wind_rose():
    file_path = os.path.join(target_folder, 'wind_rose.vsf')
    VisualizationSet.parse_file(file_path)


def test_visualization_set_hourly_plot():
    file_path = os.path.join(target_folder, 'hourly_plot.vsf')
    VisualizationSet.parse_file(file_path)
