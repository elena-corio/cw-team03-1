import copy
from config import OFFSET_Z
from specklepy.objects.geometry import Mesh

def offset_mesh_vertices(mesh, offset_z: float):
    """
    Move mesh vertices in the Z direction.
    Vertices are stored as flat list: [x1, y1, z1, x2, y2, z2, ...]
    """
    if hasattr(mesh, "vertices") and mesh.vertices:
        new_mesh = Mesh()
        new_vertices = []
        for i in range(0, len(mesh.vertices), 3):
            new_vertices.append(mesh.vertices[i] )  # x 
            new_vertices.append(mesh.vertices[i + 1])  # y
            new_vertices.append(mesh.vertices[i + 2] + offset_z)  # z + offset
        new_mesh.vertices = new_vertices
    
    return new_mesh

def move_geometry(obj, offset_z: float):
    """
    Move geometry in the Z direction for mesh 
    """
    # Handle displayValue (common in Revit objects)
    display_value = getattr(obj, "displayValue", None) or getattr(obj, "@displayValue", None)
    if display_value:
        if isinstance(display_value, list):
            for mesh in display_value:
                offset_mesh_vertices(mesh, offset_z)
        else:
            offset_mesh_vertices(display_value, offset_z)

def modify_geometry(brep):
    # Deep copy - duplicates nested objects
    brep_copy = copy.deepcopy(brep)
    # Move geometry
    new_brep = move_geometry(brep_copy, OFFSET_Z)
    
    return new_brep