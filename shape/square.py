import numpy as np
import pyqtgraph.opengl as gl              # => Try to use pyopengl directly


def square(s=(1,1,1), pos=(0, 0, 0)):
    """
    Return a MeshData instance with vertexes and faces computed
    for a cube surface.
    """
    x, y, z = pos
    sx, sy, sz = s

    verts = np.array([
        np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([1, 1, 0]), np.array([1, 0, 0]),
        np.array([0, 0, 1]), np.array([0, 1, 1]), np.array([1, 1, 1]), np.array([1, 0, 1])],
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
            np.array([0, 1, 2]), np.array([0, 3, 2])])

    cube = gl.MeshData(vertexes=verts, faces=faces)
    # cube = gl.MeshData.sphere(rows=2, cols=3)
    cube = gl.GLMeshItem(
        meshdata=cube,
        color=(0, 200, 0, 10), edgeColor=(200, 0, 0, 200), drawEdge=True, shader='shaded')

    # md = gl.MeshData.sphere(rows=20, cols=30)
    # m4 = gl.GLMeshItem(meshdata=md, smooth=True, shader='shaded', glOptions='opaque')
    # w.addItem(m4)

    return cube
