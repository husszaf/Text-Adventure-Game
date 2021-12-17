#creating 3 classes: Room, Choice and Treasure to create different objects (rooms) of these classes.
class Room:
    def __init__(self, empty_room, use_command, collect_command, north_door, south_door, west_door): #initializing by using the constructor
        self.empty_room = empty_room
        self.use_command = use_command
        self.collect_command = collect_command
        self.north_door = north_door
        self.south_door = south_door
        self.west_door = west_door
    def look(self):
        self.look_start_room = self.empty_room
        return self.look_start_room
    def move(self):
        pass
    def use(self):
        self.use_com = self.use_command
        return self.use_com
    def collect(self):
        self.collect_com = self.collect_command
        return self.collect_com
    def north(self):
        self.north_com = self.north_door
        return self.north_com
    def west(self):
        self.west_com = self.west_door
        return self.west_com
    def south(self):
        self.south_com = self.south_door
        return self.south_com
class Choice:
    def __init__(self, decision_choice, direction_choice, unknown_choice, no_east_key, room_decision_command):
        self.decision_choice = decision_choice
        self.direction_choice = direction_choice
        self.unknown_choice = unknown_choice
        self.no_east_key = no_east_key
        self.room_decision_command = room_decision_command
    def whattodo(self):
        self.whattodo_com = self.decision_choice
        return self.whattodo_com
    def direction(self):
        self.direction_com = self.direction_choice
        return self.direction_com
    def unknown(self):
        self.unknown_com = self.unknown_choice
        return self.unknown_com
    def direction_nokey(self):
        self.direction_nokey_com = self.no_east_key
        return self.direction_nokey_com
    def room_decision(self):
        self.room_decision_com = self.room_decision_command
        return self.room_decision_com

class Treasure:
    def __init__(self, chest_treasure, bookcase_treasure):
        self.chest_treasure = chest_treasure
        self.bookcase_treasure = bookcase_treasure
    def chest(self):
        self.chest_treasure_com = self.chest_treasure
        return self.chest_treasure_com
    def bookcase(self):
        self.bookcase_treasure_com = self.bookcase_treasure
        return self.bookcase_treasure_com

#creating an instance of the room one
roomone = Room("You are in an empty room. There is a door to the north, and a door to the west. Behind you to the south is the stairs that lead back to the entrance.",
               "Nothing to use","Nothing to collect","The door to the north is locked.","You are back to the entrance!",
               "You are in a small room with a table. Upon the table are some letters and a key. There is a door to the East.")

#creating an instance of the room two
roomtwo = Room("You are in a small room with a table. Upon the table are some letters and a key. There is a door to the East.",
               "Nothing to use","What would you like to collect? The [Coin], the [Key] or the [Letters]?","The door to the north is locked.",
               "You are back to the entrance!", "You are in a small room with a table. Upon the table are some letters and a key. There is a door to the East.")
#creating an instance of room two when the coin is taken, so this way I can output the correct options [key] and [letters] instead of having also [coin] which is not needed.
roomtwo_cointaken = Room("You are in a small room with a table. Upon the table are some letters and a key. There is a door to the East.",
               "Nothing to use","What would you like to collect? The [Key] or the [Letters]?","The key fits! You turn it and the door unlocks.", "You are back to the entrance!",
               "You are in a small room with a table. Upon the table are some letters and a key. There is a door to the East.")

#creating an instance of room three
roomone_collected_key = Room("You are in an empty room. There is a door to the north, and a door to the west. Behind you to the south is the stairs that lead back to the entrance.",
               "What would you like to use? [Key]","Nothing to collect","The key fits! You turn it and the door unlocks. ","You are back to the entrance!",
               "This door is already unlocked")
#creating an instance of room four
roomthree = Room("You are in a dark room. There is bookcase against the wall and a chest in the centre of the room, lit only by the light of the doorway. There is a door to the South.",
                "What would you like to use? [Bookcase] or [Chest]","There is nothing here to collect","The door to the north is locked.","You are back to the entrance!","Which direction would you like to move? [South]?")
#creating an instance of room five
roomfour = Room("You are in an empty room. There is a door to the north, and a door to the west. Behind you to the south is the stairs that lead back to the entrance.",
                "","","","","")
