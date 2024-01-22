from typing import List

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider


class SimulationAnimation:
    def __init__(self, states: List[List], repeat: bool = False):
        self.states = states
        self.num_frames = len(states)

        # Create a figure without axes
        self.fig, self.axes = plt.subplots()
        self.fig.subplots_adjust(bottom=0.2)  # Adjust the bottom margin for the slider

        # Create an initial plot (assuming it's a 2D plot)
        self.image = plt.imshow(states[0], cmap="viridis")

        # Center the slider
        slider_width = 0.65
        slider_height = 0.03
        slider_x = (1 - slider_width) / 2  # Center the slider horizontally
        slider_y = 0.01  # Adjust the vertical position if needed
        self.ax_slider = plt.axes([slider_x, slider_y, slider_width, slider_height])

        self.slider = Slider(
            self.ax_slider, "Time Step", 0, self.num_frames - 1, valinit=0, valstep=1
        )

        # Add a legend for the color range
        self.fig.colorbar(self.image, orientation="vertical", label="Color Range")

        # Hide the axes completely
        self.axes.axes.get_xaxis().set_visible(False)
        self.axes.axes.get_yaxis().set_visible(False)

        # Set up the animation with repeat parameter
        self.ani = FuncAnimation(
            self.fig, self.update, frames=self.num_frames, blit=True, repeat=repeat
        )

        # Connect the slider to the update function
        self.slider.on_changed(self.update_slider)

    def set_title(self, title):
        self.fig.suptitle(title)

    def update(self, frame):
        current_state = self.states[frame]
        self.image.set_array(current_state)

        # Set the slider value to the current frame
        self.slider.set_val(frame)

        return [self.image]

    def update_slider(self, val):
        frame = int(val)
        current_state = self.states[frame]
        self.image.set_array(current_state)
        plt.draw()

    def show_animation(self):
        plt.show()
