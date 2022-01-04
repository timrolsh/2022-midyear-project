import random
import cv2
import numpy as np
import matplotlib.pyplot as plt


class Field:
    def __init__(self, width, height):
        self.data = [0] * width * height
        self.height = height
        self.width = width

    def set(self, x, y, alive):
        self.data[self._get_idx(x, y)] = (1 if alive else 0)

    def get(self, x, y):
        if x >= self.width:
            x -= self.width
        elif x < 0:
            x += self.width
        if y >= self.height:
            y -= self.height
        elif y < 0:
            y += self.height
        return self.data[self._get_idx(x, y)]

    def neighbours(self, x, y):
        return self.get(x - 1, y - 1) + self.get(x, y - 1) + self.get(x + 1, y - 1) + \
               self.get(x - 1, y) + self.get(x + 1, y) + \
               self.get(x - 1, y + 1) + self.get(x, y + 1) + self.get(x + 1, y + 1)

    def alive(self):
        return sum(self.data) > 0

    def _get_idx(self, x, y):
        return x + y * self.width

    @classmethod
    def from_config(cls, initial_configuration):
        width = 0
        lines = initial_configuration.split('\n')
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            width = max(width, len(lines[i]))
        field = Field(max(50, width), max(30, len(lines)))
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                field.set(x, y, lines[y][x] == '#')
        return field


class Life:

    def __init__(self, width=50, height=30, dot_size=10, initial_configuration=None):
        self.exit = False
        self.round = 1
        self.width = width
        self.height = height
        self.dot_size = dot_size
        if initial_configuration:
            self.field = Field.from_config(initial_configuration)
            self.width = self.field.width
            self.height = self.field.height
        else:
            self.field = Field(width, height)
            self.populate()

        self.plot = None
        self.init_ui()
        self.start()

    def populate(self):
        for i in range(int(self.width * self.height / 10)):
            r = random.uniform(0, self.width * self.height)
            x = int(r % self.width)
            y = int(r / self.width)
            self.field.set(x, y, True)

    def evolve(self):
        new_field = Field(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                alive = self.field.get(x, y)
                neighbours = self.field.neighbours(x, y)
                if alive:
                    new_field.set(x, y, 2 <= neighbours <= 3)
                else:
                    new_field.set(x, y, neighbours == 3)
        self.field = new_field

    def draw(self):
        canvas = self.clear_canvas()
        cv2.rectangle(canvas, pt1=(0, 0),
                      pt2=(self.width * self.dot_size - 1, self.height * self.dot_size - 1),
                      color=(100, 0, 0),
                      thickness=1)
        for y in range(self.height):
            for x in range(self.width):
                if self.field.get(x, y):
                    cv2.rectangle(canvas,
                                  pt1=(x * self.dot_size, y * self.dot_size),
                                  pt2=((x + 1) * self.dot_size - 2, (y + 1) * self.dot_size - 2),
                                  color=(0, 0, 0),
                                  thickness=-1)
        self.plot.clear()
        self.plot.imshow(canvas)
        self.plot.set_axis_off()
        self.plot.set_title(f"Round: {self.round}")

    def handle_close(self, evt):
        self.exit = True

    def init_ui(self):
        fig, axs = plt.subplots()
        self.plot = axs
        plt.show(block=False)
        fig.suptitle("Game of Life")
        fig.canvas.mpl_connect('close_event', self.handle_close)

    def clear_canvas(self):
        return 255 * np.ones(shape=[self.dot_size * self.field.height,  # height
                                    self.dot_size * self.field.width,  # width
                                    3],
                             dtype=np.uint8)

    def start(self):
        while not self.exit:
            self.draw()
            self.evolve()
            self.round += 1

            if not self.field.alive():
                break
            plt.pause(.5)


def main():
    Life(dot_size=5, initial_configuration="""






    .     ####                  #####                         ######               .











    .                           ##########                  ########               .









    .                                 #  
    .                                # #
    .......... ###                  #   #
    ..........#   #                  # #
    .......... ###                    #





    """)


if __name__ == "__main__":
    main()
