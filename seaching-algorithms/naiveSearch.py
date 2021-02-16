def naiveSearch(long,short):
    count = 0
    for i in range(len(long)):
        for j in range(len(short)):
            if short[j] != long[i+j]:                
                break
            # after finish second loop check if we are in last
            # element of short string.
            if j == (len(short) - 1):
                count += 1 
            # add break to see if we end longer string
            if i == (len(long)-1):
                break
    return count

naiveSearch('lorielollollololokay','lol')