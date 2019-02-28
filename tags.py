import sys



def get(line):
    x, y = line
    new_l = list()
    new_l.append(str(x))
    feed = y.split()
    new_l.append(feed[2:])
    return new_l, feed[0] == 'H'

def get_all_tegs(lists):
    all_tegs = list()
    kist = lists
    for el in kist:
        id = el[0]
        show = set(el[1])
        maybe = dict()
        dict_keys = maybe.keys()
        for x in kist:
            if id != x[0]:
                number = len(set(x[1]) - show)
                if number not in dict_keys:
                    maybe[number] = x
                    dict_keys = maybe.keys()
                if number == 0:
                    break
        sorted_keys = sorted(dict_keys)
        print(sorted_keys)
        new = list()
        found = maybe[sorted_keys[0]]
        new.append(str(id) + " " + str(found[0]))
        new.append(list(show.union(set(found[1]))))
        all_tegs.append(new)
        print(found)
        print(el)
        kist.remove(found)
        kist.remove(el)
    if len(kist) != 0:
        for i in range(0, len(kist), 2):
            new = list()
            new.append(str(kist[i][0]) + " " + str(kist[i+1][0]))
            setik = set(kist[i][1]).union(set(kist[i+1][1]))
            new.append(list(setik))
            all_tegs.append(new)
    print(all_tegs)
    print(len(all_tegs))
    return all_tegs

def output(name, lists):
    lines = [str(x[0]) for x in lists]
    with open(name, 'w') as f:
        lengtht = str(len(lines))
        f.write(lengtht)
        for i in lines:
            f.write("\n" + i)

def findMaxMin(elements):
    outIndex = []
    temp = 0
    centerSame = 0
    leftSame = 0
    rightSame = 0
    arrLength = len(elements)
    bestIndex = None
    els = elements
    first_s = True
    for i in els:
        if first_s:
            first_s = False
        else:
            first = 0
            first_set = set(i[1])
            print(i)
            for j in elements:
                if first != 0:
                    second = set(j[1])
                    center = first_set & second
                    left = (first_set - second).union(center)
                    right = (second - first_set).union(center)
                    leftSame = len(left)
                    rightSame = len(right)
                    centerSame = len(center)
                    minTegs = min(centerSame, leftSame, rightSame)
                    if temp < minTegs:
                        temp = minTegs
                        bestIndex = j
                else:
                    first += 1

                centerSame = 0
                leftSame = 0
                rightSame = 0
                temp = 0
        if bestIndex is None:
            outIndex.append(i)
            els.remove(i)
        else:
            outIndex.append(bestIndex)
            els.insert(0, bestIndex)
            els.remove(bestIndex)
        bestIndex = None
    return outIndex




def read_file(filename):
    with open(filename, 'r') as f:
        num = int(f.readline())
        all_lines = f.readlines()
        lines = [list(x[0]).append(x[1].split()) for x in zip(len(all_lines), all_lines)]
    print(lines[:50])

def read_another(filename):
    vertical = list()
    horizontal = list()
    with open(filename, 'r') as f:
        num = int(f.readline())
        all_lines = f.readlines()
        for x in enumerate(all_lines):
            line, ifHorizontal = get(x)
            if ifHorizontal:
                horizontal.append(line)
            else:
                vertical.append(line)
        print(vertical[:25])
        print(horizontal[:25])
        print(len(vertical))
        print(len(horizontal))

    return vertical, horizontal

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])
    #file = read_file(sys.argv[1])
    print("-------------------------")
    print("-------------------------")


    vert, horizontal = read_another(sys.argv[1])
    vertical = get_all_tegs(vert)
    #print(vertical)
    print(horizontal)
    alll = horizontal + vertical
    print(alll)
    out = findMaxMin(alll[:40000])
    output(sys.argv[2], out)
