def return_data():
    f = open(r'D:\MAC\Python\AdventOfCode\2025\Day 2\FullData.txt')
    data = []
    for line in f:
        s_line = line.strip()
        data = [list(map(int,i.split('-'))) for i in s_line.split(',')]

    return data

def check_digits(step):
    str_step = str(step)
    if len(str_step) % 2 == 0:
        half_step = int(len(str_step) / 2)
        half_code = str_step[:half_step]

        if str_step.count(half_code) > 1:
            return True
    

    return False
    
def check_digits2(step):
    str_step = str(step)
    length = len(str_step)
    if len(set(str_step)) == 1 and len(str_step) > 1:
        return True
    else: 
        for i in range(1,length+1):
            sub = str_step[:i]
            if str_step.count(sub) > 1:
                if str_step.replace(sub,"") == "":
                    return True
    return False           

def main():
    input_data = return_data()
    largest_step = 0
    bad_ids = []
    for i in input_data:
        start = i[0]
        end = i[1]
        x = [steps for steps in range(start, end+1) if check_digits2(steps)]
        if x: bad_ids.extend(x) 
    [print(i) for i in bad_ids]
    print(sum(bad_ids))

    
        
        

if __name__=='__main__':main()