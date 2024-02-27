rooms = {
    #name: [entertext, enemycount, doorcount, danger, special, nextpossbiledifficulties]
    #specials: 0(nothing), 1(wet), 2(long)
    'start': ['You come to 2 doors.', 0, 2, 0, 0, [0, 1]],
    'hallwayS': ['You come to a long hallway with one door at the end of it', 0, 1, 0, 2,[1,2]],
    'damproom': ['You enter a damp room with 3 doors', 0, 3, 1, 1, [1,2]],
    '1enemyroom': ['you enter a room with 1 enemy and 2 doors', 1, 2, 2, 0, [1]],
    '2enemyroom': ['you enter a room with 2 enemies and 2 doors', 2, 2, 2, 0, [0,1]],
    'prechaosroom': ['You enter a peacefull room with one door at the end', 0, 1, 1, 0, [3]],
    'chaosroom': ['you enter a room with 6 enemies and 8 doors, the room is wet', 6, 8, 3, 1, [0, 1]]
}

students = {
    'izu': [17,3],
    'spm': [32,2],
    'chrl': [18,1]
      
}

students2 = {
    'izu': 17,
    'spm': 32,
    'chrl': 18
    
    
}

def selectxelement(element, elementx):
    return element[elementx]


print(dict(sorted(students.items())))
print(dict(sorted(students.items(), key=lambda item: item[1])))
print(dict(sorted(students.items(), key=lambda item: item[1][1])))


print(sorted(students, key=lambda student: student[1]))

print(sorted(rooms, key=lambda room: room[3]))