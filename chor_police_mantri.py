import random
def rolls():
    num = int(input('Enter number of players '))
    players = {}
    t_naam = []
    t_kaam = {}
    roll = {
        "chor" : 0,
         "police" : 100,
         "raja" : 1000,
         "rani" : 800,
        "mantri" : 500,
        "sipahi" : 200,
        "nagarik" : 50,
        "aam_nagarik" : 25
    }
    choice = list(roll.keys())
    print(choice)
    sum = 0

    temp = {}
    naam = []
    kaam = []
    for i in range(0, num + 1):
        name = input('Enter player name ')
        players.update({name: ""})
    print(players)
    player = list(players.keys())
    for p in player:
        if p not in t_kaam.keys():
            t_kaam.update({p: ''})
            print(t_kaam[p], "is list1")



    con = True
    while con:

        print(choice)
        print(player,"suffled")

        while con:
            random.shuffle(player)
            print("start")
            for i in range(0, num + 1):
                val = players[player[i]]
                ch = choice[i]+val+" "
                players.update({player[i]: ch })
                print(f'here id there player: {players}')
                print(ch,' ch is here')
                if(i==1):
                 print(f"{player[i]} is police please enter you friend name who you think he/she might be chor")
                if(ch=="chor " or ch == "police "):
                    temp.update({player[i]: ch})

                print(players)
                tempo = list(temp.keys())
                print(f"{tempo} is tempo")
                print(f"{temp} is tempo")



                if i==num:
                    print(f" is bigto")
                    for j in tempo:
                        print(f"{j} is bigto")
                        print(f" is to")
                        if(players[j] == 'chor ' or players[j] == 'police '):
                            naam.append(j)
                            kaam.append(temp[j])
                        if(kaam == ['chor ', 'police ']):
                            print(f'''select:''')
                            for k in player:

                                if(players[k] == 'police '):
                                    continue
                                else:
                                    print(f'{players[k]}''')
                                    print(f'{k}')
                            choose = []
                            while True:
                                choose.append(input('Enter your choice '))
                                print(players[choose[0]], "is choose")
                                print(players[naam[0]], " is choose")

                                if (players[choose[0]] == players[naam[0]]):
                                    choose.clear()
                                    print("sussy")
                                    break

                                elif players[choose[0]] == players[naam[1]]:
                                    choose.clear()

                                else:
                                    players[naam[0]] = 'police '
                                    players[naam[1]] = 'chor '
                                    break

                            kaam.clear()
                            naam.clear()
                            choose.clear()




            for p in player:
                print(temp)
                if p in t_kaam.keys():
                    t_kaam[p] = t_kaam[p] + players[p]
            print(t_kaam)
            kaam.clear()
            naam.clear()
            choose.clear()
            for z in players.keys():
                players[z] = ''
            # random.shuffle(player)
            v = input("Enter your choice ")
            if(v == 'e'):
                con = False
                con = False



rolls()

