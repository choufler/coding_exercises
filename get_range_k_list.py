# you have k lists of sorted integers. 
# Find the smallest range that includes at least one number from each of the k lists.

#For example,
#List 1: [4, 10, 15, 24, 26]
#List 2: [0, 9, 12, 20]
#List 3: [5, 18, 22, 30]

#The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.
import operator

# can be impproved using heaps
def get_next_to_iterate(idx, end, buf):
    minIdx = -1
    min = 0
    for i in range (len(idx)):
        if (idx[i] != end[i]):
            if (minIdx == -1 or min > buf[i]) :
                minIdx = i
                min = buf[i]
    return minIdx

def get_len(buf):
    min_value = min(buf)
    max_value = max(buf)
    return max_value-min_value, [min_value, max_value]
def get_smallest_range(lists):
    idx = [], #aray of current indices
    end = []
    buf = []
    for list in lists:
        idx.append(0)
        end.append(len(list) -1 )
        buf.append(list[0])

    min_len, res  = get_len(buf)
    while idx != end:
        advIdx = get_next_to_iterate(idx, end, buf)        
        idx[advIdx]+=1
        buf[advIdx] = lists[advIdx][idx[advIdx]]
        len_idx, cur  = get_len(buf)
        if (len_idx < min_len):
            min_len = len_idx
            res = cur            

    return res

test1 = [ [4, 10, 15, 24, 26],  [0, 9, 12, 20] ,[5, 18, 22, 30] ]
testsimple = [ [3,5,6], [2,3], [0,1]]



print (get_smallest_range(testsimple))
print (get_smallest_range(test1))
