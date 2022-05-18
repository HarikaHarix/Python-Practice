text="    Harry is good     "
print(text)
print(text.strip())

#remove a given word from a string and strip it at the same time
def remove_and_split(string,word):
    newString=string.replace(word,"")
    return newString.strip()

statement="    Let's remove nothing   "
print(remove_and_split(statement,"nothing"))