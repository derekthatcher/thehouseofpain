#!/usr/bin/env python
#############################################
#####-----A text based adventure--------#####
#####----------House of Pain------------#####
#####---------Object Oriented-----------#####
#############################################
#copyright derek thatcher 2013
#now on github.com/derekthatcher/thehouseofpain/
#################################
#       #       #       #       #
#       |       |       |       #
# room7 # room8 # room9 # room10#
#       #       #       #       #
####################~#######~##############
#       #       #       #       #         #
#       |       |       #       # finish  #
# room1 # room4 # room5 # room6 #         #
#       #       #       #       #         #
###-#######-################~########-#####
#       #       #       #       #         #
#       |       |       #       #         #
# start # room2 # room3 # room11}  room12 #
#       #       #       #       #         #
###########################################

#imports
from string import lower
from thop_classes import *

#############################################
#####----------Set up the Game----------#####
#############################################
#initilise rooms
start = room()
room1 = room()
room2 = room()
room3 = room()
room4 = room()
room5 = room()
room6 = room()
room7 = room()
room8 = room()
room9 = room()
room10 = room()
room11 = room()
room12 = room()
finish = room()
finish.setup('finish',[], [], [],"Well done!")

#starting room
item1 = item('table', False, False,0)
item2 = item('chair', False, False,0)
item3 = item('pencil', True, True,2)
character1 = character('Old Midget', True, True, "So you are awake. It is time to talk. What is your business here?",101)
door1 = door('north',room1,False,'')
door2 = door('east',room2,True,'silver key')
start.setup('start',[item1,item2,item3], [character1], [door1,door2],"You are in a dark room.")
#room1
item1 = item('table', False, False,0)
item2 = item('bookcase', False, False,0)
item3 = item('book of radness', True, False,0)
item4 = item('book of wealth', True, False,-30)
character1 = character('Spider', False, True, 'Leave my web alone. Careful which book you take.',0)
door1 = door('south',start,False,'')
door2 = door('east',room4,False,'')
room1.setup('room1',[item1,item2,item3,item4], [character1], [door1,door2], "You are in the library.")
#room2
item1 = item('silver key', True, False,0)
item2 = item('battle axe', True, True,10)
item3 = item('bench', False, False,00)
character1 = character('Midget', True, False, '',160)
character2 = character('Angry Goblin', True, False, '',170)
door1 = door('west',start,False,'')
door2 = door('north',room4,True,'book of radness')
door3 = door('east',room3,True,'broad sword')
room2.setup('room2',[item1,item2,item3], [character1, character2], [door1,door2,door3], "You walk into a dirty kitchen.")
#room3
item1 = item('copper key', True, False,0)
character1 = character('Old Man', False, True, "You must learn when to run and when to fight? Beware the Angel of Doom.",0)
door1 = door('west',room2,False,'')
room3.setup('room3',[item1], [character1], [door1], "You are in a small room.")
#room4
item1 = item('fish tank', False, False,0)
item2 = item('rock', False, False,0)
character1 = character('Fish', False, True, "Can you feed me?",0)
door1 = door('west',room1,False,'')
door2 = door('south',room2,False,'')
door3 = door('east',room5,True,'silver key')
room4.setup('room4',[item1,item2], [character1], [door1,door2,door3], "You walk into a room with a large fish tank.")

#room5
item1 = item('pedestal', False, False,0)
character1 = character('Grumpy Wizard', False, True, "What do you want peasant?",0)
door1 = door('west',room4,False,'')
door2 = door('north',room9,True,'battle axe')
room5.setup('room5',[item1], [character1], [door1,door2], "You walk into a strange room.")

#room6
character1 = character('Angel', True, True, "You must search for what you desire.",500)
door1 = door('north',room10,True,'silver key')
room6.setup('room6',[], [character1], [door1], "You are near the end.")

#room7
item1 = item('rock', True, False,-5)
item2 = item('broad sword', True, True,80)
character1 = character('Huge Ogre', True, True, "I will squash you!",300)
door1 = door('east',room8,True,'rock')
room7.setup('room7',[item1, item2], [character1], [door1], "You are in a room with no way out.")

#room8
item1 = item('mirror', False, False,0)
door1 = door('west',room7,False,'')
door2 = door('east',room9,False,'')
room8.setup('room8',[item1], [], [door1,door2], "You are in a long corridor")

#room9
item1 = item('rock', False, False,0)
character1 = character('Ogre', True, True, "Prepare to die!",350)
door1 = door('west',room8,False,'')
door2 = door('south',room5,True,'broad sword')
door3 = door('east',room10,True,'copper key')
room9.setup('room6',[item1], [character1], [door1,door2,door3], "The room is dark.")

#room10
item1 = item('boxing ring', False, False,0)
character1 = character('Ogress', True, True, "Grunt, grunt.",400)
door1 = door('west',room9,False,'')
door2 = door('south',room6,True,'brass key')
room10.setup('room10',[item1], [character1], [door1,door2], "You are in a large hall.")

