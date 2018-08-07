import timeit

import random    
my_randoms=[]    
for i in range (100):    
    my_randoms.append(random.randrange(1,10001,1))    
myList = my_randoms



"""myList = [ 6931, 3546, 7202, 8192, 7631, 753, 6906, 2445, 1468, 9134, 2947, 1080, 3549, 5164, 5287, 4453, 2853, 3077, 1843, 502, 2866, 7069, 9685, 4429, 2891, 4875, 6629, 4995, 4860, 5677, 6245, 3514, 2431, 7414, 1708, 7374, 6176, 1283, 2866, 5037, 3049, 5568, 3545, 8440, 9962, 4124, 4893, 7132, 50, 2350, 4700, 4307, 1898, 689, 6461, 6800, 4214, 2874, 4304, 5537, 4113, 4790, 7898, 9421, 6985, 2994, 2437, 26, 6301, 9935, 3713, 4416, 5338, 1570, 8303, 4782, 7369, 1420, 2114, 864, 1585, 5972, 287, 3848, 6280, 9750, 6505, 9730, 9057, 8959, 6064, 2492, 5517, 8582, 2062, 912, 1502, 4125, 9123, 7022, 260, 5353, 983, 3505, 3809, 9316, 3547, 7313, 8794, 362, 7250, 773, 3199, 3704, 2496, 467, 511, 2509, 7512, 9128, 1864, 8445, 1647, 8655, 7588, 888, 8260, 6384, 7028, 2101, 356, 6142, 6456, 9643, 9170, 8235, 8792, 8732, 730, 2609, 9574, 3036, 9135, 8873, 5976, 7192, 9249, 7795, 320, 8158, 4437, 395, 8766, 4472, 6427, 9628, 9187, 3707, 2770, 3914, 1148, 5958, 5168, 7682, 5276, 8455, 796, 4653, 996, 168, 646, 5220, 3461, 6671, 8173, 2024, 7492, 5338, 8381, 6315, 9979, 8127, 5034, 6503, 7708, 3533, 3661, 6398, 1438, 7587, 5936, 4420, 1795, 6146, 4758, 2201, 9959, 4752, 9924, 3160, 3772, 4282, 6882, 4993, 8298, 7970, 522, 7361, 4071, 4451, 3342, 2624, 9911, 3617, 942, 7751, 4153, 5305, 8744, 7717, 7086, 582, 1175, 8978, 5193, 5012, 2213, 2261, 2282, 6552, 4329, 7957, 4146, 4922, 2990, 3695, 6046, 5310, 6030, 8098, 1348, 3005, 6489, 3802, 8495, 4014, 2701, 1864, 3756, 4821, 2198, 7954, 4253, 4496, 2956, 1238, 3447, 383, 9514, 9154, 2241, 9673, 1354, 9814, 4849, 7714, 7066, 4328, 1171, 4373, 8438, 1184, 4142, 4790, 1650, 2574, 5742, 3108, 9020, 3808, 193, 5654, 913, 277, 5796, 1997, 1356, 3353, 8247, 1137, 4491, 7203, 7133, 6509, 7819, 5652, 1985, 1399, 1446, 8980, 6949, 2676, 4778, 7834, 6300, 7688, 6422, 1969, 3863, 8890, 4874, 2524, 7361, 7349, 7504, 7054, 8270, 8745, 6817, 8243, 6352, 7718, 8035, 5882, 1986, 1799, 1463, 779, 4297, 9511, 9792, 5212, 3574, 4549, 6155, 1882, 7770, 4975, 5140, 3929, 8359, 1453, 9219, 5855, 8220, 7937, 2062, 2613, 9878, 1778, 1982, 7507, 7521, 2059, 8945, 9449, 6497, 335, 5845, 1230, 8378, 746, 867, 954, 7064, 3472, 6725, 8013, 7106, 5060, 2380, 2155, 8059, 5875, 1832, 9143, 3599, 8568, 1351, 6619, 825, 2256, 8761, 8456, 9241, 7450, 6217, 7257, 1512, 9925, 2997, 8956, 8382, 6320, 6760, 8921, 9850, 9446, 6581, 26, 2741, 4883, 4711, 145, 3985, 9461, 5701, 5876, 2682, 6901, 1573, 8008, 1963, 8230, 6581, 7575, 3846, 4363, 8284, 9939, 1283, 5533, 9358, 2644, 1973, 397, 1373, 6415, 8017, 156, 6992, 7183, 375, 2159, 4891, 7417, 5299, 5087, 9568, 4677, 4312, 9362, 6694, 4970, 5819, 3969, 6550]"""

print("\n\n Heapsort")
start = timeit.default_timer()

def swap(i, j):                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 

def heapify(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and sqc[i] < sqc[l]:   
        max = l   
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heap_sort():     
    end = len(sqc)   
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)   

sqc = myList
heap_sort()

stop = timeit.default_timer()

print("Tempo de execução: ")
print (stop - start)






print("\n QUICK SORT ")


start = timeit.default_timer()
# quick sort
def partition(myList, start, end):
    #pivot = myList[start]
    pivot = myList[start]
    left = start+1
    # Start outside the area to be partitioned
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def quicksort(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList



def main(myList):
    sortedList = quicksort(myList,0,len(myList)-1)
    

main(myList)
stop = timeit.default_timer()

print("Tempo de execução: ")
print (stop - start)





#Desenvolvido por White Hawk
#Licenciado sob a GPL(GNU Public License)
def bubbleSort(A):
    if len(A) <= 1:
        sA = A
    else:
        for j in range(0,len(A)):
            for i in range(0,len(A)-1):
                if A[i]>A[i+1]:
                    Aux = A[i+1]
                    A[i+1] = A[i]
                    A[i] = Aux
        sA = A

    return sA


bubbleSort(myList)
stop = timeit.default_timer()

print("\n BubbleSort")
print("Tempo de execução: ")
print (stop - start)