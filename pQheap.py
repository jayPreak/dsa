H = [0]*50
size = -1

#to return index of parent node of given node
def parent(i):
    return((i-1)//2)

#to return index of left node of given node
def leftChild(i):
    return((2*i)+1)

#to return index of right node of given node
def rightChild(i):
    return((2*i)+2)

def bubbleUp(i):
    while(i>0 and H[parent(i)]<H[i]):
        swap(parent(i), i)

        i = parent(i)

def bubbleDown(i):
    maxIndex = i
    l = leftChild(i)
    r = rightChild(i)

    if (l <= size and H[l]>H[maxIndex]):
        maxIndex = l
    if (r <= size and H[r]>H[maxIndex]):
        maxIndex = r

    if (i != maxIndex):
        swap(i, maxIndex)
        bubbleDown(maxIndex)

def insert(p):
    global size
    size += 1
    H[size] = p

    bubbleUp(size)

#to extract elem w max priority?XD (ahh to like swap root and last, to help w deletion ykyk)
def extractMax():
    global size
    result = H[0]

    H[0] = H[size]
    size = size - 1

    bubbleDown(0)
    return result

def changePriority(i, p):
    oldp = H[i]
    H[i] = p

    if (p > oldp):
        bubbleUp(i)
    else:
        bubbleDown(i)

def getMax():
    return H[0]

def Remove(i):
    H[i] = getMax() + 1
    bubbleUp(i)
    extractMax()

def swap(i, j):
    temp = H[i]
    H[i] = H[j]
    H[j] = temp

insert(45)
insert(20)
insert(14)
insert(12)
insert(31)
insert(7)
insert(11)
insert(13)
insert(7)
   
i = 0
   
# Priority queue before extracting max
print("Priority Queue : ", end = "")
while (i <= size) :
 
    print(H[i], end = " ")
    i += 1
   
print()
   
# Node with maximum priority
print("Node with maximum priority :" ,  extractMax())
   
# Priority queue after extracting max
print("Priority queue after extracting maximum : ", end = "")
j = 0
while (j <= size) :
 
    print(H[j], end = " ")
    j += 1
   
print()
   
# Change the priority of element
# present at index 2 to 49
changePriority(2, 49)
print("Priority queue after priority change : ", end = "")
k = 0
while (k <= size) :
 
    print(H[k], end = " ")
    k += 1
   
print()
   
# Remove element at index 3
Remove(3)
print("Priority queue after removing the element : ", end = "")
l = 0
while (l <= size) :
 
    print(H[l], end = " ")
    l += 1


