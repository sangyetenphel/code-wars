##def song_decoder(song):
##    result = ''
##    i = 0
##    while i < len(song):
##        if i < (len(song)-2) and song[i:i+3] == "WUB":
##            i += 3
##            result += " "
##        else:
##            result += song[i]
##            i += 1
##
##    return " ".join(result.split())
##            

def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
# =>  WE ARE THE CHAMPIONS MY FRIEND
