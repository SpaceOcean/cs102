import pygame
from pygame.locals import *
import random
from copy import deepcopy


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        clist = CellList(self.cell_height, self.cell_width, randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            x = 0
            y = 0
            csize = self.cell_size
            for cell in clist:
                if cell.is_alive():
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                        [x, y, csize, csize])
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                        [x, y, csize, csize])
                x += csize
                if x >= self.width:
                    x = 0
                    y += csize
            clist.update()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


class Cell:

    def __init__(self, row, col, state=False):
        self.row = row
        self.col = col
        self.state = state

    def is_alive(self):

        return self.state


class CellList:

    def __init__(self, nrows, ncols, randomize=False):
        self.nrows = nrows
        self.ncols = ncols
        for row in range(nrows):
            for col in range(ncols):
                if randomize:
                    self.clist = Cell(row, col, random.randint(0, 1))
                else:
                    self.clist = Cell(row, col, 0)

    def get_neighbours(self, cell):
        neighbours = []
        for neighbours_row in range(cell.row-1, cell.row+2):
            if neighbours_row < 0 or neighbours_row > self.nrows - 1:
                continue
            for neighbours_col in range(cell.col-1, cell.col+2):
                if (neighbours_row, neighbours_col) == (cell.row, cell.col):
                    continue
                if neighbours_col < 0 or neighbours_col > self.ncols - 1:
                    continue
                neighbours.append(self.clist[neighbours_row][neighbours_col])

        return neighbours

    def update(self):
        new_clist = copy.deepcopy(self.clist)
        for cell in self:
            neighbours = self.get_neighbours(cell)
            value = 0
            for i in neighbours:
                value += i.is_alive()
            if cell.is_alive():
                if not (1 < value < 4):
                    new_clist[cell.row][cell.col].state = 0
            else:
                if value == 3:
                    new_clist[cell.row][cell.col].state = 1
        self.clist = new_clist

        return self

    def __iter__(self):
        self.row, self.col = 0, 0

        return self

    def __next__(self):
        if self.row == self.nrows:
            raise StopIteration

        cell = self.clist[self.row][self.col]
        self.col += 1
        if self.col == self.ncols:
            self.row += 1
            self.col = 0

        return cell

    def __str__(self):
        str = ''
        for row in range(self.nrows):
            for col in range(self.cols):
                if self.clist[row][col].state:
                    str += '1'
                else:
                    str += '0'
            str += '\n'

        return str

    @classmethod
    def from_file(cls, filename):
        clist = []
        with open(filename) as file:
            for row, line in enumerate(file):
                for col, state in enumerate(line):
                    if state in "01":
                        clist.append(Cell(row, col, int(state)))

        return clist
