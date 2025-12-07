def return_data():
    f = open(r'Day 6\Full.txt')
    cleaned = []
    for line in f:
        cleaned.append(line.replace('\n',''))
    
    indexes = []
    for id, i in enumerate(cleaned[-1]):
        if i != ' ' and id != 0:
            indexes.append(id-1)

    for id, row in enumerate(cleaned):
        for index in indexes:
            cleaned[id] = cleaned[id][:index] + '|' + cleaned[id][index+1:]
    
    cleaned = [i.split('|') for i in cleaned]

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

        max_index = max([len(i) for i in values])
        values = [i.zfill(max_index) for i in values]
        
        cella_value = []
        for c in range(len(values[0])):
            char = -1 - c
            val = ''
            for v in values:
                if v[char] != '0':
                    val+= v[char]
            cella_value.append(val)
            val = ''

        eq_str = f' {operator} '.join(cella_value)
        total.append(eval(eq_str))
    
    print(sum(total))

if __name__=='__main__':main()