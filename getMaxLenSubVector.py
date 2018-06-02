def getMaxAreaSubVector(vector, S):
    WindowMaxLen = 0
    windowSum = 0
    WindowStart = 0
    currentRangeStart = 0
    for i in range (0, len(vector)):
        windowSum += vector[i]
        if windowSum <= S:            
            WindowMaxLen +=1
            WindowStart = currentRangeStart
        else:
            windowSum-= vector[currentRangeStart]
            currentRangeStart+=1
    return vector[WindowStart:WindowStart + WindowMaxLen]
            

res = getMaxAreaSubVector([1,2,7,100,4,8,3,1,1,1,1,1,2,3,4,5,6], 5)
print(res)
