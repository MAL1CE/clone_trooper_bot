# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:17:42 2021

@author: MAD_MAL1CE
"""

import praw
import random
import time

roll_d6_list = ["1", "2", "3", "4", "5", "6"]
roll_d4_list = ["1", "2", "3", "4"]

clone_triggers = ["clone",
                  "clones",
                  "trooper"]

clone_quotes = ["'For The Republic!'",
                "'Nice Shooting!'",
                "'We're Gaining on em!'",
                "'Keep up the assault!'",
                "'Just Like the simulations!'",
                "'For the Chancellor!'",
                "'No one messes with the 501st!'",
                "'I used to believe that being a good soldier meant doing everything they told you. That's how they engineered us. But we're not droιds. We're not programmed. You have to learn to make your own decisions.' -Captain Rex",
                "'In My Book, Experience Outranks Everything.' -Captain Rex",
                "'We’re just clones, sir. We’re meant to be expendable.' -Sinker",
                "'You deserve it. You’re one of us.' -Hevy",
                "'Look around. We’re one and the same. Same heart, same blood.' -Fives",
                "'We’re not programmed. You have to learn to make your own decisions.' -Captain Rex",
                "'Well, I've known no other way. Gives us clones all a mixed feeling about the war. Many people wish it never happened. But without it, we clones wouldn't exist.' -Captain Rex",
                "'Sometimes in war, it's hard to be the one that survives.' -Commander Cody",
                "'That's what brothers do.' -Rex",
                "'This ship is going down and those soldiers, my brothers, are willing to die to take you and me along with them.' -Captain Rex",
                "'Big gun doesn't make a big man.' -Commander Cody",
                "'An elegant weapon for a more civilized time, eh? Well guess what? Times have changed.' -Boss, Delta 38",
                "'With all due respect, Sir, you're in my way.' -Fixer, Delta 40",
                "'Well I think you have an intelligence problem.' -Sev, Delta 07",
                "'I love my job.' -Sev, Delta 07",
                "'I wonder what the weather's like on Kamino right now.' -Scorch, Delta 62",
                "'You hear that, Sev? Someone thinks I'm excellent.' -Scorch, Delta 62",
                "'Would you like a large or small crater, sir?' -Scorch, Delta 62",
                "'I used to think General Krell was reckless, but now I'm beginning to think he just hates clones.' -Fives",
                "'You believe that, or is that what you were engineered to think?' -Fives",
                "'We're soldiers. We have a duty to follow orders and, if we must, lay down our lives for victory.' -Captain Rex",
                "'I honor my code. That's what I believe.' -Captain Rex",
                "'I'm a soldier, like you! This is what I was bred for.' -99",
                "'This is our home. This is our war.' -Echo",
                "'Good soldiers follow orders'",
                "'I want you troopers to remember, we are shoulder-to-shoulder on those frontlines. Brothers! Rule one, we fight together.' -Colt",
                "'We're better than these guys.' -Fives",
                "'My squad? We're nothing but a bad batch--failures, like you.' -Hevy",
                "'Hey, ugly! Come and get me!' -Tup, to Pong Krell",
                "'Tup is my friend. He's not a number.' -Fives",
                "'Boys, this might be it. At least we'll go down fighting like a clone should.' -Captain Rex",
                "'How'd I spoil the fun? We haven't been shot at in years.' -Gregor",
                "'It was an honor to serve with you, Rex. It was an honor to fight with you for something that we chose to believe in.' -Gregor",
                "'I got blown up once and survived. I can survive this.' -Gregor",
                "'I can't think of a better time to die than when I'm no longer the best.' -Darman, RC-1136",
                "'I don't feel like a Republic citizen because none of us are.' -Fi, RC-8015",
                "'You can't talk to Captain Rex like that!' -Jesse",
                "'If your plans were so good, why did Commander Cody have to call us in?' -Crosshair",
                "'Commander Rex, you're in violation of Order 66. I accuse you of treason against the Grand Army of the Republic.' -Jesse",
                "'He's wound tight, but he's loyal.' -Captain Rex",
                "'...I had to...he betrayed us!' -Dogma",
                "'Well, I for one agree with the General's plan. We're running out of time and this is the best option.' -Dogma",
                "'The mission....the nightmares...they're...finally...over....' -Fives",
                "'The air in here's getting a bit stale.' -Commander Wolffe",
                "'Minimal casualties, maximum effectiveness. That's us.' -Broadside",
                "'The name's Rex, but you'll call me Captain or sir' -Captain Rex",
                "'Looks like we got us a bunch of shinies, Commander.' -Captain Rex",
                "'All right, listen up. There's only one target of interest in this sector: Kamino. It's the closest thing we Clones have to a home. Today we fight for more than the Republic. Today we fight for all our brothers back home. Understood?' -Captain Rex",
                "'Skywalker, explosives are in place, sir. Objective completed.' -Captain Rex",
                "'All of you just blindly following orders! for what?! At least I've gotten something out of all this suffering!' -Sergeant Slick",
                "'I really wish you hadn't noticed that, sir' - Sergeant Slick",
                "'A lot of the General's plans involve falling.' -Captain Rex",
                "'Sir, if I may address your accusation. I followed your orders. Even in the face of a plan that was, in my opinion, severely flawed. A plan that cost us men, not clones, MEN! As sure as it is to my duty to remain loyal to your command, I also have another duty: to protect those men.' -Captain Rex",
                "'I think he almost complimented you.' -Fives",
                "'Eh, I’m sorry sir it’s just how I am. My Kamino commander said that my incubation tube had a leak when I was made, makes me hyper-active or something.' -Hardase",
                "'Keep those clankers back! Give 'em all you've got!' -Captain Rex",
                "'Live to fight another day, boys. Live to fight another day.' -Hardcase",
                "'I don't know. Could be fun.' -Hardcase",
                "'Is Krell trying to get us killed?' -Jesse",
                "'I'm no Jedi.' -Captain Rex",
                "'We're just numbers, Ninty-Nine! Just numbers...' -Hevy",
                "'Everyone, stop firing! We're shooting at our own men!' -Captain Rex",
                "'The whole place is surrounded. No one's getting past us.' -Commander Fox",
                "'Representative Binks is the highest ranking person here.' -Commander Stone",
                "'I must get you to safety, General!' -Captain Zak",
                "'Yes, sir! Right away.' -Commander Thire",
                "'There's not much to look at here, sir. We all share the same face.' -Commander Thire",
                "'We're on your tail, General Kenobi.' -Odd Ball",
                "'Thank you, sir. Sorry I panicked.' -Odd Ball",
                "'General, the enemy fire is penetrating our shields!' -Ponds",
                "'Sir. I have five special commando units awaiting your orders, sir.' -Ponds",
                ]

droid_triggers = ["clanker",
                  "clanka"]

droid_quotes = ["'For The Republic!'",
               "'Watch those Wrist Rockets!'",
               "'I'll take care of those clankers.'",
               "'Hostiles have gained a command post!'",
               "'We can't keep losing command posts!'",
               "'Our second wave of troops is being depleted.'",
               "'Our Reinforcements are being depleted!'",
               "'Set em up and knock em down!'",
               "'We're taking heavy fire!'",
               "'We're losing ground!'",
               "'Theres too many of em!'",
               "'We're taking heavy casualties!'",
               "'I'm beginning to remember how much I hate these guys.'",
               "'Just Like the simulations!'",
               "'They're losing reinforcements!'",
               "'We captured a command post!'",
               "'Frellin' Heck it's a Super!'",
               "'They've got supers!'",
               "'One shot, one kill.'",
               "'The bigger they are; the harder they fall!'",
               "'We've got Droιdekas!'",
               "'For the Chancellor!'",
               "'No one messes with the 501st!'",
               "'Super Battle Droιd! Take it down!'",
               "'Take out that Battle Droιd!'",
               "'These are the droιds we're looking for.' -Scorch, Delta 62",
               "'I don't think Trade Federation security appreciates our work here!' -Scorch, Delta 62",
               "'Eat laser clankers!' -Sinker",
               "'So, who wants to blast some droιds?' -99",
               "'General, the enemy fire is penetrating our shields!' -Ponds",
               "'Droιds have begun a firebombing campaign.' -Ponds"]

friendly_droid_quotes = ["'Hold your fire! This one's with us!'",
                         "'Affιrmative, this one is friendly.'",
                         "'Never thought I’d see the battle droιds helping us' -Echo",
                         "'Look sir, droιds!' -Scorch, Delta 62"
                         ]

greivous_triggers = ["_💀_"]

greivous_quotes = ["'It's Grιevous, hit him from all sides!'"]

maul_triggers = ["maul"]

maul_quotes = ["'It's Darth Maul; stay back!'",
               "'Watch out for that Dual Blade!'",
               "'Darth Maul? What's he going to do, bleed on us?'"]

order_66_triggers = ["order 66",
                     "order sixty six",
                     "order sixty-six"]

order_66_quotes = ["'It will be done, my lord.'",
                   "'Yes, my lord.'",
                   "'There's been a rebellion. Don't worry. The situation is under control.' -Appo",
                   "'I was here on Coruscant. Did my part—all the clones did. Shut those Jedi agitators down cold.' -Commander Fox"]

# Put your bot's reddit id here. It will be used in several funtions.
bot_id = "dzuogrxz"

# Connecting your bot to your personal script app and logging in
reddit = praw.Reddit(client_id="SuqDqaDqKyqNGKRVy5IYjw",
                     client_secret="xvxGcYN_g3asjU3Dhruxt5ivnvyYiQ",
                     user_agent="<console:CLONE_TROOPER_BOT:1.0>",
                     username='clone_trooper_bot',
                     password= 'MysterySauce1994!')

# Begins the comment stream, scans for new comments
for comment in reddit.subreddit('PrequelMemes').stream.comments(skip_existing=True):
    
    author_name = str(comment.author.name) # Fetch author name
    author_id = str(comment.author.id) # Fetch author id
    comment_lower = comment.body.lower() # Fetch comment body and convert to lowercase
    
    with open('ignore_list.txt', 'r')as rf: # Opens ignore_list in read only mode
    
        rf_contents = rf.read() # Reads the contents of ignore list
        
        if author_id not in rf_contents and author_id != bot_id: #Checks comment against ignore list and bot id
            
            if "ignore" in comment_lower and len(comment_lower) < 8: # Looks for the word "ignore" in the comment and checks length of comment to prevent misfire.
                
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
                
                print("##### NEW COMMENT #####")
                print(comment.submission.title)
                print("          ")
                print(comment.author)
                print(comment.author.id)    
                print(comment.body.lower())
                print("           ")
                
                if any(word in comment_lower for word in order_66_triggers): #Checks for keywords in comment

                    print("===== Generating Reply =====")
                    generated_reply = random.choice(order_66_quotes) # Fetch random quote from list
                    comment.reply(generated_reply) # Replies to comment with random quote
                    print("  ")
                    print(generated_reply) # Prints random quote from reply
                    print("  ")
                    print("===== Reply Posted ======")
                    print("  ")
                    time.sleep(60) # Cooldown in seconds
                
                if any(word in comment_lower for word in droid_triggers): #Checks for keywords in comment

                    print("===== Generating Reply =====")
                    generated_reply = random.choice(droid_quotes) # Fetch random quote from list
                    comment.reply(generated_reply) # Replies to comment with random quote
                    print("  ")
                    print(generated_reply) # Prints random quote from reply
                    print("  ")
                    print("===== Reply Posted ======")
                    print("  ")
                    time.sleep(60) # Cooldown in seconds
                    
                elif any(word in comment_lower for word in maul_triggers): #Checks for keywords in comment

                    print("===== Generating Reply =====")
                    generated_reply = random.choice(maul_quotes) # Fetch random quote from list
                    comment.reply(generated_reply) # Replies to comment with random quote
                    print("  ")
                    print(generated_reply) # Prints random quote from reply
                    print("  ")
                    print("===== Reply Posted ======")
                    print("  ")
                    time.sleep(60) # Cooldown in seconds
                    
                elif any(word in comment_lower for word in greivous_triggers): #Checks for keywords in comment

                    print("===== Generating Reply =====")
                    generated_reply = random.choice(greivous_quotes) # Fetch random quote from list
                    comment.reply(generated_reply) # Replies to comment with random quote
                    print("  ")
                    print(generated_reply) # Prints random quote from reply
                    print("  ")
                    print("===== Reply Posted ======")
                    print("  ")
                    time.sleep(60) # Cooldown in seconds
                
                elif any(word in comment_lower for word in clone_triggers): #Checks for keywords in comment

                    print("===== Generating Reply =====")
                    generated_reply = random.choice(clone_quotes) # Fetch random quote from list
                    comment.reply(generated_reply) # Replies to comment with random quote
                    print("  ")
                    print(generated_reply) # Prints random quote from reply
                    print("  ")
                    print("===== Reply Posted ======")
                    print("  ")
                    time.sleep(60) # Cooldown in seconds
                    
                elif "gonk" in comment_lower:
                    
                    roll_die = random.choice(roll_d4_list)
                    
                    if roll_die == "1":
                
                        print("===== Generating Reply =====")
                        generated_reply = random.choice(droid_quotes) # Fetch random quote from list
                        comment.reply(generated_reply) # Replies to comment with random quote
                        print("  ")
                        print(generated_reply) # Prints random quote from reply
                        print("  ")
                        print("===== Reply Posted ======")
                        print("  ")
                        time.sleep(60) # Cooldown in seconds
                        
                    else:
                        
                        print("  ")
                        print("Roll failed, ignoring comment")
                        print("  ")
                
        
        else: # If user on ignore list, prints User Ignored, and does not reply to comment
            
            print("##### NEW COMMENT #####")
            print(comment.author)
            print(comment.author.id)    
            print(comment.body.lower())
            print("           ")
            
            print ("!!!!!!!! User Ignored !!!!!!!!")