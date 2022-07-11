import os
from ladybug_display_schema.geometry2d import Vector2D, Point2D, Ray2D, \
    LineSegment2D, Polyline2D, Arc2D, Polygon2D, Mesh2D
from ladybug_display_schema.geometry3d import Vector3D, Point3D, Ray3D, \
    Plane, LineSegment3D, Polyline3D, Arc3D, Face3D, Mesh3D, Polyface3D

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'samples', 'geometry')


def test_vector2d():
    file_path = os.path.join(target_folder, 'vector_2d.json')
    Vector2D.parse_file(file_path)


def test_point2d():
    file_path = os.path.join(target_folder, 'point_2d.json')
    Point2D.parse_file(file_path)


def test_ray2d():
    file_path = os.path.join(target_folder, 'ray_2d.json')
    Ray2D.parse_file(file_path)


def test_line_segment_2d():
    file_path = os.path.join(target_folder, 'line_segment_2d.json')
    LineSegment2D.parse_file(file_path)


def test_polyline_2d():
    file_path = os.path.join(target_folder, 'polyline_2d.json')
    Polyline2D.parse_file(file_path)


def test_arc_2d():
    file_path = os.path.join(target_folder, 'arc_2d.json')
    Arc2D.parse_file(file_path)


def test_polygon_2d():
    file_path = os.path.join(target_folder, 'polygon_2d.json')
    Polygon2D.parse_file(file_path)


def test_mesh_2d():
    file_path = os.path.join(target_folder, 'mesh_2d.json')
    Mesh2D.parse_file(file_path)


def test_vector3d():
    file_path = os.path.join(target_folder, 'vector_3d.json')
    Vector3D.parse_file(file_path)


def test_point3d():
    file_path = os.path.join(target_folder, 'point_3d.json')
    Point3D.parse_file(file_path)


def test_ray3d():
    file_path = os.path.join(target_folder, 'ray_3d.json')
    Ray3D.parse_file(file_path)


def test_plane():
    file_path = os.path.join(target_folder, 'plane.json')
    Plane.parse_file(file_path)


def test_line_segment_3d():
    file_path = os.path.join(target_folder, 'line_segment_3d.json')
    LineSegment3D.parse_file(file_path)


def test_polyline_3d():
    file_path = os.path.join(target_folder, 'polyline_3d.json')
    Polyline3D.parse_file(file_path)


def test_arc_3d():
    file_path = os.path.join(target_folder, 'arc_3d.json')
    Arc3D.parse_file(file_path)


def test_face_3d():
    file_path = os.path.join(target_folder, 'face_3d.json')
    Face3D.parse_file(file_path)


def test_mesh_3d():
    file_path = os.path.join(target_folder, 'mesh_3d.json')
    Mesh3D.parse_file(file_path)


def test_polyface_3d():
    file_path = os.path.join(target_folder, 'polyface_3d.json')
    Polyface3D.parse_file(file_path)
