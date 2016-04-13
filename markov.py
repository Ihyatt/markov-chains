from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #Binds variable to opened file and reads entire file as a text-string
    contents = open(file_path).read()
    #returns giant tet-string
    return contents


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    #binds list of strings to words variable
    words = text_string.split()
    #Initilaize dictionary
    chains = {}
    #Iterates over words list by index, up to and including the third from the last element
    for i in range(len(words) - 2):
        #Checks if tuple-key is within the chains dictionary
        if (words[i], words[i + 1]) in chains:
            #If key-tuple is within chains dictionary, append value so as to not over write it
            chains[(words[i], words[i + 1])].append(words[i + 2])
        else:
            #If key-tuple is not in the dictionary, add key and value-list
            chains[(words[i], words[i + 1])] = [words[i + 2]]

    return chains, words
    # print chains



def make_text(chains, words):
    """Takes dictionary of markov chains; returns random text."""
    #Initialize string
    text = ""
    #Initializing empty variable
    current_key = None

    #Starts markov chain 
    #Using a while True loop to find a capitalized word in chains dictionary
    while True:
        #Binding randomly selected key from chains dictionary
        current_key = choice(chains.keys())
        #Checks if first item from tuple is capitalized 
        if current_key[0].istitle():
            #If so, concatenates tuple to string 
            text += current_key[0] + " " + current_key[1] + " "
            #break out of while true loop once condition is met
            break
    #List of punctuations 
    punctuations = ["!","?","."]

    #Estabelish condition to terminate Markov Chain
    while current_key != tuple(words[-2:]) and len(text) <=140:
        #Prevents the formation of new key that has a none value 
        chosen_word = choice(chains[current_key])
       #Iterates through punctuations list to ensure chains ends with punctuation
        for punctuation in punctuations:
            if punctuation in chosen_word:
                #If so, break
                break

        #Middle Markov chain    )
        #Concatenates chosen_word-value to string
        text += chosen_word + " "
        #Estabelishing new variable, new_key, that is the second element of current_key and chosen_word
        new_key = (current_key[1], chosen_word)
        #Re-inds current_key to new_key 
        current_key = new_key
      
            
            
    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains, words = make_chains(input_text)


# Produce random text
random_text = make_text(chains, words)

print random_text