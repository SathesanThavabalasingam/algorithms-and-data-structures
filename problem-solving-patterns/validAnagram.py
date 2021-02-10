def validAnagram(a, b):
    
    # define edge case
    if len(a) != len(b):
        return False
    
    # define lookup    
    lookup = {}
    
    # loop over a and place its values and freqs in lookup object
    for item in a:
        if item in lookup:
            lookup[item] +=1
        else:
            lookup[item] = 1
    # loop over b and perform lookup check
    for item in b:
        # if frequencey of char doesn't exist or 0 will return false
        if not lookup[item]:
            return False
        # we decrease the freq as it represents how many times we've
        # seen this letter
        else:
            lookup[item] -= 1
    # return true if all else cases fail        
    return True

validAnagram('anagram','nagaram')