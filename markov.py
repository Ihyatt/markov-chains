from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
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
  
    
    
    words = text_string.split()
    chains = {}
    for i in range(len(words) - 2):
        if (words[i], words[i + 1]) in chains:
            chains[(words[i], words[i + 1])].append(words[i + 2])
        else:
            chains[(words[i], words[i + 1])] = [words[i + 2]]

    return chains
    # print chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    current_key = choice(chains.keys())
    text += current_key[0]  + " " + current_key[1] + " "

    while True:
            if current_key == ("Sam", "I"):
                text += chains[current_key][0]
                break
                
            chosen_word = choice(chains[current_key])
            text += chosen_word + " "
            new_key = (current_key[1], chosen_word)
            current_key = new_key
            
    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text