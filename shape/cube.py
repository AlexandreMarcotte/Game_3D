import numpy as np
import pyqtgraph.opengl as gl              # => Try to use pyopengl directly


class Cube:
    def __init__(self, s=(1, 1, 1), pos=(0, 0, 0)):
        self.x, self.y, self.z = pos
        self.sx, self.sy, self.sz = s

        self.verts = self.create_vertices()
        self.faces = self.create_faces()

        if s != (1, 1, 1):
            self.resize_vertices()
        if pos != (0, 0, 0):
            self.move_vertices()

        mesh_data = self.create_mesh_data()
        self.mesh_item = self.create_mesh_item(mesh_data)

    @staticmethod
    def create_faces():
        faces = np.array([
            np.array([0, 1, 2]), np.array([0, 3, 2]),
            np.array([4, 5, 6]), np.array([4, 7, 6]),
            np.array([0, 4, 7]), np.array([0, 3, 7]),
            np.array([1, 5, 6]), np.array([1, 2, 6]),
            np.array([0, 4, 5]), np.array([0, 1, 5]),
            np.array([3, 7, 6]), np.array([3, 2, 6])])
        return faces

    @staticmethod
    def create_vertices():
        verts = np.array([
            np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([1, 1, 0]), np.array([1, 0, 0]),
            np.array([0, 0, 1]), np.array([0, 1, 1]), np.array([1, 1, 1]), np.array([1, 0, 1])],
            dtype=float)
        return verts

    def create_mesh_data(self):
        return gl.MeshData(vertexes=self.verts, faces=self.faces)

    def create_mesh_item(self, mesh_item):
        return gl.GLMeshItem(
            meshdata=mesh_item, color=(0, 200, 0, 10), shader='shaded')

    def resize_vertices(self):
        for v in self.verts:
            v[0] *= self.sx
            v[1] *= self.sy
            v[2] *= self.sz

    def move_vertices(self):
        for v in self.verts:
            v[0] += self.x
            v[1] += self.y
            v[2] += self.z



def cube(s=(1,1,1), pos=(0, 0, 0)):
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
        np.array([0, 1, 2]), np.array([0, 3, 2]),
        np.array([4, 5, 6]), np.array([4, 7, 6]),
        np.array([0, 4, 7]), np.array([0, 3, 7]),
        np.array([1, 5, 6]), np.array([1, 2, 6]),
        np.array([0, 4, 5]), np.array([0, 1, 5]),
        np.array([3, 7, 6]), np.array([3, 2, 6])])

    cube = gl.MeshData(vertexes=verts, faces=faces)
    # cube = gl.MeshData.sphere(rows=2, cols=3)
    cube = gl.GLMeshItem(
            meshdata=cube, color=(0, 200, 0, 10), shader='shaded')

    # md = gl.MeshData.sphere(rows=20, cols=30)
    # m4 = gl.GLMeshItem(meshdata=md, smooth=True, shader='shaded', glOptions='opaque')
    # w.addItem(m4)

    return cube

