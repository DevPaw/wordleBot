guessed = False

grayLetters = []
yellowLetters = []
greenLetters = []


#extracting words from text file in the format of a list
with open ('wordle-allowed-guesses.txt', 'r') as f:
    supersetWords = f.read().splitlines()

#the list which will undergo iterations
plausibleWords = supersetWords.copy()


while guessed == False:

    currWord = input("What word did u enter?: ")

    #map function to make elements of list into integer just by writing int
    currGrayPlaces = list(map(int, input("Grays: ").split()))
    currYellowPlaces = list(map(int, input("Yellows: ").split()))
    currGreenPlaces = list(map(int, input("Green: ").split()))

    if len(currGreenPlaces) == 5:

        guessed = True
        print("good job :)")

    else: 

        for i in currGrayPlaces:
            grayLetters.append((currWord[i], i))    

        for i in currYellowPlaces:
            yellowLetters.append((currWord[i], i))

        for i in currGreenPlaces:
            greenLetters.append((currWord[i], i))
        #updated the method of checking by adding in positional data, this made it way easier and accurate


        for grayLetter, grayPos in grayLetters:
            for word in plausibleWords.copy():      #its important to map through a copy of list because if not, then on removing words it messes up the ongoing indexing
                if grayLetter in word:
                    if word.count(grayLetter) == 1:     #for gray letter occuring once that can be removed
                        plausibleWords.remove(word)
                    else:
                        if word[grayPos] == grayLetter:     
                            plausibleWords.remove(word)
                    #this is the case where a leter is twice, once gray once yellow, so we cant discard this word just on the basis of it having a gray, we can discard by checking specific position

        for yellowLetter, yellowPos in yellowLetters:
            for word in plausibleWords.copy():
                if yellowLetter not in word:
                    plausibleWords.remove(word)
                elif word[yellowPos] == yellowLetter:       #position based checking
                    plausibleWords.remove(word)
            
        for greenLetter, greenPos in greenLetters:
            for word in plausibleWords.copy():
                if greenLetter not in word:
                    plausibleWords.remove(word)
                elif word[greenPos] != greenLetter:
                    plausibleWords.remove(word)
                    

        #clearing the temperorary list       
        currGrayPlaces = []
        currYellowPlaces = []
        currGreenPlaces = []

        print(plausibleWords, "\n You have ", len(plausibleWords), " more options left")