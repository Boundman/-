import datetime
import requests
from get_friends import *
from id_from_username import *

def make_diagram(friends):
    diagramma = {}

    for friend in friends:
        date_birth = friend['bdate']
        date = datetime.datetime.strptime(date_birth, '%d.%m.%Y')
        years = int((datetime.datetime.now() - date).days/365.25)

        if years in diagramma:
            diagramma[years] += 1
        else:
            diagramma[years] = 1
    return diagramma

def draw_diagram(diagramma):
    for i in diagramma.keys():
        print(i, ":", diagramma[i]*'#')

def operate_with_id(id):
    friends_norm = []
    
    x = getFriends(id)
    try:
        friends = x.execute().json()['response']
    except KeyError:
        print('Incorrect id or username')
    else:
        for friend in friends:
            if 'bdate' in friend:
                if len(friend['bdate'].split('.')) > 2:
                    friends_norm.append(friend)
            
        diagramma = make_diagram(friends_norm)
        draw_diagram(diagramma)

def operate_with_username(username):
    x = getId(username)
    user = x.execute()
    try:
        user = user.json()['response']
    except KeyError:
        print('Incorrect id or username')
    else:
        id = user[0]['uid']
        operate_with_id(id)
    

if __name__ == '__main__':
    id_username = input("Введите ID пользователя или Username: ")

    if id_username.isdigit():
        id = int(id_username)
        operate_with_id(id)        
    else:
        username = id_username
        operate_with_username(username)
        
