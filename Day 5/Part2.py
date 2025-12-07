def return_data():
    f = open(r'Day 5\Full.txt')
    ranges = []
    id_list = []
    set_ids = False
    for line in f:
        s_line = line.strip()
        if s_line == '':
            set_ids = True
            continue
        
        if set_ids:
            id_list.append(int(s_line))
        else:
            new_range = list(map(int,s_line.split('-')))
            ranges.append(new_range)
    return ranges, id_list

    

def main():
    ranges, id_list = return_data()

    fresh = 0
    uniques = [[i[0], i[1]] for i in set([tuple(i) for i in ranges])]
    uniques.sort(key=lambda item: (item[0], item[1]))
    
    searched_ranges = []

    for i in uniques:
        range_updated = False
        for s, row in enumerate(searched_ranges):
            if row[0] <= i[0] <= row[1] or row[0] <= i[1] <= row[1]:
                start = row[0] if row[0] <= i[0] else i[0]
                end = row[1] if row[1] >= i[1] else i[1]
                searched_ranges[s] = [start,end]
                range_updated = True
        if not range_updated:
            searched_ranges.extend([i])
    print(sum([i[1] - i[0] + 1 for i in searched_ranges]))
    

        
        

if __name__=='__main__':main()