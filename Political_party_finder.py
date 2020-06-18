#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# words/frases a democrate might use
democratic_affiliation = ['#dem','#democrat','#dems','#democrats','#undocumentedimmigrants', '#gun safety', '#estate tax',
                          '#obama','#biden','#forward','#middle class']

# words/frases a republican might use
republican_affiliation = ['#rep','#republican','#republicans','#guncontrol','#deathtax','#illegalaliens', '#foxnews','#extremist',
                         '#radical', '#americandream','#trump','#church','#freedom']

# words/frases a liberal might use
liberal_affiliation = ['#libertarian',' #trump',' #conservative',' #liberty',' #freedom',' #republican','#politics', '#liberal', '#maga', '#capitalism' ,' #ancap', '#taxationistheft', 
        '#democrat', '#boogaloo', '#america', '#usa', '#socialism', '#guns', '#libertarianism', '#memes', '#anarchy', '#constitution', '#donaldtrump', '#libertarianmemes' ,'#anarchist', '#donttreadonme',
        '#communism', '#anarchism' ,'#bhfyp']




# This program will try and figure out based on a persons message what political party they are or
# what party they are in









#----------------------------------------------------------------

# input of tweet

Your_tweet = input('Type in your tweet here please: ')
Your_tweet = Your_tweet.lower()




#----------------------------------------------------------------
def Convert(tweet_split):
        
        tweet_split = list(tweet_split.split(" "))
       
        return tweet_split
    
    
#----------------------------------------------------------------
        
def party_determine(Your_tweet):
    
    
    dem_count = 0
    rep_count = 0
    lib_count = 0




# This part will count/rank how many words are related to a certain & most likely would be said by a person associated to a 
# political party
    
    for word in Your_tweet:
        if word in democratic_affiliation:
            dem_count += 1
       


    for word1 in Your_tweet:
        if word1 in republican_affiliation:
            rep_count += 1
        


    for word2 in Your_tweet:
        if word2 in liberal_affiliation:
            lib_count += 1

    #return [dem_count,rep_count,lib_count]



# now will see which count has the most and determine what party they might be a part of:


# checking democratic affiliation
    if (dem_count > 0) and ((dem_count>rep_count) and (dem_count>lib_count)):
        print('Based on this tweet, this person is most likely a democrat.')
       
# checking republican affiliation
            
    if (rep_count > 0) and ((rep_count>dem_count) and (rep_count>lib_count)):
        print('Based on this tweet, this person is most likely a republican.')
      
# checking libritarian affiliation

    if (lib_count > 0) and ((lib_count>rep_count) and (lib_count>dem_count)):
        print('Based on this tweet, this person is most likely a libritarian.')
        

    








#----------------------------------------------------------------



# Function call

Your_tweet = Convert(Your_tweet)    # This will convert the input message to a list

Your_most_likely_party = party_determine(Your_tweet)    # This will take the given message and rank the likelyness 
                                                        # of it being affiliated to a certain party




