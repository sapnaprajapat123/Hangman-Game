#creating a list of words
word_list =["deer","bowl","spoon","knife"]

import random
stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

choosen_letter=random.choice(word_list)

print(f"pssst, the solution is {choosen_letter}")

lives=6 
display=[]
word_length=len(choosen_letter)
for letter in range(len(choosen_letter)):
    display+="_"
print(display)

end_of_game =False
while not end_of_game:
        guess_letter=input("guess a letter: ").lower()

        for position  in range (word_length):
            letter=choosen_letter[position]
            if letter==guess_letter:
                display[position]=letter
          
        if guess_letter not in choosen_letter:
            lives-=1
            if  lives==0:
                end_of_game=True
                print("you loose")
            print(f" {' '.join(display)}" )

            if "_" not in display:
                end_of_game=True
            print("you win")  
print(stages[lives])         
        

    
