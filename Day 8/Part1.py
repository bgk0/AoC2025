import math

def return_data():
    f = open(r'Day 8\Full.txt')
    cords = {}
    box = 1
    for line in f:
        cords[box] = [int(i) for i in line.strip().split(',')]
        box+=1
    return cords
    

def main():
    cords = return_data()
    circut = []

    lowest_connections = {

    }

    for k,v in cords.items():
        x,y,z = v
        distances = {}
        for i, n in cords.items():
            if i == k:
                continue
            if any(s in [f'{k}_{i}', f'{i}_{k}'] for s in list(lowest_connections.keys())):
                continue

            x2,y2,z2 = n
            weight = math.sqrt((x2 - x)**2 + (y2 - y)**2 + (z2 - z)**2)
            distances[f'{k}_{i}'] = weight
            
        distances = dict(sorted(distances.items(), key=lambda item: item[1]))
        if len(lowest_connections) < 1000:
            keys = list(distances.keys())[:1000]
            lowest_connections = {k: v for k, v in distances.items() if k in keys}
        else:
            current_low = list(distances.keys())[0]
            highest_low = list(lowest_connections.keys())[-1]
            if distances[current_low] > lowest_connections[highest_low]:
                continue

            curerent_ten = list(distances.keys())[:10000]
            distances = {k: v for k, v in distances.items() if k in curerent_ten}
            lowest_connections.update(distances)
            lowest_connections = dict(sorted(lowest_connections.items(), key=lambda item: item[1]))
            keys = list(lowest_connections.keys())[:1000]
            lowest_connections = {k: v for k, v in lowest_connections.items() if k in keys}

    skip_cords = []
    for key in cords:
        if str(key) in skip_cords:
            continue
            
        search_cords = [str(key)]
        found = [str(key)]
        while True:
            if len(search_cords) == 0:
                break
            find = search_cords[0]
            
            all_keys = [i.split('_') for i in lowest_connections if find in i.split('_')]
            all_keys = sum(all_keys, [])

            for i in all_keys:
                if i not in skip_cords and i != find:
                    search_cords.append(i)
            
            found = list(set(found+all_keys))
        
            search_cords.remove(find)
            skip_cords.append(find)
        
        circut.append(found)

    z = sorted(circut, key=len,reverse=True)
    largest_3 = [len(i) for i in sorted(circut, key=len,reverse=True)[:3]]
    print(math.prod(largest_3))
    print('')


if __name__=='__main__':main()