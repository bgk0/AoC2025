def return_data():
    f = open(r'Day 7\Full.txt')
    field = []
    cleaned = []
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

    splits = []
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
            next_check.append([next_y, x])
            field[next_y][x] = '|'
        elif field[next_y][x] == '^':
            splits.append([next_y, x])
            next_check.extend([[y, x_mi], [y, x_pl]])

      
    print(len(splits))
    """
    for y in range(len(field)):
        print(field[y])
    """
        
            

        



if __name__=='__main__':main()