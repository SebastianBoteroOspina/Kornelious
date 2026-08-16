import outcome_probability

def text_adjustment(text):
    """Returns a list of the words in the text, for estadistical purposes"""
    separeted_text = text.split()
    word_list = []
    for word in separeted_text:
        word = word.lower()
        word_list.append(word)
    #word_list.append(" ")
    return special_character_apreciation(word_list)

def special_character_apreciation(word_list):
    """Returns a list of all the words, with special characters removed
    or taken in mind, with assigned effects"""
    adjusted_list = []
    for word in word_list:
        adjusted_word = word.strip(" !@#$%^&*()-_=+[]{}:;.\"\'<>,/?|\\")
        adjusted_list.append(adjusted_word)
        #If there is a "." subsequent to a word, therefore that word can finish
        #a sentence. With the " " meaning the posible end of the sentence
        if list(word)[-1] in (".?!"):
            adjusted_list.append(" ")
    adjusted_list.append(" ")
    return adjusted_list

def bigram_probability_training(adjusted_text):
    """Fills out the Biagram Probability dictionary, keeping track of each word
    appearance(value) after a certain word(key)"""
    bigram_probability = outcome_probability.bigram_probability
    for i in range(len(adjusted_text)):
        word = adjusted_text[i]
        if word == " ":
            continue
        if i == len(adjusted_text) - 1:
            break
        bigram_probability[word] = bigram_probability.get(word, [])
        subsequent = adjusted_text[i + 1]
        bigram_probability[word].append(subsequent)