roomfive = Room("You are in an empty room. There is a only door to the west",
               "Nothing to use","Nothing to collect","The door to the north is locked.","You are back to the entrance!",
               "You are in a small room with a table. Upon the table are some coins. There is a door to the West.")

#creating an instance of the choice class
choice_roomone = Choice("What would you like to do? [Look], [Move], [Use] or [Collect].","Which direction would you like to move? [North], [South] or [West]","Command not recognised!","none","none")

choice_roomtwo = Choice("What would you like to do? [Look], [Move], [Use] or [Collect].","Which direction would you like to move? [East]?","Command not recognised!","none","none")

choice_roomone_collected_key = Choice("What would you like to do? [Look], [Move], [Use] or [Collect].","Which direction would you like to move? [North], [South] or [West]?","Command not recognised!",
                          "Which direction would you like to move? [North], [South] or [West]?",
                          "What would you like to use the key on? [North Door] or [West Door]?")

choice_roomthree = Choice("What would you like to do? [Look], [Move], [Use] or [Collect].","What would you like to use the key on? [North Door] or [West Door]?","Command not recognised!","You don't have a key to use!.","")

choice_roomfour = Choice("Would you like to exit the dungeon? [Yes] or [No]?","Which direction would you like to move? [South]?","Command not recognised!","","")
#creating an instance of the Treasure class
trasure_roomthree = Treasure("The chest is unlocked! Inside is a bag of gold coins and a helmet.","the bookcase contains a pamphlet showing a map of this room")
#player inventory, this dictionary stores the players items.
inventory = {"coin": 0, "key": 0, "helmet": 0}

#player input funtion
def player():
    player.inp = input("> ")

#starts the first function loop the game towards the endgame.
print(roomone.look())
def firstroom():
    while True:
        print(choice_roomone.whattodo())
        player()
        if player.inp.lower() == "look":
            print(roomone.look())
            return firstroom()
        elif player.inp.lower() == "move":
            print(choice_roomone.direction())
            player()
            if player.inp.lower() == "north":
                print(roomone.north())
                return firstroom()
            elif player.inp.lower() == "south":
                print(roomone.south())
                return firstroom()
            elif player.inp.lower() == "west":
                print(roomone.west())
                return secondroom()
            else:
                print(choice_roomone.unknown())
                return firstroom()
        elif player.inp.lower() == "use":
            print(roomone.use())
            return firstroom()
        elif player.inp.lower() == "collect":
            print(roomone.collect())
            return firstroom()
        else:
            print(choice_roomone.unknown())
            return firstroom()
#from the start this is the room to the west
def secondroom():
    while True:
        print(choice_roomtwo.whattodo())
        player()
        if player.inp.lower() == "look":
            print(roomtwo.look())
            return secondroom()
        elif player.inp.lower() == "collect":
            print(roomtwo.collect())
            player()
            if player.inp.lower() == "coin":
                if inventory['coin'] >= 1:
                    print("coin already taken")
                    return secondroom()
                elif inventory["coin"] == 0:
                    inventory['coin'] = 1
                    print("You have collected",inventory['coin'],"coin and it is now in your inventory")
                    print("You take the coin. You now have",inventory['coin'],"Gold Piece")
                    return secondroom()
                else:
                    print(choice_roomtwo.unknown())
                    return secondroom()
            elif player.inp.lower() == "key":
                if inventory['key'] >= 1:
                    print("You already have collected the key.")
                    return secondroom()
                elif inventory['key'] == 0:
                    print("You are now holding the key")
                    inventory['key'] = 1
                    print("You have",inventory['key'],"Key")
                    return secondroom()
                else:
                    print(choice_roomtwo.unknown())
                    return secondroom()
            elif player.inp.lower() == "inventory":
                print(inventory['coin'], inventory['key'], sep="\n")
            else:
                    print(choice_roomtwo.unknown())
                    return secondroom()
        elif player.inp.lower() == "move":
            print(choice_roomtwo.direction())
            player()
            if player.inp.lower() == "east":
                return firstroom_collected_key()
            elif player.inp.lower() == "go back":
                return secondroom()
            else:
                print(choice_roomtwo.unknown())
                return secondroom()
        elif player.inp.lower() == "use":
            print(roomtwo.use())
            return secondroom()
        else:
            print(choice_roomtwo.unknown())
            return secondroom()
