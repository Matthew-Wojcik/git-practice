#alternatingCharacters
#input - a string made of 2 characters / n characters
#output - the number of characters that would have to removed to make the string alternating / non repearting character by character
def alternatingCharacters(s):
    total = 0
    seen = s[0]
    s = s[1:]
    for c in s:
        if (c == seen):
            total = total +1
        seen = c
    
    return total

def main():
    s = input()
    result = alternatingCharacters(s)
    print (result)

if __name__ == '__main__': main()

