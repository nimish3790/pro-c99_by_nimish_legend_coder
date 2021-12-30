def countWordsFromFile():
    fileName=input("ENTER THE FILE NAME :-")
    numberofWords=0

    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberofWords=numberofWords+len(words)
    print("number of words :-")
    print(numberofWords)
countWordsFromFile()
