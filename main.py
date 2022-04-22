import json, webbrowser, os, requests, time
from bs4 import BeautifulSoup

#split
#       0                 1          2             3            4        5
#www.curseforge.com / minecraft / mc-mods / gravestone-mod / files / 3713957
#www.curseforge.com / minecraft / mc-mods / gravestone-mod / download / 3713957

#direct links
#https://media.forgecdn.net/files/3441/117/iceandfire-2.1.9-1.16.5.jar
#https://edge.forgecdn.net/files/3441/117/iceandfire-2.1.9-1.16.5.jar

mod_count = 0

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
            webbrowser.open(get_download_link(link))
            time.sleep(0.5)
            mod_count += 1
        time.sleep(2.0)

            # page = requests.get("https://" + link)
            # soup = BeautifulSoup(page.content, "html.parser")
            # file_name = soup.find_all("span", {"class": "text-sm"})
            # print("\n".join(file_name))
            # print(page.content)
            # print(link)

# do_test = True

# if do_test:
#     page = requests.get("https://www.curseforge.com/minecraft/mc-mods/mekanism/files/3659389")
#     soup = BeautifulSoup(page.content, "html.parser")
#     print(page.content)
#     file_name = soup.find_all("div", class_="flex flex-row md:flex-col mr-2 justify-between md:flex-col md:w-full md:justify-between")
#     print("\n".join(file_name))
# else:
