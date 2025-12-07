def return_data():
    f = open(r'Day 6\Full.txt')
    cleaned = []
    for line in f:
        s_line = line.strip()
        cleaned.append([i for i in s_line.split(' ') if i])
    
    formatted = []
    for col in range(len(cleaned[0])):
        new_row = []
        for row in range(len(cleaned)):
            new_row.append(cleaned[row][col])
        formatted.append(new_row)
    
    return formatted


    

def main():
    equations = return_data()
    
    total = []
    for e in equations:
        values = e[0:-1]
        operator = e[-1]
        eq_str = f' {operator} '.join(values)
        total.append(eval(eq_str))
    
    print(sum(total))

if __name__=='__main__':main()