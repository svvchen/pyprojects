# header

import sys
import pronouncing
import numpy as np
from sty import fg, bg, ef, rs, Style, RgbFg
import re

# I: poem txt file.
# O: poem but with highlights.

def highlight_rhyming_words(poem_file):

    with open(poem_file, 'r') as file:
        data = file.read()
    input = re.sub(r'[^\w\s]','',data)
    input_list = re.findall(r'(\S+)\s*$(?!/)', input, re.MULTILINE)

    # initializing our sound dict
    sound_dict = {}
    already_rhymed = []
    for i in input_list:
        sound_dict[i] = []
    
    # rhyming
    for i in input_list:
        for n in input_list:
            if n != i:
                if n in pronouncing.rhymes(i) and n not in already_rhymed:
                    sound_dict[i].append(n)
                    already_rhymed.append(n)
                    already_rhymed.append(i)

    # remove the non-rhymers
    for x in list(sound_dict.keys()):
        if sound_dict[x] == []:
            del sound_dict[x]

    # add the word itself to the values
    for k in sound_dict:
        sound_dict[k].append(k)

    # print out the final results
    # print(sound_dict)

    # optionally, and maybe more usefully, print out all rhyming values in a list
    rhyming_words = list(sound_dict.values())

    # print("original poem:\n\n" + data)

    for rhyme_scheme in rhyming_words:

        #generate a color for the current scheme
        r_rand = np.random.choice(range(256))
        g_rand = np.random.choice(range(256))
        b_rand = np.random.choice(range(256))
        fg.color = Style(RgbFg(r_rand, g_rand, b_rand))

        for word in rhyme_scheme:

            # in here, we'd like to find and replace each word in the text file with it's associated fg.color word
            colored_word = fg.color + ef.bold + word + fg.rs + rs.bold_dim
            data = data.replace(word, colored_word)

    print(data)


highlight_rhyming_words('poem.txt')
