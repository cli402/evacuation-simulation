

import grid_info


def main():
    grid = grid_info.grid
    cell_size = grid_info.person_size    
    num_cols = 888
    num_rows = 634

    bit_data = [['0' for x in range(num_cols)] for y in range(num_rows)]

    for length, height, coords in grid:
        x_start = int(coords[0] / cell_size)
        y_start = int(coords[1] / cell_size)

        # a coordinate of (0, 0) indicates no real data is present, so skip it
        if ((x_start == 0) and (y_start == 0)):
            continue            

        x_size = int(length / cell_size)
        y_size = int(height / cell_size)

        y = y_start
        while y < (y_start + y_size):
            x = x_start
            while x < (x_start + x_size):
                bit_data[y][x] = '1'
                x += 1
            y += 1
    
    lines = [' '.join(row) for row in bit_data] 
   
    #write data to file
    with open("grid_bits.txt", "w") as fo:
        fo.write('\n'.join(lines))


if __name__ == '__main__':
    main()
