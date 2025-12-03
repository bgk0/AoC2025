def return_data():
    f = open(r'\AdventOfCode\2025\Day 3\Full.txt')
    data = []
    for line in f:
        s_line = line.strip()
        data.append(s_line)

    return data


    
             

def main():
    input_data = return_data()

    volts = []

    x = len(input_data[1])
    y = input_data[1].index('9')

    print(x,y)

    for banks in input_data:
        cell_1 = -1
        cell_2 = -2
        for cell in banks:
            c = int(cell)

            if c > cell_1 and banks.index(cell) != len(banks)-1:
                cell_1 = c
                cell_2 = -2
            elif c > cell_2:
                cell_2 = c
        volts.append(int(f'{cell_1}{cell_2}'))

    print(sum(volts))
         


        
        

if __name__=='__main__':main()