def draw_line(length_tick, label=''):
    print('-' * length_tick + label)

def draw_center(length_tick):
    if length_tick > 0:
        draw_center(length_tick - 1)
        draw_line(length_tick)
        draw_center(length_tick - 1)

if __name__ == "__main__":
    len_ruler = int(input())
    len_tick = int(input())

    draw_line(len_tick, '0')

    for label in range(1 , len_ruler + 1):
        draw_center(len_tick - 1)
        draw_line(len_tick, str(label))