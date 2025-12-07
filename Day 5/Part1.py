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
    for id in id_list:
        for id_range in ranges:
            start , finish = id_range

            if start <= id <= finish:
                fresh+=1
                break
    print(fresh)
    

        
        

if __name__=='__main__':main()