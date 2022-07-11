from ladybug_display_schema.geometry3d import Vector3D
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'samples', 'geometry')


def test_vector3d():
    file_path = os.path.join(target_folder, 'vector_3d.json')
    Vector3D.parse_file(file_path)
