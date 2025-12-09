import random
def rolls():
    num = int(input('Enter number of players '))

    while True:
        if num <= 2:
            num = int(input('Enter number of players '))

        else:
            break
    players = {}

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

    sum = 0

    temp = {}
    naam = []
    kaam = []
    num = num - 1
    for i in range(0, num + 1):
        name = input('Enter player name ')
        players.update({name: ""})

    player = list(players.keys())
    for p in player:
        if p not in t_kaam.keys():
            t_kaam.update({p: ''})




    con = True
    while con:



        while con:
            random.shuffle(player)
            print("start")
            for i in range(0, num + 1):
                val = players[player[i]]
                ch = choice[i]+val+" "
                players.update({player[i]: ch })

                if(i==1):
                 print(f"{player[i]} is police please enter you friend name who you think he/she might be chor")
                if(ch=="chor " or ch == "police "):
                    temp.update({player[i]: ch})


                tempo = list(temp.keys())




                if i==num:

                    for j in tempo:

                        if(players[j] == 'chor ' or players[j] == 'police '):
                            naam.append(j)
                            kaam.append(temp[j])
                        if(kaam == ['chor ', 'police ']):
                            print(f'''select:''')
                            for k in player:

                                if(players[k] == 'police '):
                                    continue
                                else:

                                    print(f'player : {k}')
                            choose = []
                            while True:
                                choose.append(input('Enter your choice '))
                                print(choose)
                                print(player)
                                while True:
                                    if choose[0] in player:
                                        print(choose)
                                        print(player)
                                        break
                                    else:
                                        print(choose)

                                        choose.clear()

                                print("you choose ",players[choose[0]])


                                if (players[choose[0]] == players[naam[0]]):
                                    choose.clear()

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


            temp.clear()

            for p in player:

                if p in t_kaam.keys():
                    t_kaam[p] = t_kaam[p] + players[p]

            kaam.clear()
            naam.clear()
            choose.clear()
            for z in players.keys():
                players[z] = ''
            # random.shuffle(player)
            v = input("Press e to 'exit' ")
            if(v == 'e'):
                con = False
                con = False

    final_naam = list(t_kaam.keys())
    final_kaam = []
    a=[]
    for i in players.keys():
        final_kaam.append(t_kaam[i])

        final_kaam[0].rstrip()
        a = final_kaam[0].split(' ')
        a.pop(-1)
        for j in a:
            sum += roll[j]
        print(f"the score of {i} is {sum}")
        sum = 0

        a.clear()
        final_kaam.clear()



rolls()

