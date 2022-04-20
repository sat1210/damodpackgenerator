import json, webbrowser

with open("rawlinks.json", "r") as file:
    links = json.load(file)
    file.close()

def get_download_link(file_link):
#       0                 1          2             3            4        5
#www.curseforge.com / minecraft / mc-mods / gravestone-mod / files / 3713957
#www.curseforge.com / minecraft / mc-mods / gravestone-mod / download / 3713957
    splitted = file_link.split("/")
    splitted[4] = "download"
    return "/".join(splitted)

for link in links:
    webbrowser.open(get_download_link(link))
