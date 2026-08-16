import outcome_probability
import slm_training
import random

print("KORNELIOUS (ChatBot)\n")
bigram_probability = outcome_probability.bigram_probability
text = input("Input training text:\n") 
text = slm_training.text_adjustment(text)                             
slm_training.bigram_probability_training(text)

#Generation of text, based randomly on the Bigram Probability
current_word = " "
while current_word == " ":
    current_word = text[random.randint(0, len(text) - 1)]
next_word = ""
new_message = [current_word]
while not current_word == " ":
    next_word = bigram_probability[current_word]
    random_int = random.randint(0, len(next_word) - 1)
    next_word = next_word[random_int]
    new_message.append(next_word.strip(","))
    current_word = next_word

#The first letter of a sentence is always capitalized
first_word = list(new_message[0])
first_word[0] = first_word[0].upper()
first_word = "".join(first_word)
new_message[0] = first_word

#There's always a dot at the end
new_message[-2] += "."

print(f"\nChatBot response:\n{" ".join(new_message).strip(" ")}")
