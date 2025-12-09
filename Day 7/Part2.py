def return_data():
    f = open(r'Day 7\Full.txt')
    field = []
    start = []
    for line in f:
        row = [i for i in line.strip()]
        if 'S' in row:
            y = 0
            x = row.index("S")
            start = [y,x]
        field.append(row)
    
    return field, start

def main():
    field, start = return_data()

    next_check = [start]

    while True:
        if len(next_check) == 0:
            break
        y,x = next_check[0]
        next_check.pop(0)
        next_y = y + 1
        x_pl = x + 1
        x_mi = x - 1
        if x < 0 or x == len(field[0]):
            continue
        elif next_y < 0 or next_y == len(field):
            continue
        elif field[next_y][x] == '.':
            
            beam_count = 1 if field[y][x] == 'S' else field[y][x]

            next_check.append([next_y, x])
            field[next_y][x] = str(beam_count)
        elif field[next_y][x] == '^':
            left_beam = field[next_y][x_mi]
            right_beam = field[next_y][x_pl] 

            if left_beam != '.':
                field[next_y][x_mi] = str(int(field[next_y][x_mi]) + int(field[y][x]))
            elif field[y][x_mi] != '.':
                field[next_y][x_mi] = str(int(field[y][x_mi]) + int(field[y][x]))
            else:
                field[next_y][x_mi] =  field[y][x]

            if right_beam != '.':
                field[next_y][x_pl] = str(int(field[next_y][x_pl]) + int(field[y][x]))
            elif field[y][x_pl] != '.':
                field[next_y][x_pl] = str(int(field[y][x_pl]) + int(field[y][x]))
            else:
                field[next_y][x_pl] =  field[y][x]

            next_check.extend([[next_y, x_mi], [next_y, x_pl]])


    print(sum([int(i) for i in field[-1] if i not in ['S','.']]))
        

if __name__=='__main__':main()