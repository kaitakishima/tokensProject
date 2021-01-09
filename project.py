"""
Function that tokenizes a sentence based off of if it's an alphanumeric word or not

@param sentence: a string holding words creating a sentence
@return tokens: the alphanumeric tokens (strings) in an array
"""
def tokenizeMySentence(sentence):

    # splits up the variable words into an array
    words = sentence.split()
    tokens = []

    for i in range(len(words)):
        # saying that if words[i] is alphanumeric, then add words[i] to 
        # the empty array
        if(words[i].isalnum()):
            tokens.append(words[i])

    # returning variable tokens
    return tokens

"""
Function that accepts a list of tokens and writes it to a .txt file line by line

@param tokensList: an array holding alphanumeric words (strings)
@return None
"""
def writeListToFile(tokensList):
    # opens a txt file to write to
    f = open("output.txt", "a+")

    
    # for every token in tokensList, append a token to the file
    for token in tokensList:
        f.write(token + "\n")
    f.close()

def main():
    f = open("output.txt", "w+")
    f.seek(0)
    f.truncate()
    f.close()
    userInput = ""
    while userInput != "-1":
        # a = "Apples to pears 12321 @#@! 123"
        userInput = input("Type in a sentence: ")
        
        # passing variable a into tokenizeMySentence
        tokensList = tokenizeMySentence(userInput)
        
        writeListToFile(tokensList)
        
        # printing the value returned from tokenizeMySentence
        print(tokensList)

if __name__ == "__main__":
    main()