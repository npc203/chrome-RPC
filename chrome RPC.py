from pywinauto import Application
from pypresence import Presence
import time

#Setting up RPC stuff
client_id = 'YOUR CLIENT ID' #PASTE UR TOKEN HERE
RPC = Presence(client_id,pipe=0) 
RPC.connect()


#Getting your chrome stuff
app = Application(backend='uia')
app.connect(title_re=".*Chrome.*",found_index=0)
ytb = app.Pane.child_window(title_re=".*YouTube.*",control_type="TabItem")


def get_song():
    """getting the video name from the header file"""
    song = ytb.window_text()
    #print(song)
    spliting = song.split('-')[:-2] 
    if "Audio playing" in song:
        if len(spliting)>1:
            return spliting[0],'-'.join(spliting[1:])
        else:
            return '-'.join(spliting),'....'
    else:
        return "Idling","we doe be vibin"


#Updating the RPC
while True:  
    try:
        details,status=get_song()
        RPC.update(details=details,
                        state=status,
                        large_image='youtube',
                        )  
    except Exception as e:
        print("####",e)
        RPC.update(details="Idling",
                        state="we doe be vibin",
                        large_image='youtube',
                        )  
    time.sleep(15) # Can only update rich presence every 15 seconds



  


