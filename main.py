'''You have write a function that accepts, a string which length is βlenβ,
the string has some β#β, in it you have to move all the hashes to the front of the string and return the whole string back and print it.'''
s='Move#Hash#to#Front'
len=len(s)
def MoveHash(s,len):
    l = []
    a = ''
    for i in s:
        if i == "#":
            l.append(i)
    for j in s:
        if j != "#":
            l.append(j)
    for c in l:
        a += c
    return a
print(MoveHash(s,len))