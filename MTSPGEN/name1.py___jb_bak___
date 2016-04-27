import urllib2
import json
import random
import itertools


STOPS = []
# DISTANCE MATRIX
GENERATIONSIZE = 10
DURATION_FACTOR = 10;
DESTINATION_FACTOR = 1;

def divide(lst, min_size, split_size):
    it = iter(lst)
    size = len(lst)
    for i in range(split_size - 1,0,-1):
        s = random.randint(min_size, size -  min_size * i)
        yield list(itertools.islice(it,0,s))
        size -= s
    yield list(it)


def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

filename = 'data.txt'
f = open(filename)
data = f.readlines()
for i in data:
    STOPS.append(i[:-1].replace(' ','%20'))

urlprefix="https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial"
urlorigin="&origins="
urldestination="&destinations="
urlsuffix="&key=AIzaSyC_FeMZPmb73-GYUQ1gjqbLzBsxtDuqwH4"

DISTANCEMATRIX = [[0]*len(STOPS) for i in range(len(STOPS))]
DURATIONMATRIX = [[0]*len(STOPS) for i in range(len(STOPS))]

for i in range(0,len(STOPS)):
    for j in range(0,len(STOPS)):
        if(i<j):
            url = urlprefix+urlorigin+STOPS[i]+urldestination+STOPS[j]+urlsuffix
            print url
            content = urllib2.urlopen(url).read()
            data = json.loads(content)
            t = data["rows"][0]["elements"][0]["distance"]["value"]
            DISTANCEMATRIX[i][j] = t
            DISTANCEMATRIX[j][i] = t

            t2 = data["rows"][0]["elements"][0]["duration"]["value"]
            DURATIONMATRIX[i][j] = t2
            DURATIONMATRIX[j][i] = t2

print "Distrance Matrix :",DISTANCEMATRIX
print "Duration Matrix :",DURATIONMATRIX


#/////////////////////////////////////////////////////////////////////////////////////////////////
#   MTSP

def fitness(y):
    sum = 0
    sum_time = 0
    for j in range(0,len(y)):
        y[j].insert(0,0)
        y[j].append(0)
        #print "debug_path",y[j]
        for i in range(0,len(y[j])-1):
            #print "debug_distance[",y[j][i],"][",y[j][i+1],"]:",DISTANCEMATRIX[y[j][i]][y[j][i+1]]
            sum = sum + DISTANCEMATRIX[y[j][i]][y[j][i+1]]
            sum_time = sum_time + DURATIONMATRIX[y[j][i]][y[j][i+1]]
        #print "\n"
    #print "debug_sum :",sum
    return sum+(sum_time*DURATION_FACTOR)

def mtsp(x,evolutionFlag):

    print "Alpha Parent : ",x,

    #reproduction
    generation = []
    for i in range(0,GENERATIONSIZE):
        temp = []
        for j in x:
            temp.append(random.sample(j,len(j)))
        generation.append(temp)
    print "\nChild Generation : ",generation

    #finding alpha parent
    fitnessList = []
    for i in range(0,len(generation)):
        #print "debug_fitness",fitnessList
        fitnessList.append(fitness(generation[i]))
    print "fitness score : ",fitnessList

    #finding alpha
    parentindex = fitnessList.index(min(fitnessList))
    bestchild = fitnessList[parentindex]
    print "Best Child : ",generation[parentindex],"  Cost : ",bestchild
    print "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

    prunedelement = []
    #pruning the origin
    for i in generation[parentindex]:
        t1 = remove_values_from_list(i,0)
        prunedelement.append(t1)

    if(evolutionFlag > bestchild):
        return mtsp(prunedelement,bestchild)
    else:
        print "Optimal Solution" , generation[parentindex],"  Cost : ",bestchild
        f = []
        f.append(generation[parentindex])
        f.append(bestchild)
        return f


tag = []

for j in range(2,len(STOPS)):
    initialparent= []
    for i in range(1,len(STOPS)):
        initialparent.append(i)
    x = list(divide(initialparent,1,j))
    print x
    tag.append(mtsp(x,1000000000))

min = 1000000000
minindex =0
for i in tag:
    if(i[1]<min):
        min = i[1]
        minindex = tag.index(i)

print "M-CHILD",tag
print "M-CHILD OPTIMAL SOLUTION :",tag[minindex]


st = ""
for i in tag[0][0]:
    st = st + "\n"
    for j in i:
       st = st+STOPS[j].replace("%20"," ")+"  "
print st



