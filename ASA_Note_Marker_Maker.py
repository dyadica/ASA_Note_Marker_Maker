# Used to brute parse data from the following ark.wiki.gg pages

# https://ark.wiki.gg/wiki/Explorer_Map/The_Island
# https://ark.wiki.gg/wiki/Explorer_Map/Scorched_Earth
# https://ark.wiki.gg/wiki/Explorer_Map/Aberration

import json
import os

#marker deffinitions to cater for differing color and icon (lazzy).
unEditedStringD = """SavedMinimapMarks=(Name="{1}",CustomTag="{2}",Location=(X={3},Y={4},Z={5}),Color=(R=0.134600,G=0.123100,B=0.379481,A=1.000000),ID=232,MarkIcon=/Script/Engine.Texture2D'"/Game/PrimalEarth/UI/Textures/T_UI_HUDPointOfInterest_Tame.T_UI_HUDPointOfInterest_Tame"',MapName="{6}",bIsShowing=False,IconColor=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),bIsShowingText=True,CharacterID=-1,CharacterIsPlayer=False)"""
unEditedStringN = """SavedMinimapMarks=(Name="{1}",CustomTag="{2}",Location=(X={3},Y={4},Z={5}),Color=(R=0.000000,G=0.123100,B=0.379481,A=1.000000),ID=232,MarkIcon=/Script/Engine.Texture2D'"/Game/PrimalEarth/UI/Textures/T_UI_HUDPointOfInterest_Special.T_UI_HUDPointOfInterest_Special"',MapName="{6}",bIsShowing=False,IconColor=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),bIsShowingText=True,CharacterID=-1,CharacterIsPlayer=False)"""
unEditedStringB = """SavedMinimapMarks=(Name="{1}",CustomTag="{2}",Location=(X={3},Y={4},Z={5}),Color=(R=1.000000,G=0.123100,B=0.379481,A=1.000000),ID=232,MarkIcon=/Script/Engine.Texture2D'"/Game/PrimalEarth/UI/Textures/T_UI_HUDPointOfInterest_Special.T_UI_HUDPointOfInterest_Special"',MapName="{6}",bIsShowing=False,IconColor=(R=1.000000,G=1.000000,B=1.000000,A=1.000000),bIsShowingText=True,CharacterID=-1,CharacterIsPlayer=False)"""

#Change as required; the name of the map which you wish to create markers for

#mapName = "TheIsland_WP"
mapName = "ScorchedEarth_WP"
#mapName = "Aberration_WP"

#These are the names of the files I created using the json data from the aforementioned ark.wiki.gg pages. Files must be saved next to the script!

#mapData = "theIsland.json"
mapData = "scorchedEarth.json"
#mapData = "aberration.json"

#The names of the files that you wish to create. These are then cut and pasted into GameUserSettings.ini. Change name as required
#noteFileName = "islandNotes.txt"
#cmdsFileName = "islandCmds.txt"
noteFileName = "scorchedNotes.txt"
cmdsFileName = "scorchedCmds.txt"
#noteFileName = "aberrationNotes.txt"
#cmdsFileName = "aberrationCmds.txt"

#Lists to temp save the extracted data
TeleportCmds = list()
ExtractedData = list()

#Perform the data extraction
def beginDataExtraction():

    with open('json/' + mapData) as f:
        
        data = json.load(f)        
        #print(data)
        
        markers = data["markers"]
        #Find the dossiers
        dossiers = markers["dossier"]
        #Find the explorer-note(s)
        expNotes = markers["explorer-note"]
        
        #Extract data
        extractNoteData(dossiers)
        extractNoteData(expNotes)
    
def extractNoteData(notes):
    
    for note in notes:
        
        #Get lat and lon
        lat = note["lat"]
        lon = note["lon"]
        
        #Strip unused html and text
        n = note["name"]
        n = n.replace('<span class="datamap-explorer-note-id">','')
        n = n.replace(' (ID: ',',')
        n = n.replace(')</span>','')
        
        #Split remaning data [name, id]
        x = n.split(',')
        
        name = x[0]
        nid = x[1]
        
        #print(name, lat, lon)
        
        #Strip unused html and text
        d = note["description"]
        d = d.replace('Teleport command: <code>','')
        d = d.replace('</code>','')
        
        #Store teleport command
        TeleportCmds.append(name + ": " + d)
        
        #Strip unused html and text
        ch = d.replace('cheat spi ','')
        
        #Get the x, y, z
        chords = ch.split(' ')
        dx = chords[0]
        dy = chords[1]
        dz = chords[2]
        
        #print(ch)
        
        #Swap marker deffinition to cater for differing color and icon (lazzy).
        
        #Get default marker deffinition
        editedString = unEditedStringN
        
        #Is it a dossier if so swap default
        if("Dossier" in name):
           editedString = unEditedStringD
        
        #Is it a tall tale if so swap default
        if("Bobs Tall Tales" in name):
           editedString = unEditedStringB     
        
        #Input json data into marker deffinition
        editedString = editedString.replace('{1}', name)
        editedString = editedString.replace('{2}', nid)        
        editedString = editedString.replace('{3}', dx)
        editedString = editedString.replace('{4}', dy)
        editedString = editedString.replace('{5}', dz)        
        editedString = editedString.replace('{6}', mapName)
        
        #Store marker deffinition
        ExtractedData.append(editedString)

#Write the Marker definitions to text file named via <noteFileName>          
def writeDataToFile():
    
    if not os.path.exists('bin'):
        os.makedirs('bin')
    
    for data in ExtractedData:
    
        # print(data + "\r")
        
        f = open('bin/' + noteFileName, "a")
        f.write(data + "\r")
        f.close()

#Write the Marker definitions to text file named via <cmdsFileName>    
def writeCmdsToFile():
    
    if not os.path.exists('bin'):
        os.makedirs('bin')
        
    for data in TeleportCmds :
    
        # print(data + "\r")
        
        f = open('bin/' + cmdsFileName, "a")
        f.write(data + "\r")
        f.close()
        
#Perform extraction  
print("Extracting Information")
beginDataExtraction()
#Write data
print("Writing Information")
writeDataToFile()
writeCmdsToFile()
#Coffee time!
print("Done")

while True:
    break