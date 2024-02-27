import random
import sys

sys.setrecursionlimit(100000)

rooms = {
    #name: [entertext, enemycount, doorcount, danger, special, nextpossbiledifficulties]
    #specials: 0(nothing), 1(wet), 2(long), 3(healing room)
    'start': ['You come to 2 doors.', 0, 2, 0, 0, [0, 1]],
    'hallwayS': ['You come to a long hallway with one door at the end of it', 0, 1, 0, 2,[1,2]],
    'damproom': ['You enter a damp room with 3 doors', 0, 3, 1, 1, [1,2]],
    '1enemyroom': ['you enter a room with 1 enemy and 2 doors', 1, 2, 2, 0, [1]],
    '2enemyroom': ['you enter a room with 2 enemies and 2 doors', 2, 2, 2, 0, [0,1]],
    'prechaosroom': ['You enter a peacefull room with one door at the end', 0, 1, 1, 0, [3]],
    'chaosroom': ['you enter a room with 6 enemies and 8 doors, the room is wet', 6, 8, 3, 1, [0, 1]],
    'healroom': ['you enter a room with a fountain in the middle', 0, 3, 2, 3, [0, 1,2]]
    

    
}
specroomexpl = ['', 'The room is wet, electric effects will hurt you', 'The room is long, in order to cross it, you need to press enter atleast once.','you feel refreshed']
name = ''
possiblerooms = []
nextroom = []
playereffects = []
playerstats = [10,0, 1]




def die():
    print('you have died! you survived',playerstats[1], 'rooms!')
    quit()

def takeanswer(question, possibleanswers):
    if playerstats[0] <= 0:
        die()
    test = '-1000'
    passed = False
    while passed == False:
        try:
            test = input(question)
            while int(test) not in possibleanswers:
                test = input(question)
            else:
                return(test)
        except:
            match test:
                case 'me':
                    print(playereffects, playerstats)
                case 'test':
                    pass
                case _:
                    pass
                
            
    

    




def doors(roomkey):
    if playerstats[0] <= 0:
        die()
    doorl = []
    dooropt = []
    for i in range(0, rooms[roomkey][2]):
        doorl.append(rooms[roomkey][5][random.randint(0, len(rooms[roomkey][5])-1)])
#        print(doorl)
        if not 1 in dooropt:
            dooropt.append(1)
        else:
            dooropt.append(len(dooropt)+1)
    print(dooropt)
    cdoor = takeanswer('please pick a door to go, you have '+str(rooms[roomkey][2])+' choices.', dooropt)
    enter(doorl[int(cdoor)-1])
    
def enemr(enemycount, roomkey):
    if playerstats[0] <= 0:
        die()
    tempansw = takeanswer("there are "+str(enemycount)+" enemies, either type one of their numbers to attack or type 0 to try and run past", list(range(0,int(enemycount)+1)))
    if int(tempansw) == 0:
        print("you run past the enemies")
        if random.randrange(0,2*playerstats[2]) == 1:
            playerstats[0]-=enemycount
            print("You take",enemycount,'damage')
        doors(roomkey)
    else:
        enemycount -= 1
        if random.randrange(0,2*playerstats[2]) == 1 and enemycount > 0:
            playerstats[0]-=enemycount
            print("You take",enemycount,'damage')
        if enemycount <= 0:
            doors(roomkey)
        enemr(enemycount, roomkey)
def specr(speceffect, roomkey):
    if playerstats[0] <= 0:
        die()
    print(specroomexpl[rooms[roomkey][4]])
#    print(speceffect)
    match speceffect:
        case 1:
            if "Electrified" in playereffects:
                playereffects[0] -= 1
            doors(roomkey)
        case 2:
            input("Type anything to move forward")
            doors(roomkey)
        case 3:
            healthplus = random.randrange(1,3)
            playerstats[0]+= healthplus
            print("you gained",healthplus,'health')
            doors(roomkey)
            
            

def enter(threat):
    if playerstats[0] <= 0:
        die()
    for i in rooms:
        if rooms[i][3] == int(threat):
            possiblerooms.append(i)
#    print(threat, possiblerooms)
    playerstats[1] += 1
    nextroom = possiblerooms[random.randint(0, len(possiblerooms)-1)]
    possiblerooms.clear()
    print(rooms[nextroom][0])
    if rooms[nextroom][1] != 0:
        enemr(rooms[nextroom][1], nextroom)
    elif rooms[nextroom][4] != 0:
        specr(rooms[nextroom][4], nextroom)
    else:
        doors(nextroom)
        


def main():
    print("Welcome to the dungeon, whenever you enter a room you will be given a set of choices:\nIf there are enemies, you can type the number of the enemy to hit it\n[You enter a room, it has 2 enemies: 1 : you hit the first enemy]\nIf the room has a shop you can eitehr type in the number of the item you want to purchase or leave to leave\nIf you come to a set of doors you can type a number to choose one to enter.\n\ntype in your username and press enter to begin!")
    name = input()
    if name == 'izutsumi' or name == 'izu':
        playerstats[0] = 3
        playerstats[2] = 3 #dodge multiplier
        print("wow im a big fan")
    elif name == 'ttk' or name == 'charlie':
        playerstats[0] = 100
        playerstats[2] = 100
        print('not even a struggle but ok') 
    elif name == 'hard':
        playerstats[0],playerstats[2] = 1,1
    print('hello',name)
    enter(0)
    
    
    

    
    
main()