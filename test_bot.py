# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:44:03 2021

@author: Asher
"""

import praw
import random

with open('maul_responses.txt', 'r', encoding='utf-8') as tf:
                                
    quote_selection = tf.read().splitlines()

    print("===== Generating Reply =====")
    generated_reply = random.choice(quote_selection) # Fetch random quote from list
    
    print("  ")
    print(generated_reply) # Prints random quote from reply
    print("  ")
    print("===== Reply Posted ======")
    print("  ")