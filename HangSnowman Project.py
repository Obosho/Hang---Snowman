#outputs
snowman_art = (
"""
______
|   |  
|   __            
| _|__|_
|
|
|_____
""",
"""
____
|  |
|  __         
|_|__|_     
| ('')
|
|______
""",
"""
____
|  |
|   __          
| _|__|_     
|  ('')  
| (  . )  
|_______
""",
"""
____
|  |
|   __   
| _|__|_ 
|  ('')  
| (  . )
|(   .  )
|__________
""",
"""
____
|   |
|    __   
|  _|__|_
|   ('')   
|  (  . )---
| (   .  )
|_________
""",
"""
________
|      |
|      __   
|    _|__|_
|     ('')   
| ---(  . )---
|   (   .  )
|____________
"""

)

#stores the hidden words 
word = []
guessed_letters = []
#inputs have to be valid letters.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


Player1 = input("Who is player one? ")
Player2 = input("Who is player two? ")
print("Player 1 is " + Player1)
print("Player 2 is " + Player2)

# identify which user will guess letters (Player 2)
print(Player2 + ", look away from the screen!! ")
print("\n")

hidden_word = input(Player1 + ", what is your desired word?")
length_word = len(hidden_word)

category = input(Player1 + ", give a one-word hint of your word! ")
# provide space so that user guessing cannot see the word
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("Your hint is " + category + "! ")

#The amount of characters need to be outputted without actually 
def HiddenWord():

    for character in hidden_word: # printing blanks for each letter in secret word
        word.append("_")

    print("The word is", length_word, "characters. You can enter only 1 letter from a-z")


    print("Word: {0}".format(" ".join(word)))




def GuessLoop():
    tries_left = 0
    
    while tries_left < 6:
        guess = input(Player2 + ", guess a letter! ")
        print("\n")

        if guess not in alphabet:
            print("Enter a letter in the alphabet. Make sure it is lowercase: ")
        elif guess in guessed_letters:
            print("You already entered that letter")
        else:
            guessed_letters.append(guess)
            if guess in hidden_word:
                 print("You guessed correctly!")
                 for x in range(0, length_word): 
                    if hidden_word[x] == guess:
                        word[x] = guess
                 print("Word: {0}".format(" ".join(word)))

            if not '_' in word:
                print("Congratulations " + Player2 + " you won!")
                break
            if guess not in hidden_word:
                print(snowman_art[tries_left])
                tries_left = tries_left + 1
                print("Sorry, that letter is not in the word" )
            if tries_left == 6:
                print(Player1 + " wins! The word was " + hidden_word)

HiddenWord()
GuessLoop()


