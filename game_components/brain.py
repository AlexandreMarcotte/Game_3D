import pyqtgraph.opengl as gl
import numpy as np
from random import randint


class Brain:
    def __init__(self, win, square_size):
        self.square_size = square_size

        self.add_brain_lines(win)

        self.curent_angle = 0
        self.angle_corresponding_to_mvt = {'l': 0, 'j': 180, 'i': 90, 'k': -90}

    def add_brain_lines(self, win):
        neuron_width = 1
        self.neurons = []
        for i in range(-5, 6):
            if i == 0:
                neuron_width = 8
            else:
                neuron_width = 1

            for j in range(-5, 6):
                top_pos = [i * self.square_size, j * self.square_size, 10]
                self.neurons.append(gl.GLLinePlotItem(
                    pos=np.array([[-1.5, 1.5, 0], top_pos]),
                    color=np.array([[200, 200, 200, 0.5], [0, 0, 200, 0.5]]),
                    width=neuron_width))
                win.addItem(self.neurons[-1])

    def translate(self, translate_arr):
        for neuron in self.neurons:
            neuron.translate(*translate_arr)

    def rotate(self, body_mvt, head_pos):
        temp_pos = np.array(head_pos)
        for neuron in self.neurons:
            angle_to_rotate = self.curent_angle - self.angle_corresponding_to_mvt[body_mvt]
            neuron.translate(*(-temp_pos))
            neuron.rotate(angle_to_rotate, 0, 0, 1)
            neuron.translate(*temp_pos)
        self.curent_angle = self.angle_corresponding_to_mvt[body_mvt]

    def update_neurons_weight(self):
        x_rand = randint(0, 10)
        y_rand = randint(0, 10)
        self.neurons[x_rand * y_rand].color = [100, 0, 0, 50]



