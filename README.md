# A Chrome Youtube RPC for discord:

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord)](https://github.com/qwertyquerty/pypresence) [![license](https://img.shields.io/github/license/qwertyquerty/pypresence.svg?style=for-the-badge)](https://github.com/npc203/chrome-RPC/blob/branch/LICENSE)

![Imgur](https://i.imgur.com/r90l0KG.png)
> if this works for you, then it's nothing short of a miracle. Just another fun project.
> Unstable, you better have some knowledge of python and pywinauto else don't even bother cloning the repo unless you want to learn something from this.


## Installing:

1. Highly recommended that you do this in a venv
2. Just clone the repo and install the requirements
3. Run the `chrome RPC.py` 

```shell
git clone https://github.com/npc203/chrome-RPC.git
cd chrome-RPC
pip install -r requirements.txt
python "chrome RPC.py"
```

## Important Note:
You need to have the RPC token, cause I can't give mine lol.(or can I? hmm)
Just goto the discord developer portal and make an app.
1. Name the app as Youtube.
2. Under the Rich presence assets, Add a youtube icon image(pick from the net).
3. You `must` name the icon "youtube" (without quotes UwU)
4. copy paste the your token into the py file

## Anomalities:
1. Says as Idling if youtube is in miniplayer mode.
2. Only works for chrome, too lazy to add others.
3. Enclosed the loop with try catch so that the errors are silent, 
   probably a bad idea, idk remove it, if needed.
4. <Fill here> I'm pretty sure there are more.

## TODOS:
- Make it so that the code runs in the background
- Add some sort of QT GUI for more control
- Add support for other browsers
- Why not extend it to other tabs rather than Ytb alone?!
- More stable and reliable way of getting the tabs
- package it (far far far future)

### Footer stuff?:
- Any PR's, issues, features, improvements are always welcome,
- The debug folder is just junk files, delete them if you want
- yes i wrote this kinda detailed readme to understand how markdown works 😂.
- Made with pypresence and pywinauto.
