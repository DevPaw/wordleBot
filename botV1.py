guessed = False

grayLetters = []
yellowLetters = []
greenLetters = []

with open ('wordle-allowed-guesses.txt', 'r') as f:
    supersetWords = f.read().splitlines()

plausibleWords = supersetWords.copy()

while guessed == False:

    currWord = input("What word did u enter?: ")

    #map function to make elements of list into integer just by writing int
    currGrayPlaces = list(map(int, input("Grays: ").split()))
    currYellowPlaces = list(map(int, input("Yellows: ").split()))
    currGreenPlaces = list(map(int, input("Green: ").split()))

    if len(currGreenPlaces) == 5:
        guessed == True
    else: 
        for i in currGrayPlaces:
            grayLetters.append(currWord[i])

        for i in currYellowPlaces:
            yellowLetters.append(currWord[i])

        for i in currGreenPlaces:
            greenLetters.append(currWord[i])

        if currGrayPlaces:
            for grayLetter in grayLetters:
                for word in plausibleWords.copy():
                    if grayLetter in word:
                        plausibleWords.remove(word)

        if currYellowPlaces:
            for yellowLetter in yellowLetters:
                for word in plausibleWords.copy():
                    if yellowLetter not in word:
                        plausibleWords.remove(word)
                    if yellowLetter in word:
                        if word[currWord.index(yellowLetter)] == yellowLetter:
                            plausibleWords.remove(word)
                    
    
        if currGreenPlaces:
            for greenLetter in greenLetters:
                for word in plausibleWords.copy():
                    if greenLetter in word: 
                        if word[currWord.index(greenLetter)] != greenLetter:
                            plausibleWords.remove(word)
                    else:
                        plausibleWords.remove(word)

        currGrayPlaces = []
        currYellowPlaces = []
        currGreenPlaces = []

        yellowLetters = []

        print(plausibleWords, "\n You have ", len(plausibleWords), " more options left")