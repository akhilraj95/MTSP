import random
import itertools
def divide(lst, min_size, split_size):
    it = iter(lst)
    size = len(lst)
    for i in range(split_size - 1,0,-1):
        s = random.randint(min_size, size -  min_size * i)
        yield list(itertools.islice(it,0,s))
        size -= s
    yield list(it)

for j in range(1,5):
    initialparent= []
    for i in range(1,5):
        initialparent.append(i)
    x = list(divide(initialparent,1,j))
    print x




print list(divide([1,2,3,4,5,6,7,8],1,5))
