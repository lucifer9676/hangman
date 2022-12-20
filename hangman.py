from random import choice
from words import words


def get_valid_word(words):
    word = choice(words)
    while "-" in word or " " in word:
        word = choice(words)
    return word.lower()

answer = list(get_valid_word(words))
ans = "".join(answer)
print("we are going to play a hangman.You have 7 lives.\nEvery time you guess a wrong letter you lose a live.\n Best of Luck! :)")
temp = ["_" for char in answer]
used_char = []

 
def hangman():
    chances = 7
    while chances:
        print(" ".join(temp))  # displaying
        guess = input("Enter a letter:")
        
        for char in used_char:
            if guess == char:
                print("you have already used this letter")
                chances+=1
                continue
        used_char.append(guess)

        if len(guess) != 1:#checking for invalid input
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
        i = len(answer) - 1
        while i>=0:
            if answer[i]==guess:
                break
            elif answer[i]!= guess and i==0:
                chances -= 1
            i=i-1
        
        if temp == answer:
            print(f"the word is '{ans}'.\nYou guessed it right.you win.")
            break
        if not chances:
            print(f"0 lives left.\n You lose.\n the word was '{ans}'")
        else:
            print(f"You have {chances} lives left")


if __name__ == "__main__":
    hangman()
