from pywinauto import Application

app = Application(backend='uia')
app.connect(title_re=".*Chrome.*")
ytb = app.Pane.child_window(title_re=".*YouTube.*",control_type="TabItem")

def get_song():
    song = ytb.window_text()
    print(song)
    if "Audio playing" in song:
        return '-'.join(song.split('-')[:-2])
    else:
        return "Idling"

print(get_song())
