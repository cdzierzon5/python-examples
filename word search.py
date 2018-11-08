#cody dzierzon
#11/8/18

attempts = 0

print("PYTHON TERMS")
puzzle = ("fjvfloatdyyopxedninsmspfycnnalxeaeeukgeislufryprlcabeeiagco"+
          "ibuclqttbongojlivxobgadmyahgerjstringwvrs")
def display_puzzle():
    print(puzzle[0:10])
    print(puzzle[10:20])
    print(puzzle[20:30])
    print(puzzle[30:40])
    print(puzzle[40:50])
    print(puzzle[50:60])
    print(puzzle[60:70])
    print(puzzle[70:80])
    print(puzzle[80:90])
    print(puzzle[90:])
    print()

print()

#display the puzzle
display_puzzle()


print("WORD LIST")
word_list = "float, while, if, boolean, double, operators, string, slicing, index"
print(word_list)
print()

#getting the lengths of the words
word1_length=len("float")
word2_length=len("while")
word3_length=len("if")
word4_length=len("boolean")
word5_length=len("double")
word6_length=len("operators")
word7_length=len("string")
word8_length=len("slicing")
word9_length=len("index")

#getting player answer
x=0
while x==0:
    word1=input("Enter the index positions of float: ")
    attempts+=1
    i=0
    foundword=""
    while i < word1_length:
        index=word1[i]
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=1
    if foundword == "float":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")

x=0
while x==0:
    word1=input("Enter the index positions of while: ")
    attempts+=1
    i=0
    foundword=""
    while i < word2_length*2:
        index=word1[i:i+2]
        print(i)
        print(index)
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=2
    if foundword == "while":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")

x=0
while x==0:
    word1=input("Enter the index positions of if: ")
    attempts+=1
    i=0
    foundword=""
    while i < word3_length*2:
        index=word1[i:i+2]
        print(i)
        print(index)
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=2
    if foundword == "if":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")

x=0
while x==0:
    word1=input("Enter the index positions of boolean: ")
    attempts+=1
    i=0
    foundword=""
    while i < word4_length*2:
        index=word1[i:i+2]
        print(i)
        print(index)
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=2
    if foundword == "boolean":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")

x=0
while x==0:
    word1=input("Enter the index positions of double: ")
    attempts+=1
    i=0
    foundword=""
    while i < word5_length*2:
        index=word1[i:i+2]
        print(i)
        print(index)
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=2
    if foundword == "double":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")

x=0
while x==0:
    word1=input("Enter the index positions of operators: ")
    attempts+=1
    i=0
    foundword=""
    while i < word6_length*2:
        index=word1[i:i+2]
        print(i)
        print(index)
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=2
    if foundword == "operators":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")

x=0
while x==0:
    word1=input("Enter the index positions of string: ")
    attempts+=1
    i=0
    foundword=""
    while i < word7_length*2:
        index=word1[i:i+2]
        print(i)
        print(index)
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=2
    if foundword == "string":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")

x=0
while x==0:
    word1=input("Enter the index positions of slicing: ")
    attempts+=1
    i=0
    foundword=""
    while i < word8_length*2:
        index=word1[i:i+2]
        print(i)
        print(index)
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=2
    if foundword == "slicing":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")

x=0
while x==0:
    word1=input("Enter the index positions of index: ")
    attempts+=1
    i=0
    foundword=""
    while i < word9_length*2:
        index=word1[i:i+2]
        print(i)
        print(index)
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=2
    if foundword == "index":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that's not right try again")


