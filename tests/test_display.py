
from ladybug_display_schema.display2d import DisplayVector2D, DisplayPoint2D, \
    DisplayRay2D, DisplayLineSegment2D, DisplayPolyline2D, \
    DisplayArc2D, DisplayPolygon2D, DisplayMesh2D
from ladybug_display_schema.display3d import DisplayVector3D, DisplayPoint3D, \
    DisplayRay3D, DisplayPlane, DisplayLineSegment3D, DisplayPolyline3D, \
    DisplayArc3D, DisplayFace3D, DisplayMesh3D, DisplayPolyface3D
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'samples', 'display')


def test_display_vector2d():
    file_path = os.path.join(target_folder, 'vector_2d.json')
    DisplayVector2D.parse_file(file_path)


def test_point2d():
    file_path = os.path.join(target_folder, 'point_2d.json')
    DisplayPoint2D.parse_file(file_path)


def test_ray2d():
    file_path = os.path.join(target_folder, 'ray_2d.json')
    DisplayRay2D.parse_file(file_path)


def test_line_segment_2d():
    file_path = os.path.join(target_folder, 'line_segment_2d.json')
    DisplayLineSegment2D.parse_file(file_path)


def test_polyline_2d():
    file_path = os.path.join(target_folder, 'polyline_2d.json')
    DisplayPolyline2D.parse_file(file_path)


def test_arc_2d():
    file_path = os.path.join(target_folder, 'arc_2d.json')
    DisplayArc2D.parse_file(file_path)


def test_polygon_2d():
    file_path = os.path.join(target_folder, 'polygon_2d.json')
    DisplayPolygon2D.parse_file(file_path)


def test_mesh_2d():
    file_path = os.path.join(target_folder, 'mesh_2d.json')
    DisplayMesh2D.parse_file(file_path)


def test_display_vector3d():
    file_path = os.path.join(target_folder, 'vector_3d.json')
    DisplayVector3D.parse_file(file_path)


def test_point3d():
    file_path = os.path.join(target_folder, 'point_3d.json')
    DisplayPoint3D.parse_file(file_path)


def test_ray3d():
    file_path = os.path.join(target_folder, 'ray_3d.json')
    DisplayRay3D.parse_file(file_path)


def test_plane():
    file_path = os.path.join(target_folder, 'plane.json')
    DisplayPlane.parse_file(file_path)


def test_line_segment_3d():
    file_path = os.path.join(target_folder, 'line_segment_3d.json')
    DisplayLineSegment3D.parse_file(file_path)


def test_polyline_3d():
    file_path = os.path.join(target_folder, 'polyline_3d.json')
    DisplayPolyline3D.parse_file(file_path)


def test_arc_3d():
    file_path = os.path.join(target_folder, 'arc_3d.json')
    DisplayArc3D.parse_file(file_path)


def test_face_3d():
    file_path = os.path.join(target_folder, 'face_3d.json')
    DisplayFace3D.parse_file(file_path)


def test_mesh_3d():
    file_path = os.path.join(target_folder, 'mesh_3d.json')
    DisplayMesh3D.parse_file(file_path)


def test_polyface_3d():
    file_path = os.path.join(target_folder, 'polyface_3d.json')
    DisplayPolyface3D.parse_file(file_path)
