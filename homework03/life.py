import pygame
from pygame.locals import *
import random


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10) -> None:
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

    def draw_grid(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        # Создание списка клеток
        self.clist = self.cell_list()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.draw_grid()
            self.draw_cell_list(self.clist)
            self.update_cell_list(self.clist)
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True) -> list:
        """ Создание списка клеток.

        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        if randomize:
            for row in range(self.cell_height):
                self.clist.append([])
                for col in range(self.cell_width):
                    self.clist[row].append(random.randint(0, 1))
        else:
            for row in range(self.cell_height):
                self.clist.append([])
                for col in range(self.cell_width):
                    self.clist[row].append(0)

        return self.clist

    def draw_cell_list(self, clist):
        """ Отображение списка клеток

        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for row in range(self.cell_height):
            for col in range(self.cell_width):
                x = row * self.cell_size + 1
                y = col * self.cell_size + 1
                edge = self.cell_size - 1
                if clist[row][col]:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                        (x, y, edge, edge))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                        (x, y, edge, edge))

    def get_neighbours(self, cell: tuple) -> list:
        """ Вернуть список соседей для указанной ячейки

        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        for row in range(cell[0]-1, cell[0]+2):
            if row < 0 or row >= len(self.clist):
                continue
            for col in range(cell[1]-1, cell[1]+2):
                if (row, col) == cell:
                    continue
                if col < 0 or col >= len(self.clist[row]):
                    continue
                neighbours.append(self.clist[row][col])

        return neighbours

    def update_cell_list(self, cell_list: list) -> list:
        """ Выполнить один шаг игры.

        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.

        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = []
        for row in range(len(cell_list)):
            new_clist.append([])
            for col in range(len(cell_list[row])):
                neighbours = self.get_neighbours((row, col))
                value = 0
                for i in neighbours:
                    value += i
                if cell_list[row][col] == 0 and value == 3:
                    new_clist[row].append(1)
                elif cell_list[row][col] == 0 and value != 3:
                    new_clist[row].append(0)
                elif cell_list[row][col] == 1 and (3 < value or value < 2):
                    new_clist[row].append(0)
                elif cell_list[row][col] == 1 and (1 < value < 4):
                    new_clist[row].append(1)
        self.clist = new_clist

        return self.clist

if __name__ == '__main__':
    game = GameOfLife(500, 500, 20, 10)
    game.run()
