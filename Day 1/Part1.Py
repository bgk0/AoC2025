def return_data():
    f = open(r'\AdventOfCode\2025\Day 1\full.txt')
    data = []
    for line in f:
        s_line = line.strip()
        key, values = s_line[0], s_line[1:]
        data.append((key, int(values)))

    return data
               

def main():
    input_data = return_data()

    starting_point = 50
    current_point = starting_point
    found = 0
    print(f'The startingpoint is at {starting_point}')
    for moves in input_data:
        key = moves[0]
        steps = moves[1]
        
        actual_steps = steps if steps <= 100 else steps%100
        operation = '+' if key == 'R' else '-'
        current_point = eval(f'{current_point} {operation} {actual_steps}')
        if current_point < 0:
            current_point = 100 - abs(current_point)
        elif current_point > 99:
            current_point = current_point - 100
        
        if current_point == 100:
            current_point = 0
        print(f'The dial is rotating {key}{steps} ({actual_steps}) to point at {current_point}')

        if current_point == 0:
            found +=1

    print(found)
        
        

if __name__=='__main__':main()