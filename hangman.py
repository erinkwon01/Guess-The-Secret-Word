import random

# A list of words that
potential_words = ["blueberries", "parrot", "clown", "bumblebee", "Disneyland"]

word = random.choice(potential_words)

print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
list  = ["_"]*len(word) # TIP: the number of letters should match the word
print(list)

# Some useful variables
guesses = []
maxfails = 6
fails = 0

while fails < maxfails:
	guess = input("Guess a letter from the alphabet: ")

for
	if guess in word:
		print(list)
		singleletter = word.index(guess)
		word[singleletter:singleletter]
		print(guess)
	else:
		fails = fails+1
		print("You have " + str(maxfails - fails) + " tries left!")
	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
