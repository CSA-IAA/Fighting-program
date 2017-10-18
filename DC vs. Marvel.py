'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
Fighting program
Version .1
'''

from tkinter import *
from tkinter import ttk
import sys

class Stats: #attack, defense, health, regeneration variables
    def __init__(self, attack, defense, health, regeneration):
        self.attack = attack
        self.defense = defense
        self.health = health
        self.regeneration = regeneration

#DC attack,defense,health
Superman = Stats(50, 95, 95, 45)
Supergirl = Stats(60, 60, 60, 30)
Flash = Stats(20, 10, 10, 90)
Green_Lantern = Stats(30, 50, 60, 0)
#Marvel attack,defense,health
Hulk = Stats(80, 60, 70, 10)
Thor = Stats(60, 70, 80, 30)
Cyclops = Stats(35, 10, 10, 0)
Wolverine = Stats(45, 20, 20, 90)

root = Tk() #creates GUI
root.title("DC Vs. Marvel") #title

def doNothing(): #exit function
    sys.exit() # exists the window

def fight():
    if len(box1.curselection()): #checks to see if a character was selected from box 1
        if len(box2.curselection()):  #checks to see if a character was selected from box 2, if yes then has them fight
            #makes it so that there has to be a character chosen from each box if fight button is pressed

            DCl = [Superman, Supergirl, Flash, Green_Lantern]
            #list of characters that are connected to Class(as variables) stored in list for access
            Marvell = [Hulk, Thor, Cyclops, Wolverine]
            char1 = box1.curselection()[0] #locates index of selected item
            charl= DCl[char1] #uses that index and finds item in list with same index and connects to character class
            charl_d = charl.defense*2 #now can multiply selected character's defense by two
            charl_r = charl.regeneration/2 #divide selected character's regeneration by two
            charl_s = (charl_d+charl.health+charl_r)#adds health, defense, and regen to subtract with the enemy's attack

            Marvchar1 = box2.curselection()[0]
            Marvcharl= Marvell[Marvchar1]
            Marvcharl_d = Marvcharl.defense*2
            Marvcharl_r = Marvcharl.regeneration/2
            Marvcharl_s = (Marvcharl_d+Marvcharl.health+Marvcharl_r)

            dcc = charl_s-Marvcharl.attack #subtracts the attack of a marvel character against total health of DC's char
            marv = Marvcharl_s-charl.attack#subtracts the attack of a DC character against total health of Marvel's char

            box1.select_clear(0, END) #clears the blue highlight
            box2.select_clear(0, END)

            DCs.set('Name: ' + '\n' + 'Power: ' + '\n' + 'Attack: ' + '\n' + 'Defense: ' '\n' + 'Health: ' + '\n' +
                'Regeneration: ')
            # clears stats
            Marvels.set('Name: ' + '\n' + 'Power: ' + '\n' + 'Attack: ' + '\n' + 'Defense: ' '\n' + 'Health: ' +
                        '\n' + 'Regeneration: ')

            #checks to see whos remaining HP is the lesser amount. one with bigger HP amount left is winner
            if dcc > marv: #This matchup leaves DC with more HP left
                winlos.set('Winner: ' + '\n' + box1.get(ACTIVE) + '\n' + 'Loser: ' + '\n' + box2.get(ACTIVE))
                #winlos.set(box1.get(ANCHOR)+'\n'+'Wins!') #says who the winner is
                winDc.set(winDc.get() + 1) #adds one win to DC's score if they beat a character of Marvel
                lossMarvel.set(lossMarvel.get() + 1) # adds one loss to marvels score if they lose to a character of DC

            elif marv > dcc: #This matchup leaves Marvel with more HP left
                winlos.set('Winner: ' + '\n' + box2.get(ACTIVE) + '\n' + 'Loser: ' + '\n' + box1.get(ACTIVE))
                #winlos.set(box2.get(ANCHOR) + '\n' + 'Wins!') #says who the winner is
                winMarvel.set(winMarvel.get() + 1) #adds one win to marvels score if they beat a character of DC
                lossDc.set(lossDc.get() + 1) #adds one loss to DC's score if they lose to a character of Marvel
            elif dcc == marv: #This matchup leaves both DC and Marvel with same HP
                print("It was a tie")

        else:
            pass #wont let them through unless they pick character from each box
    else:
        pass #wont let them through unless they pick character from each box

def DCstat(*args):
    char = box1.curselection() #finds the index of the selected item
    if 0 in char: #checks to see if the 0 index is in that list. only one index is in the list(the one selected)
        char_n = "Superman" #character selected
        char_attack = "Laser Vision" #type of power being used(currently)
        DCs.set('Name: '+char_n+'\n'+ 'Power: '+char_attack+'\n'+'Attack: '+str(Superman.attack)+'\n'+'Defense: '+
                str(Superman.defense)+'\n'+'Health: '+str(Superman.health)+'\n'+'Regeneration: '+
                str(Superman.regeneration)) #his/her stats
    elif 1 in char: #checks to see if the 1st index is in that list. only one index is in the list(the one selected)
        char_n = "Supergirl"
        char_attack = "Strength"
        DCs.set('Name: '+char_n+'\n'+ 'Power: '+char_attack+'\n'+'Attack: '+str(Supergirl.attack)+'\n'+'Defense: '+
                str(Supergirl.defense)+'\n'+'Health: '+str(Supergirl.health)+'\n'+'Regeneration: '+
                str(Supergirl.regeneration)) #his/her stats
    elif 2 in char:
        char_n = "Flash"
        char_attack = "Speed"
        DCs.set('Name: '+char_n+'\n'+ 'Power: '+char_attack+'\n'+'Attack: '+str(Flash.attack)+'\n'+'Defense: '+
                str(Flash.defense)+'\n'+'Health: '+str(Flash.health)+'\n'+'Regeneration: '+
                str(Flash.regeneration)) #his/her stats
    elif 3 in char:
        char_n = "Green Lantern"
        char_attack = "Power ring"
        DCs.set('Name: '+char_n+'\n'+ 'Power: '+char_attack+'\n'+'Attack: '+str(Green_Lantern.attack)+'\n'+'Defense: '+
                str(Green_Lantern.defense)+'\n'+'Health: '+str(Green_Lantern.health)+'\n'+'Regeneration: '+
                str(Green_Lantern.regeneration)) #his/her stats
    else:
        pass

def Marvelstat(*args):
    char = box2.curselection() #finds the index of the selected item
    if 0 in char: #checks to see if the 0 index is in that list. only one index is in the list(the one selected)
        char_n = "Hulk" #character selected
        char_attack = "Strength"  #type of power being used(currently)
        Marvels.set('Name: '+char_n+'\n'+ 'Power: '+char_attack+'\n'+'Attack: '+str(Hulk.attack)+'\n'+'Defense: '+
                str(Hulk.defense)+'\n'+'Health: '+str(Hulk.health)+'\n'+'Regeneration: '+
                str(Hulk.regeneration)) #his/her stats
    elif 1 in char: #checks to see if the 1st index is in that list. only one index is in the list(the one selected)
        char_n = "Thor"
        char_attack = "Hammer"
        Marvels.set('Name: '+char_n+'\n'+ 'Power: '+char_attack+'\n'+'Attack: '+str(Thor.attack)+'\n'+'Defense: '+
                str(Thor.defense)+'\n'+'Health: '+str(Thor.health)+'\n'+'Regeneration: '+
                str(Thor.regeneration)) #his/her stats
    elif 2 in char:
        char_n = "Cyclops"
        char_attack = "Optic Blast"
        Marvels.set('Name: '+char_n+'\n'+ 'Power: '+char_attack+'\n'+'Attack: '+str(Cyclops.attack)+'\n'+'Defense: '+
                str(Cyclops.defense)+'\n'+'Health: '+str(Cyclops.health)+'\n'+'Regeneration: '+
                str(Cyclops.regeneration)) #his/her stats
    elif 3 in char:
        char_n = "Wolverine"
        char_attack = "Claws"
        Marvels.set('Name: '+char_n+'\n'+ 'Power: '+char_attack+'\n'+'Attack: '+str(Wolverine.attack)+'\n'+'Defense: '+
                str(Wolverine.defense)+'\n'+'Health: '+str(Wolverine.health)+'\n'+'Regeneration: '+
                str(Wolverine.regeneration)) #his/her stats
    else:
        pass
root.option_add('*tearOff', FALSE) #gets rid of dashed line

menu = Menu(root) #creates menu
root.config(menu=menu) #adds ability to create options

subMenu = Menu(menu) #creats submenu
menu.add_cascade(label="File", menu=subMenu) # creates a memu option
subMenu.add_command(label="Exit", command=doNothing) #file option

mainframe = ttk.Frame(root, padding="5 10")
mainframe.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#listbox characters
charz= ['Superman', 'Supergirl', 'Flash', 'Green Lantern'] #DC
charx= ['Hulk', 'Thor', 'Cyclops', 'Wolverine'] #Marvel

#variable where characters,wins,losses,stats are stored
chara = StringVar(value=charz)
charb = StringVar(value=charx)
DCs = StringVar()
Marvels = StringVar()
winDc = IntVar()
lossDc = IntVar()
winMarvel = IntVar()
lossMarvel = IntVar()
winlos = StringVar()

#exportselection makes it so that they can select from both listboxes at the same.
box1 = Listbox(mainframe, height=4, listvariable=chara, exportselection=0) #DC
box1.grid(column = 1, row = 1, sticky = W)
#creates listbox which has all the characters. listvariable acceses the characters and adds to listbox
box2 = Listbox(mainframe, height=4, listvariable=charb, exportselection=0) #Marvel
box2.grid(column = 3, row = 1, sticky = E)

ttk.Label(mainframe, textvariable = winlos).grid(column = 2, row = 1, sticky=(W,E))
#creates a label so that fight button can be centered and place to put winner
winlos.set('Winner: '+'\n'+'\n'+'Loser: '+'\n')

#wins and losses for each side
ttk.Label(mainframe, text="Wins:").grid(column=1, row=2, sticky = W) #DC
ttk.Label(mainframe, text="Losses:").grid(column=1, row=3, sticky = W) #DC
ttk.Label(mainframe, text="Wins:").grid(column=3, row=2,sticky = W) #Marvel
ttk.Label(mainframe, text="Losses:").grid(column=3, row=3, sticky = W) #Marvel

#creates a label to put the stats of characters in
ttk.Label(mainframe, textvariable=DCs).grid(column=1, row=4, sticky=(W))
ttk.Label(mainframe, textvariable=Marvels).grid(column=3, row=4, sticky=(W))
DCs.set('Name: ' + '\n' + 'Power: ' + '\n' + 'Attack: ' + '\n' + 'Defense: ' '\n' + 'Health: ' + '\n' +'Regeneration: ')
# stats format
Marvels.set('Name: ' + '\n' + 'Power: ' + '\n' + 'Attack: ' + '\n' + 'Defense: ' '\n' + 'Health: ' +
            '\n' +'Regeneration: ')

#wins and losses score sticked east cause west is label of Wins/Losss
ttk.Label(mainframe, textvariable=winDc).grid(column=1, row=2, sticky=E) #wins for DC
ttk.Label(mainframe, textvariable=lossDc).grid(column=1, row=3, sticky=E) #loss for DC
ttk.Label(mainframe, textvariable=winMarvel).grid(column=3, row=2, sticky=E) #wins for Marvel
ttk.Label(mainframe, textvariable=lossMarvel).grid(column=3, row=3, sticky=E) #loss for Marvel

#fight button takes to fight function
ttk.Button(mainframe, text="Fight!", command=fight).grid(column=2, row=5, sticky=(N,S,E,W))

box1.bind('<<ListboxSelect>>', DCstat) #shows stat of DC character when selected
box2.bind('<<ListboxSelect>>', Marvelstat) #shows stat of DC character when selected

#moves everything as window expands
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=3)
mainframe.columnconfigure(2, weight=3)
mainframe.columnconfigure(3, weight=3)
mainframe.rowconfigure(1, weight=3)
mainframe.rowconfigure(2, weight=3)
mainframe.rowconfigure(3, weight=3)
mainframe.rowconfigure(4, weight=3)
mainframe.rowconfigure(5, weight=0)#so button size doesnt become overly big

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()