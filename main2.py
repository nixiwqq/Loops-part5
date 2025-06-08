def draw_chessboard(cell_size):
    for row in range(8):
        for i in range(cell_size):
            line = ""
            for col in range(8):
                if (row + col) % 2 == 0:
                    line += "*" * cell_size
                else:
                    line += "-" * cell_size
            print(line)


size = int(input("Введіть розмір клітинки: "))
draw_chessboard(size)
