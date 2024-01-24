from typing import List

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider


class SliderHandler:
    def __init__(self, ax, num_frames):
        self.slider = Slider(ax, "Time Step", 0, num_frames - 1, valinit=0, valstep=1)

    def on_changed(self, callback):
        self.slider.on_changed(callback)

    def set_value(self, value):
        self.slider.set_val(value)


class PlottingHandler:
    def __init__(self, states):
        self.states = states
        self.num_frames = len(states)

        self.fig, self.axes = plt.subplots()
        self.fig.subplots_adjust(bottom=0.2)

        self.image = plt.imshow(states[0], cmap="viridis")

        self.fig.colorbar(self.image, orientation="vertical", label="Color Range")
        self.axes.axes.get_xaxis().set_visible(False)
        self.axes.axes.get_yaxis().set_visible(False)

    def update_plot(self, frame):
        current_state = self.states[frame]
        self.image.set_array(current_state)

    def set_title(self, title):
        self.axes.set_title(title)

    def show_plot(self):
        plt.show()


class UpdateHandler:
    def __init__(self, plotting_handler, slider_handler):
        self.plotting_handler = plotting_handler
        self.slider_handler = slider_handler

    def update(self, frame):
        self.plotting_handler.update_plot(frame)
        self.slider_handler.set_value(frame)
        return [self.plotting_handler.image]


class SimulationAnimation:
    def __init__(self, states: List[List], repeat: bool = False):
        self.plotting_handler = PlottingHandler(states)

        ax_slider = self.plotting_handler.fig.add_axes([0.2, 0.01, 0.65, 0.03])
        self.slider_handler = SliderHandler(ax_slider, len(states))
        self.update_handler = UpdateHandler(self.plotting_handler, self.slider_handler)

        self.ani = FuncAnimation(
            self.plotting_handler.fig,
            self.update_handler.update,
            frames=len(states),
            blit=True,
            repeat=repeat,
        )

        self.slider_handler.on_changed(self.update_handler.update)

    def set_title(self, title):
        self.plotting_handler.set_title(title)

    def show_animation(self):
        self.plotting_handler.show_plot()
