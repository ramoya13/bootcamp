print("====PRINCIPLE STORY====")

def nounWord():
    print("enter nouns")
    nounWords=[]

    for n in range(5):
        input1=input("{}".format(n+1))
        nounWords.append(input1)

    return nounWords


def verbword():
    print("enter verbs")
    verbwords = []

    for n in range(5):
        input1 = input("[{}".format(n + 1))
        verbwords.append(input1)

    return verbwords

def adjword():
    print("enter adjectives")
    adjwords = []

    for n in range(5):
        input1 = input("{}".format(n + 1))
        adjwords.append(input1)

    return adjwords


nounwords1 = nounWord()
verbwords1 = verbword()
adjwords1 = adjword()



principlestory="Good morning"+nounwords1[0]+".I would like to "+verbwords1[2]+"all"+adjwords1[3]+"prefects"+"for the"+adjwords1[1]+"work done.Make sure you"+verbwords1[2]+"hard to get good results.Have a"+adjwords1[4]+nounwords1[3]

print(principlestory)