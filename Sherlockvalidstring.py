#Sherlock and the Valid String
#input - a string 
#output - if you remove up to one character will the count of each character be equal yes or no
def characterCount(string):
    cCount = {}

    # count how many of each character there are
    for c in string:
        if c in cCount:
            cCount[c] = cCount[c] +1
        else:
            cCount[c] = 1

    counts = []

    for count in cCount.values():
        counts.append(count)
        print (count)


    differences = 0
    for i in range(len(counts)-1):
        # check if theres too many of a character
        if counts[i+1] - counts[i] > 1:
            return "NO"
        # make sure ther isnt more than one character to remove
        elif counts[i+1] - counts[i] != 0:
            counts[i+1] = counts[i]
            differences = differences +1
            if differences > 1:
                return "NO"
    return "YES"