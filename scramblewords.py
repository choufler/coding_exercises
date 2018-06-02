import time

def getSortedString(s):
    return ''.join(sorted(s))

def getSortedDict(dict):
    sortedDict = {}
    for w in dict:
        sortedDict.update( {getSortedString(w) : w})
    return sortedDict

def unscrumble(dict, phrase):
    sortedDict = getSortedDict(dict)
    result = unscrumble_rec(sortedDict, phrase, 0, [])
    
    if not result:
        return "<could not unscrumble>"
    
    unscrumbledphrase = ""
    for w in result:
        unscrumbledphrase+= sortedDict[getSortedString(w)] + " "
        
    return unscrumbledphrase[:len(unscrumbledphrase )-1]

def unscrumble_rec(dict, phrase, curIdx, words):
    lastWordIdx = len(words) - 1
    
    if curIdx >= len(phrase):
        #all the other words has been checked already, we need to check only the last one
        if getSortedString(words[lastWordIdx]) in dict:
            return words
        return
    
    #check if there is a current word in the dict, otherwise return as we know this branch is dead
    if lastWordIdx<=0 or getSortedString(words[lastWordIdx]) in dict:
        newwords = list(words)
        newwords.append(phrase[curIdx:curIdx+1])
        result = unscrumble_rec(dict, phrase, curIdx + 1, newwords)
        if result:
            return result
    
    if lastWordIdx>= 0:
        last = len(words) - 1
        words[lastWordIdx]+= phrase[curIdx]
        return unscrumble_rec(dict, phrase, curIdx +1, words)

if __name__ == "__main__":
    dict = {"hell","hello", "world","from","h","he","ow","row"}
    phrase = "llehoworldformhell"
    start_time = time.time()
    print (unscrumble(dict, phrase))
    print("--- %s seconds ---" % (time.time() - start_time))
