import pyqtgraph.opengl as gl              # => Try to use pyopengl directly
import numpy as np


def pyramid(s=(1,1,1), pos=(0, 0, 0)):
    """
    Return a MeshData instance with vertexes and faces computed
    for a cube surface.
    """
    x, y, z = pos
    sx, sy, sz = s

    verts = np.array([
        np.array([0.5, 0.5, 0.5]),
        np.array([0, 0, 0]), np.array([0, 1, 0]),
        np.array([1, 1, 0]), np.array([1, 0, 0])],
        dtype=float)

    # Resize:
    for v in verts:
        v[0] *= sx
        v[1] *= sy
        v[2] *= sz

    # Move:
    for v in verts:
        v[0] += x
        v[1] += y
        v[2] += z

    faces = np.array([
        np.array([0, 1, 2]), np.array([0, 3, 2]),
        np.array([0, 4, 3]), np.array([0, 1, 4])])

    pyramid = gl.MeshData(vertexes=verts, faces=faces)
    pyramid = gl.GLMeshItem(
        meshdata=pyramid, color=(0, 200, 0, 0.5), shader='shaded')

    return pyramid


