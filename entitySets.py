import xml.etree.ElementTree as ET
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)

outputclear = open("output.txt", "w")
outputclear.write("The file has been reset and the new output has been created")
outputclear.close()
output = open("output.txt", "a")

files = [x for x in os.listdir()
            if os.path.isfile(x)
                if x.endswith(".xml")
]

for x in range(len(files)):
    try:
        tree = ET.parse(files[x])
        root = tree.getroot()
        a = root.find('.//entitySets/Item')
        if a:
            print()
            print()
            print(Fore.LIGHTMAGENTA_EX + Back.LIGHTWHITE_EX + files[x])
            output.write("\n\n\n" + files[x] + "\n\n")
            for elements in root.findall('.//entitySets/Item'):
                    entitySetsName = elements.find('name').text
                    if entitySetsName:
                        print(Fore.LIGHTGREEN_EX + entitySetsName)
                        output.write(entitySetsName + "\n")
                    else:
                        print("This entitySets does not have a name")
        else:
            os.remove(files[x])
            print(Fore.RED + Back.RESET + "The file: " + files[x] + " has beed deleted | Reason: does not have any entitySets")
    except:
        os.remove(files[x])
        print(Fore.RED + Back.RESET + "The file: " + files[x] + " has been deleted | Reason: could not be opened")
output.close()
print(Fore.CYAN + Back.RESET + "\n\n\nA file has been created with the name: output.txt | in the file you will find the result of your search\nCopy the result from console with: CTRL + SHIFT + C " + Fore.LIGHTCYAN_EX + "or" + Fore.CYAN +" (recommended) use the file that have been created\n")
print()
input("Press ENTER to close")