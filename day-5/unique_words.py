def unique_words(lyrics):
        
    lyrics=lyrics.split()
    new_lyrics = ''
    for lyric in lyrics:
        lyric = lyric.lower()
        new_lyrics = new_lyrics +' '+ lyric
        split_lyrics = new_lyrics.split()
        
    
    print(set(split_lyrics))

def unique_words1(lyrics):
    lyrics = lyrics.lower()
    count = 0
    unique_words =[]
    for word in lyrics.split():
        if word not in unique_words:
            unique_words.append(word)
            count = count + 1
    print(unique_words)
    print('total number of unique words is = ',count)




lyrics = """
So so you think you can tell
Heaven from hell
Blue skies from pain
Can you tell a green field
From a cold steel rail
A smile from a veil
Do you think you can tell
Did they get you to trade
Your heroes for ghosts
Hot ashes for trees
Hot air for a cool breeze
Cold comfort for change
Did you exchange
A walk on part in the war
For a lead role in a cage
How I wish, how I wish you were here
We're just two lost souls
Swimming in a fish bowl
Year after year
Running over the same old ground
And how we found
The same old fears
Wish you were here

"""


unique_words1(lyrics)