#to enter the third room from the start
def firstroom_collected_key():
    while True:
        print(roomone_collected_key.look(), choice_roomone_collected_key.whattodo(), sep="\n")
        player()
        if player.inp.lower() == "use":
            if inventory['key'] >= 1:
                print(roomone_collected_key.use())
                player()
                if player.inp.lower() == "key":
                    print(choice_roomone_collected_key.room_decision())
                    player()
                    if player.inp.lower() == "west door":
                        print(roomone_collected_key.west())
                        return firstroom_collected_key()
                    elif player.inp.lower() == "north door":
                        print(roomone_collected_key.north(), choice_roomone_collected_key.whattodo(), sep="\n")
                        player()
                        if player.inp.lower() == "move":
                            print(choice_roomone_collected_key.direction())
                            player()
                            if player.inp.lower() == "north":
                                return thirdroom()
            else:
                print(choice_roomone_collected_key.direction_nokey())
                return firstroom_collected_key()
        elif player.inp.lower() == "move":
            print(choice_roomone.direction())
            player()
            if player.inp.lower() == "north":
                if inventory['key'] >= 1:
                    print("Use the key you collected to open the door")
                    return firstroom_collected_key()
                elif inventory['key'] == 0:
                    print(roomone.north())
                    return firstroom()
            elif player.inp.lower() == "south":
                print(roomone.south())
                return firstroom()
            elif player.inp.lower() == "east":
                return firstroom()
#third room north to the east
def thirdroom():
    print(roomthree.look(), choice_roomthree.whattodo(), sep="\n")
    player()
    if player.inp.lower() == "collect":
        print(roomthree.collect())
        return thirdroom()
    elif player.inp.lower() == "look":
        print(roomthree.look())
        return thirdroom()
    elif player.inp.lower() == "use":
        print(roomthree.use())
        player()
        if player.inp.lower() == "chest":
            print(trasure_roomthree.chest(), choice_roomthree.whattodo(), sep="\n")
            return thirdroom_collect()
            
        elif player.inp.lower() == "bookcase":
            print(trasure_roomthree.bookcase())
            return thirdroom_collect()
        else:
            print(choice_roomthree.unknown())
            return thirdroom_collect()
    elif player.inp.lower() == "move":
        print(choice_roomfour.direction())
        player()
        if player.inp.lower() == "south":
            return southroom()
        else:
            print(choice_roomthree.unknown())
            return thirdroom()
    else:
        print(choice_roomthree.unknown())
        return thirdroom()

#collect code part of the room four. helps me with keeping the code easily accessible and make changes.
def thirdroom_collect():
    player()
    if player.inp.lower() == "collect":
        print("What would you like to collect? The [Bag] or the [Helmet]?")
        player()   
        if player.inp.lower() == "bag":
            if inventory['coin'] >= 10:
                print("You already have collected the Bag containing 10 coins.")
                print(inventory['coin'])
                print(choice_roomthree.whattodo())
                player()
                if player.inp.lower() == "move":
                    print(choice_roomthree.direction())
                    player()
                    if player.inp.lower() == "south":
                        return southroom()
            else:
                print("You take the bag. It contains 10 Gold Pieces.")
                inventory['coin'] += 10
                print(inventory)
                return thirdroom()
        elif player.inp.lower() == "helmet":
            if inventory['helmet'] >= 1:
                print("You already have collected the helmet")
                print(inventory['helmet'])
                return thirdroom()
            else:
                print("You take the helmet")
                inventory['helmet'] = 1
                return thirdroom_collect()
        else:
            print(choice_roomthree.unknown())
            return thirdroom_collect()
    elif player.inp.lower() == "move":
        print(choice_roomfour.direction())
        player()
        if player.inp.lower() == "south":
            return southroom()
        else:
            print(choice_roomthree.unknown())
            return thirdroom()
    elif player.inp.lower() == "go back" or "back":
        return thirdroom()
    elif player.inp.lower() == "inventory" or "inv":
        print(inventory)
        return thirdroom_collect()
    else:
        print(choice_roomthree.unknown())
        return thirdroom_collect()

def southroom():
    print(choice_roomfour.whattodo())
    player()
    if player.inp.lower() == "yes":
        print("Congratulations, you have escaped the dungeon with",inventory['coin'],"Gold Pieces.")                

#this is the function that executes the game.
firstroom()