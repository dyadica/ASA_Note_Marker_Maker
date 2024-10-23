# ASA_Note_Marker_Maker
A simple Python script to create Ark Survival Ascended (ASA) Explorer note markers and teleport commands from json data found at [ark.wiki.gg](ark.wiki.gg).

![Screenshot of some parsed map data](/img/map_1.jpg)

## The TLDR just want the files

Parsed files can be found in the bin directory. Cut and paste the marker data as required into the GameUserSettings.ini file below the header [/Script/ShooterGame.ShooterGameUserSettings]. Teleport data can be used by pasting the commands into the command terminal. The GameUserSettings.ini can be found via:
\Steam\steamapps\common\ARK Survival Ascended\ShooterGame\Saved\Config\Windows

[Click here for the files](/bin)

# How to use the script

...Just hit play :)

The script can used to 'brute' parse data from the following ark.wiki.gg pages

- [https://ark.wiki.gg/wiki/Explorer_Map/The_Island](https://ark.wiki.gg/wiki/Explorer_Map/The_Island)
- [https://ark.wiki.gg/wiki/Explorer_Map/Scorched_Earth](url)
- [https://ark.wiki.gg/wiki/Explorer_Map/Aberration](url)

As additional maps are released and the coresponding data is updated at [ark.wiki.gg](ark.wiki.gg), the script can be amended to parse any new map data. This is as long as they dont change the formating. The data can be obtained via visiting the webpage and clicking on the 'Edit map data' button (pencil icon). Copy the json and save it as a .json file in the directory 'json' found next to the script. This can then be parsed by setting the name of the file to your filename i.e. mapData = "theIsland.json"

## Step by step usage

1. Change the name of the map which you wish to create markers for e.g. mapName = "TheIsland_WP"
2. Set the name of the .json data you wish to parse e.g. mapData = "theIsland.json". Files must be in the json directory next to the script.
3. Set a name for the file where the note marker text data is to be saved e.g. noteFileName = "islandNotes.txt"
4. Set a name for the file where the teleport commands are to be saved e.g. cmdsFileName = "islandCmds.txt"
5. Run the script
6. Cut and paste info as required to GameUserSettings.ini (marker data) or the command terminal (teleport commands).

![Screenshot of some parsed map data](/img/map_2.jpg)

Please be aware that the script ammends files and therefore will add data to any existing data. Either delete the files before use or ensure they are empty. Or add the relevant checks and functionality ;)




