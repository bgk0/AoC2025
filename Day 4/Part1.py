def return_data():
    f = open(r'Day 4\Full.txt')
    data = []
    for line in f:
        s_line = line.strip()
        data.append([i for i in s_line])

    return data

    

def main():
    input_data = return_data()
    
    rolls = []
    y_max = len(input_data)
    x_max = len(input_data[0])
    for y in range(y_max):
        for x in range(x_max):
            if input_data[y][x] == '@':
                rolls.append((y,x))
    checks = [-1,0,1]
    good_roll = []
    for roll in rolls:
        y=roll[0]
        x=roll[1]

        touching = 0
        for cy in checks:
            for cx in checks:
                new_y = y + cy
                new_x = x + cx
                if 0 <= new_y < y_max:
                    if 0 <= new_x < x_max:
                        if cy == 0 and cx == 0:
                            continue
                        elif input_data[new_y][new_x] == '@':
                            touching += 1
        
        if touching <= 3:
            good_roll.append(roll)
        

    print(len(good_roll))
        
        

if __name__=='__main__':main()