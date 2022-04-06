Welcome to Leword!! My custom wordle solving bot, 
along with a playable version of wordle that works more than once a day.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Leword has a very limited vocabulary, they understand things like:

next (go to next guess)

ins [guess colors] (insert results of guess)

contains [word] (see if Leword still has this word in their word list)

validate [word] (see for yourself if a word is valid in Lewords eyes)

stop (for when you're done)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

to run:

extract all .py & .txt files to the same folder.
run leword.py
(optional) run wordle.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How does Leword decide which words to guess?

Leword uses letter frequency to determine the best word to guess, with a preference for words with more unique chars.
There is a hashmap of {char : Letter objects} and {word_as_string : Word objects}. The Letter object holds its total frequency,
its frequency in each position, and its state in each positions (states are white, gray, yellow, green).
The word objects only hold the string word and their score. 

Leword will take the user input and update the letter states. Then it validates the word list by going through each letter in each word,
and checking if any of the letters are gray, or yellow in that position of the word. If either of those are true, the word is not a possible
guess and is removed. Then once the word list is shortened it will apply the word score, which is the sum of the frequencies of the letters in those positions,
multiplied by 1 + (0.1 * number of unique chars)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

to update Leword example:

ins gyngy

means first letter is green, second is yellow, third is gray, fourth is green, fifth is yellow.

when you guess a word in the wordle game it will give you this string to copy paste into Leword

have fun (: and play around with the calc_word_score function, see if you can make it better



