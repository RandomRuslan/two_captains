import random
import copy
from PIL import Image

def get_cross():
    cell = []
    for i in range(10):
        for j in range(10):
            cell.append(1 if (i == j or i == 9 - j) and 0 < i < 9 else 0)

    return cell

def get_zero():
    cell = [0] * (10 * 10)
    for i in range(3, 7):
        for j in [1, 8]:
            cell[i*10+j] = 1
            cell[j*10+i] = 1

    cell[2*10+2] = 1
    cell[7*10+2] = 1
    cell[2*10+7] = 1
    cell[7*10+7] = 1
    return cell

def get_death():
    cell = [1] * (10 * 10)
    return cell
    # cell = [0] * (10 * 10)
    # for i in range(4, 6):
    #     for j in range(2, 8):
    #         cell[i*10+j] = 1
    #         cell[j*10+i] = 1
    #
    # return cell

def draw_map(map):
    img = Image.new('RGBA', (56, 56))
    pixels = img.load()
    for i in range(56):
        for j in range(56):
            pixels[j, i] = (0,0,0) if map[i*56+j] else (255,255,255)

    for i in range(0,56,11):
        for j in range(56):
            pixels[j, i] = (0,0,0)
            pixels[i, j] = (0,0,0)

    img.save('map.png')
    img.close()

def input_cell(map, cell, i, j):
    for k in range(len(cell)):
        if cell[k] == 1:
            x = k // 10
            y = k % 10
            map[(1+i)*56 + (1+j)*1 + i*56*10 + j*10 + x*56 + y] = 1

def print_map(map, side=56):
    print('-' * 10)

    for i in range(side):
        for j in range(side):
            print(map[i * side + j], end='')
        print()

    print('-' * 10)

def get_words_location(n=9, team_count=2):
    cells = [i for i in range(25)]
    crosses = set()
    zeros = set()

    for _ in range(n):
        x = random.choice(cells)
        crosses.add(x)
        cells.remove(x)

    for _ in range(n-1):
        x = random.choice(cells)
        zeros.add(x)
        cells.remove(x)

    death = random.choice(cells)
    return death, crosses, zeros

def main():
    n = 9 # max count team's words
    death, crosses, zeros = get_words_location(n)
    map = [0] * (56 * 56)

    print(crosses, zeros)
    cross = get_cross()
    zero = get_zero()

    for i in range(5):
        for j in range(5):
            point = i*5 + j
            if point in crosses:
                input_cell(map, cross, i, j)
            elif point in zeros:
                input_cell(map, zero, i, j)
            elif point == death:
                input_cell(map, get_death(), i, j)

    draw_map(map)


if __name__ == '__main__':
    main()
