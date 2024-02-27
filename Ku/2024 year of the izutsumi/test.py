students = {
'435':{
    'vards': 'pēteris',
    'vecums': 16,
    'atzīme': 8
},
'234':{
    'vards': 'kaspars',
    'vecums': 12,
    'atzīme':7
},
'124':{
    'vards': 'gunta',
    'vecums': 14,
    'atzīme':9
},
'679':{
    'vards': 'Jēkabs',
    'vecums':15,
    'atzīme':9
},
'657':{
    'vards': 'Nikola',
    'vecums':13,
    'atzīme':5
}}


def get_age(student_data):
    return student_data[1]['vecums']
#sorted_students_by_age
sorted_students_by_age = dict(sorted(students.items(), key=get_age))




print('Sakartota vārdnīca pēc vecuma:')
for id, dati in sorted_students_by_age.items(): 
    print(f'ID:{id},Dati:  {dati}')