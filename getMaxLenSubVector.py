def getMaxAreaSubVector(vector, S):
    WindowMaxLen = 0
    WindowStart = 0

    currrentSum = 0    
    currentRangeStart = 0
    for i in range (0, len(vector)):
        currrentSum += vector[i]
        if currrentSum <= S:            
            WindowMaxLen +=1
            WindowStart = currentRangeStart
        else:
            currrentSum-= vector[currentRangeStart]
            currentRangeStart+=1
    return vector[WindowStart:WindowStart + WindowMaxLen]
            
vec = [1,2,7,100,4,8,3,1,1,1,1,1,2,3,4,5,6]
maxSum = 5
print( getMaxAreaSubVector(vec, maxSum) )