#room11
character1 = character('Devil Spawn', True, True, "210",210)
room11.setup('room11',[], [character1], [], "You are in the Devils Room.")
#room12
character1 = character('Evil Wizard', True, True, "Well, well my brave adventurer, you have gone out of your way to seek an audience with me. I will try not to disapoint!",1420)
item1 = item('excalibur', False, True,500)
door1 = door('west',room11,True,'brass key')
room12.setup('room12',[item1], [character1], [door1], "You are in the Wizards Parlour.")

#Intro
print "Welcome to the House of Pain."
print "Here you will learn the ways of adventure and discover the secrets hidden within the House."
print "You will talk, fight, take, unlock and move via the compass.(north, east, south, west)"
print "At any time you may view your (i)nventory or vital (s)tats. Type exit to leave game."

#define player
print "What do they call you, brave adventurer?"
user_input = raw_input('>')
you = player(user_input, start)
highscores = highscore()
highscores.load_score()
#####super powers#####
#item1 = item('super axe', True, True,500)
#you.inventory.append(item1)
#item1 = item('brass key', True, False,0)
#you.inventory.append(item1)
#item1 = item('diamond key', True, False,0)
#you.inventory.append(item1)
#item1 = item('silver key', True, False,0)
#you.inventory.append(item1)
killedangel = False
spawn_number = 1
newRoom = True
#main loop
while user_input <> 'exit':
    if you.haslamp() and newRoom:
        you.location.enter()
        newRoom = False
    elif not you.haslamp(): print "It is dark and you can not see, where is your lamp?"
    user_input = lower(raw_input('>'))
    for d in you.location.doors:
        if d.isdoor(user_input):
            if d.is_locked():
                print "The door is locked."
            else:
                you.move(d.door_to)
                newRoom = True
    #take objects
    if 'take' in user_input:
        you.take(user_input)
    #drop objects
    elif 'drop' in user_input:
        you.drop(user_input)
    elif 'look' in user_input:
        newRoom = True
    #unlock doors
    elif 'unlock' in user_input:
        for d in you.location.doors:
            d.unlock(you.inventory)
    #talk to character
    elif 'talk' in user_input:
        for c in you.location.characters:
            c.speak(user_input)
    #fight character
    elif 'fight' in user_input:
        for c in you.location.characters:
            if lower(c.name) in user_input:
                if c.fight(you):
                    if c.name == 'Angel':
                        item1 = item('diamond key', True, False,0)
                        start.add_item(item1)
                        item2 = item('katana', True, True,100)
                        room3.add_item(item2)
                        door2 = door('south',room11,True,'diamond key')
                        room6.doors.append(door2)
                        character1 = character('Angel of Doom', True, True, "You can't kill what is dead.",650)
                        room6.characters.append(character1)
                        character2 = character('Dragon', True, True, "FIRE!",1000)
                        room4.characters.append(character2)
                    elif c.name == 'Ogress':
                        item1 = item('brass key', True, False,0)
                        room1.add_item(item1)
                        character1 = character('Killer Dwarf', True, True, "You think you can match me?.",460)
                        room1.characters.append(character1)
                        print "You hear a loud explosion to the west."
                    elif c.name == 'Devil Spawn':
                        spawn_number += 1
                        character1 = character('Devil Spawn', True, True, spawn_number,210*spawn_number)
                        room11.characters.append(character1)
                    elif c.name == 'Evil Wizard':
                        door2 = door('north',finish,False,'')
                        room12.doors.append(door2)
                    elif c.name == 'Angel of Doom':
                        killedangel = True
                    you.location.characters.remove(c)
    #print inventory
    elif 'inventory' in user_input or 'i' == user_input:
        you.print_inventory()
    #print stats - health and points, number of items
    elif 'stats' in user_input or 's' == user_input:
        you.stats()
    #if dead
    # once 5 devils have spawned add door.
    if spawn_number == 5 and you.location == room11:
        door1 = door('north',start,False,'')
        door2 = door('east',room12,False,'')
        room11.doors.append(door1)
        room11.doors.append(door2)
        spawn_number += 1
    #when in wizards parlour you cab take sword once inventory is empty
    if len(you.inventory) == 0 and you.location == room12:
        room12.items[0].canTake = True
    #health is 0
    if you.health <= 0:
        print "You have died."
        you.points -= 482
        you.stats()
        user_input = 'exit'
    if you.location == finish and killedangel:
        print "You have completed the game. Congradulations."
        you.points += 482
        you.stats()
        user_input = 'exit'
    elif you.location == room11 and not killedangel:
        print "As you run through the south door the Angel of Doom kills you."
        you.points -= 1000
        you.stats()
        user_input = 'exit'

#end of game
highscores.add_score(you.name, you.points)
highscores.save_score()
highscores.print_score()





