from random import choice
from words import words


def get_valid_word(words):
    word = choice(words)
    while "-" in word or " " in word:
        word = choice(words)
    return word.lower()

print("we are going to play a hangman. Best of Luck! :)")
answer = list(get_valid_word(words))

temp = ["_" for char in answer]
used_char = []

    
def hangman():
    chances = 15
    while chances:
        print(" ".join(temp))  # displaying
        guess = input("Enter a letter:")
        
        for char in used_char:
            if guess == char:
                print("you have already used this letter")
                chances+=1
                continue
        used_char.append(guess)

        if len(guess) != 1 or not len(guess):
            print("Please enter one letter at a time.")
            continue
        # checking for matching letters
        for char in answer:
            # if the answer has 1 match
            if char == guess:
                index = answer.index(char)
                temp.pop(index)
                temp.insert(index, char)
                num = answer.count(char)
                # if the answer has more than 1 match
                if num > 1:
                    for i in range(num-1):
                        sliced_answer = answer[index+1:]
                        new_index = sliced_answer.index(char)+index + 1
                        temp.pop(new_index)
                        temp.insert(new_index, char)
                        index = new_index
        chances -= 1

        ans = "".join(answer)
        if temp == answer:
            print(f"the word is '{ans}'.\nYou guessed it right.you win.")
            break
        if not chances:
            print(f"0 guesses left.\n You lose.\n the word was '{ans}'")

        print(f"You have {chances} guesses left")


if __name__ == "__main__":
    hangman()
