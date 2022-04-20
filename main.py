import json, webbrowser, os

# with open("rawlinks.json", "r") as file:
#     links = json.load(file)
#     file.close()

#       0                 1          2             3            4        5
#www.curseforge.com / minecraft / mc-mods / gravestone-mod / files / 3713957
#www.curseforge.com / minecraft / mc-mods / gravestone-mod / download / 3713957

def get_download_link(file_link):
    splitted = file_link.split("/")
    splitted[4] = "download"
    splitted.append("file")
    return "/".join(splitted)

for root, dirs, files in os.walk("./parts"):
    for file_path in files:
        with open(os.path.join(root, file_path), "r") as file:
            links = json.load(file)
            file.close()
        for link in links:
            print(link)
            # webbrowser.open(get_download_link(link))
