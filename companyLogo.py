from collections import Counter
import collections
from collections import OrderedDict
from operator import itemgetter
def count(String):
    # String = "aabbbccde"
    list1 = []
    for i in String:
        list1.append(i)

    c = Counter(list1)
    d = dict(c.most_common())
    r = sorted(d.items(), key=lambda x: (x[1] * -1, x[0]))
    for i in range(0,3):
        print(r[i][0],r[i][1])




if __name__ == '__main__':
    s = input()
    count(s)

