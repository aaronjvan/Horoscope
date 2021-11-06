from pyhoroscope import *
from emotionAnalysis import *
from secrets import *
from spotPlaylistGetter import *

moodPlaylist = {"happy": "79QRwz97ZME65XdEp1eqQm?si=4791f0586e104ae5",
                 "sad": "5nT9FdSNMNTwNkvdX5lkta?si=6638465833bf4bcd", 
                 "loved": "1XPefR0TaISwZXw8ltYew4?si=c95f6aa7e2c04548",
                 "angry": "5NAiz92PO6eD61j5lGhrhY?si=07ecbd3dd2744f5c",
                 "scared": "1r4hnyOWexSvylLokn2hUa?si=62928bc1d0ce4756"}

if __name__ == "__main__":
    horo = Horoscope()
    birthMonth = input("What month is your birthday? : ")
    birthDay = input("What is the birth date? : ")
    sign = getStarSign(str(birthMonth), int(birthDay))
    #sign = input("What is your sunsign?")
    data = horo.get_todays_horoscope(sign)
    dailyMessage = data['horoscope']
    print(dailyMessage)
    mood = analyzeText(dailyMessage, 'emotions.txt')
    #THIS IS THE WHOLE API REQUEST
    
    token = getAccessToken(ClientID, ClientSecret)
    if(mood == " happy"):
        playlistID = (moodPlaylist.get("happy"))
    elif(mood == " sad"):
        playlistID = (moodPlaylist.get("sad"))
    elif(mood == " angry"):
        playlistID = (moodPlaylist.get("angry"))
    elif(mood == " scared"):
        playlistID = (moodPlaylist.get("scared"))
    else:
        playlistID = (moodPlaylist.get("loved"))
    
    tracklist = getPlaylistTracks(token, playlistID)

'''
    for t in tracklist['tracks']['items']:
        print("--------------------")
        for a in t['track']['artists']:
            print(a['name'])
        songName = t['track']['name']
        print(songName)
'''