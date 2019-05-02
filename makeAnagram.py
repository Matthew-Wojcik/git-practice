# run with -O to turn off debugging
#comment to test

#makeAnagram
#input - strings to compare
#output - total number of characters to remove for the strings to become anagrams
def makeAnagram(string1, string2):
    total = 0
    counts = {}

    for c in string1:
        if(c in counts):
            counts[c] = counts[c] + 1
        else: 
            counts[c] = 1

    for c in string2:
        if(c in counts):
            counts[c] = counts[c] - 1
        else: 
            counts[c] = -1

    for c in counts:
        total = total + abs(counts[c])

        # debugging message with what to remove
        if __debug__: 
            s = "'s "
            if abs(counts[c]) < 2:
                s = " "   
            if counts[c] > 0:
                print("Remove {0} {1}{2}from string 1".format(counts[c],c,s))
            if counts[c] < 0:
                print("Remove {0} {1}{2}from string 2".format(abs(counts[c]),c,s))

    return total

def main():
    string1 = input()
    string2 = input()
    res = makeAnagram(string1,string2)
    print(str(res) + '\n')

if __name__ == "__main__": main()
