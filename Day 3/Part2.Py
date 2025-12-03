import itertools

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
    
    for banks in input_data:
        starting_pos = 0
        search_range = -11
        values = []
        
        while search_range <= 0:
            corpus = banks[starting_pos:search_range]
            if search_range == 0:
                corpus = banks[starting_pos:]
            high_val = max(i for i in corpus)
            values.append(high_val)
            starting_pos += corpus.index(str(high_val)) + 1
            search_range +=1

        volts.append(''.join(values))
    print(sum([int(i) for i in volts]))

if __name__=='__main__':main()