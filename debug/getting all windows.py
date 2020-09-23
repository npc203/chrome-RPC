from pywinauto import Desktop

windows = Desktop(backend="uia").windows()
for w in windows:
    if "Chrome" in str(w):
        print(w)
