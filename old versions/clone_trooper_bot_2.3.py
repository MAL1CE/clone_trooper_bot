# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 00:13:32 2021

@author: MAD_MAL1CE
"""

import praw
import random
import time

clone_triggers = ["clone",
                  "clones",
                  "trooper",
                  "good soldiers follow orders"]
                
droid_triggers = ["clanker",
                  "clanka",
                  "battledroid",
                  "battle droid",
                  "droideka",
                  "b1"]

skirata_triggers = ["skirata"]

sentient_triggers = ["sentient",
                     "s e n t i e n t"]

greivous_triggers = ["💀"]

greivous_quotes = ["'It's Grιevous, hit him from all sides!'"]

maul_triggers = ["maul"]

order_66_triggers = ["order 66",
                     "order sixty six",
                     "order sixty-six"]

stormtrooper_filter = ["storm trooper",
                       "stormtrooper",
                       "death trooper",
                       "deathtrooper",
                       "scout trooper",
                       "bark trooper"]

salute_triggers = ["salute",
                   "attention",
                   "good job", 
                   "well done", 
                   "very good",
                   "excellent work"]

#The time in seconds between posts
cooldown = 60

# Put your bot's reddit id here. It will be used in several funtions.
bot_id = "dzuogrxz"

# Connecting your bot to your personal script app and logging in
reddit = praw.Reddit('CloneTrooperBot')

# Begins the comment stream, scans for new comments
for comment in reddit.subreddit('PrequelMemes').stream.comments(skip_existing=True):
    
    author_name = str(comment.author.name) # Fetch author name
    author_id = str(comment.author.id) # Fetch author id
    comment_lower = comment.body.lower() # Fetch comment body and convert to lowercase
    
    with open('ignore_list.txt', 'r')as rf: # Opens ignore_list in read only mode
    
        rf_contents = rf.read() # Reads the contents of ignore list
        
        if author_id not in rf_contents and author_id != bot_id: #Checks comment against ignore list and bot id
            
            with open('gray_list.txt', 'r')as gl:
                
                gray_list = gl.read() # Reads the contents of ignore list
                
                if author_name in gray_list:
                    
                    is_graylisted = "yes"
                    
                else:
                    
                    is_graylisted = "no"
                
            if "!ignore" in comment_lower and len(comment_lower) < 8: # Looks for the word "ignore" in the comment and checks length of comment to prevent misfire.
                
                print("Checking for bot_id")
                
                if comment.parent().author.id == bot_id: # Checks if comment is a reply to your bot
        
                    with open('ignore_list.txt', 'a') as f: # Opens ignore list in append mode
                        
                        print("##### NEW COMMENT #####")
                        print(comment.author)
                        print(comment.author.id)    
                        print(comment.body.lower())
                        print("           ")
                        
                        # Writes Username and ID of user to the ignore list
                        f.write(author_name)
                        f.write("\n")
                        f.write(author_id)
                        f.write("\n")
                        f.write("\n")
                        
                        print(" ")
                        print("User Added to Ignore List")
                        print(" ")
                        
                        # Replies to user comment
                        comment.reply("User Added to Ignore List.")
                        
                else: # if ignore is not in response to your bot, prints a false alarm message and does not add name to ignore list
                    
                    print("##### NEW COMMENT #####")
                    print(comment.author)
                    print(comment.author.id)    
                    print(comment.body.lower())
                    print("           ")
                    
                    print("           ")
                    print("&&&& False Alarm &&&&")
                    print("           ")
                    
                
            else: # If 'ignore' not present in comment body, prceeds to checking for keywords and other bot functions
                
                print("\n\n\n", "##### NEW COMMENT #####", "\n", "Submission Title: ", comment.submission.title)
                print("Author: ", comment.author)
                print("Is Graylisted: ", is_graylisted)
                print("Author ID: ", comment.author.id, "\n")
                print(comment.body.lower(), "\n\n\n\n")
                
                
                if is_graylisted == "yes":
                
                    roll_die = random.randint(1, 2)
                    print("Dice Roll: ", roll_die)
                    roll_die_string = str(roll_die)
                    if roll_die_string == "1":
                        
                        is_graylisted = "no"
                        
                if is_graylisted == "no":
                    
                    # with open('rude_words.txt', 'r') as rw:
                        
                    #     rude_words = list(rw.read())
                    
                    with open('rude_words.txt', 'r') as rw:
                        rude_words = rw.readlines()
                        rude_words = [line.rstrip() for line in rude_words]
                
                        if any(word in comment_lower for word in order_66_triggers): #Checks for keywords in comment
                
                            with open('order_66_responses.txt', 'r', encoding='utf-8') as tf:
                                                     
                                quote_selection = tf.read().splitlines()
                            
                                print("===== Generating Reply =====", "\n")
                                generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                comment.reply(generated_reply) # Replies to comment with random quote
                                print(generated_reply, "\n") # Prints random quote from reply
                                print("===== Reply Posted ======", "\n\n\n")
                                time.sleep(cooldown) # Cooldown in seconds

                        elif any(word in comment_lower for word in skirata_triggers): #Checks for keywords in comment
                
                            with open('skirata_responses.txt', 'r', encoding='utf-8') as tf:
                                
                                quote_selection = tf.read().splitlines()
                        
                                print("===== Generating Reply =====", "\n")
                                generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                comment.reply(generated_reply) # Replies to comment with random quote
                                print(generated_reply, "\n") # Prints random quote from reply
                                print("===== Reply Posted ======", "\n")
                                time.sleep(cooldown) # Cooldown in seconds   
                                
                        elif any(word in comment_lower for word in sentient_triggers): # Looks for the word "ignore" in the comment and checks length of comment to prevent misfire.
                        
                            if comment.parent().author.id == bot_id: # Checks if comment is a reply to your bot
                                
                                with open('sentient_responses.txt', 'r', encoding='utf-8') as tf:
                                    
                                    quote_selection = tf.read().splitlines()
                            
                                    print("===== Generating Reply =====", "\n")
                                    generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                    generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                    comment.reply(generated_reply) # Replies to comment with random quote
                                    print(generated_reply, "\n") # Prints random quote from reply
                                    print("===== Reply Posted ======", "\n")
                                    time.sleep(cooldown) # Cooldown in seconds  
                                    
                            else:
                                
                                print(" ")
                                print("%%%%%% Not Sentient, I guess %%%%%%")
                                print(" ")
                                

                        elif any(word in comment_lower for word in rude_words):
                            
                            if comment.parent().author.id == bot_id:
                        
                                with open('rude_responses.txt', 'r', encoding='utf-8') as tf:
                                                         
                                    quote_selection = tf.read().splitlines()
                                
                                    print("!!!!! Rudeness Detected !!!!!", "\n")
                                    print("===== Generating Reply =====", "\n")
                                    generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                    generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                    comment.reply(generated_reply) # Replies to comment with random quote
                                    print(generated_reply, "\n") # Prints random quote from reply
                                    print("===== Reply Posted ======", "\n\n\n")
                                    time.sleep(cooldown) # Cooldown in seconds
                                
                        elif any(word in comment_lower for word in salute_triggers):
                            
                            if comment.parent().author.id == bot_id:
                            
                                with open('salute_responses.txt', 'r', encoding='utf-8') as tf:
                                
                                    quote_selection = tf.read().splitlines()
                                
                                    print("!!!!! Attention, Salute !!!!!", "\n")
                                    print("===== Generating Reply =====", "\n")
                                    generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                    generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                    comment.reply(generated_reply) # Replies to comment with random quote
                                    print(generated_reply, "\n") # Prints random quote from reply
                                    print("===== Reply Posted ======", "\n\n\n")
                                    time.sleep(cooldown) # Cooldown in seconds
                                
                        # elif any(word in comment_lower for word in rude_words):
                            
                        #     if "rex" in comment.parent().author.name:
                        
                        #         print("===== Generating Reply =====", "\n")
                        #         comment.reply('"You cant talk to Captain Rex like that!" -Jesse') # Replies to comment with random quote
                        #         print('"You cant talk to Captain Rex like that!" -Jesse', "\n") # Prints random quote from reply
                        #         print("===== Reply Posted ======", "\n\n\n")
                        #         time.sleep(cooldown) # Cooldown in seconds
                            
                        elif any(word in comment_lower for word in droid_triggers): #Checks for keywords in comment
                
                            with open('droid_responses.txt', 'r', encoding='utf-8') as tf:
                                    
                                quote_selection = tf.read().splitlines()
                        
                                print("===== Generating Reply =====", "\n")
                                generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                comment.reply(generated_reply) # Replies to comment with random quote
                                print(generated_reply, "\n") # Prints random quote from reply
                                print("===== Reply Posted ======", "\n")
                                time.sleep(cooldown) # Cooldown in seconds  
                            
                        elif any(word in comment_lower for word in maul_triggers): #Checks for keywords in comment
                
                            roll_die = random.randint(1, 3)
                            print("Dice Roll: ", roll_die)
                            roll_die_string = str(roll_die)
                            if roll_die_string == "1":            
                
                                with open('maul_responses.txt', 'r', encoding='utf-8') as tf:
                                        
                                    quote_selection = tf.read().splitlines()
                            
                                    print("===== Generating Reply =====", "\n")
                                    generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                    generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                    comment.reply(generated_reply) # Replies to comment with random quote
                                    print(generated_reply, "\n") # Prints random quote from reply
                                    print("===== Reply Posted ======", "\n")
                                    time.sleep(cooldown) # Cooldown in seconds   
                            
                        elif any(word in comment_lower for word in greivous_triggers): #Checks for keywords in comment
                
                            print("===== Generating Reply =====", "\n")
                            generated_reply = random.choice(greivous_quotes) # Fetch random quote from list
                            comment.reply(generated_reply) # Replies to comment with random quote
                            print(generated_reply, "\n") # Prints random quote from reply
                            print("===== Reply Posted ======", "\n")
                            time.sleep(cooldown) # Cooldown in seconds
                        
                        elif any(word in comment_lower for word in clone_triggers): #Checks for keywords in comment
    
                            # if any(word in comment_lower for word in stormtrooper_filter):
                                
                            #     print("\n", "XXXX Post Regarding Stormtroopers XXXX", "\n")
                                
                            # elif any(word not in comment_lower for word in stormtrooper_filter):

                                with open('clone_responses.txt', 'r', encoding='utf-8') as tf:
                                        
                                    quote_selection = tf.read().splitlines()
                            
                                    print("===== Generating Reply =====", "\n")
                                    generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                    generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                    comment.reply(generated_reply) # Replies to comment with random quote
                                    print(generated_reply, "\n") # Prints random quote from reply
                                    print("===== Reply Posted ======", "\n")
                                    time.sleep(cooldown) # Cooldown in seconds     
                            
                        elif "gonk" in comment_lower:
                            
                            roll_die = random.randint(1, 50)
                            print("Dice Roll: ", roll_die)
                            roll_die_string = str(roll_die)
                            if roll_die_string == "1":
                                
                                with open('gonk_responses.txt', 'r', encoding='utf-8') as tf:
                                    
                                    quote_selection = tf.read().splitlines()
                            
                                    print("===== Generating Reply =====", "\n")
                                    generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                                    generated_reply = generated_reply_unadjusted.replace("username", author_name)
                                    comment.reply(generated_reply) # Replies to comment with random quote
                                    print(generated_reply, "\n") # Prints random quote from reply
                                    print("===== Reply Posted ======", "\n")
                                    time.sleep(cooldown) # Cooldown in seconds   
                          
                            else:
    
                                print("\n", "Roll failed, ignoring comment", "\n\n\n\n")
                                
                else:
                    
                    print("\n", "Roll failed, ignoring comment")
                    print("!!!!!!!! User Graylisted !!!!!!!!", "\n\n\n\n")
                        
        else: # If user on ignore list, prints User Ignored, and does not reply to comment
            
            print("\n", "##### NEW COMMENT #####", "\n")
            print(comment.author)
            print(comment.author.id)    
            print(comment.body.lower(), "\n")
            
            print("!!!!!!!! User Ignored !!!!!!!!", "\n\n\n\n")
            
    