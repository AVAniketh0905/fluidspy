from typing import List

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

from ..numerical.state import SimulationState


class SimulationAnimation:
    def __init__(self, states: List[List], repeat: bool = False):
        self.states = states
        self.num_frames = len(states)

        # Create a figure and axis
        self.fig, self.ax = plt.subplots()

        # Create an initial plot (assuming it's a 2D plot)
        self.image = self.ax.imshow(states[0], cmap="viridis")

        # Add a slider for controlling the time step
        self.ax_slider = plt.axes([0.1, 0.01, 0.65, 0.03])
        self.slider = Slider(
            self.ax_slider, "Time Step", 0, self.num_frames - 1, valinit=0, valstep=1
        )

        # Set up the animation with repeat parameter
        self.ani = FuncAnimation(
            self.fig, self.update, frames=self.num_frames, blit=True, repeat=repeat
        )

        # Connect the slider to the update function
        self.slider.on_changed(self.update_slider)

    def update(self, frame):
        current_state = self.states[frame]
        self.image.set_array(current_state)
        return [self.image]

    def update_slider(self, val):
        frame = int(val)
        current_state = self.states[frame]
        self.image.set_array(current_state)
        plt.draw()

    def show_animation(self):
        plt.show()
