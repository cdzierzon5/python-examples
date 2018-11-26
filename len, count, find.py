word = input("type in a word: ")
print(len(word))
pos1 = word.find("e")
pos2 = word.find("e", pos1 + 1)
substring = word[pos1:pos2}
print(substring)

print(word.count("e"))
print(word.count("e",12)

name = input("enter your first and last name: ")
x=name.find(" ")
firstName = name[:x]
lastName = name[x+1:]
print(firstName)
print(lastName)

