import win32gui
#Get Spotify Window Info
def get_info_windows():
    global paused
    windows = []
    old_window = win32gui.FindWindow("SpotifyMainWindow", None)
    old = win32gui.GetWindowText(old_window)

    def find_spotify_uwp(hwnd, windows):
        text = win32gui.GetWindowText(hwnd)
        try:
            classname = win32gui.GetClassName(hwnd)
            if classname == "Chrome_WidgetWin_0" and len(text) > 0:
                windows.append(text)
        except:
            print("Cant find window")
    if old:
        windows.append(old)
    else:
        win32gui.EnumWindows(find_spotify_uwp, windows)
    # If Spotify isn't running the list will be empty
    if len(windows) == 0:
        return None
    # Local songs may only have a title field
    try:
        artist, track = windows[0].split(" - ", 1)
    except ValueError:
        artist = ""
        track = windows[0]
    # The window title is the default one when paused
    if windows[0].startswith("Spotify"):
        pass
    return track, artist