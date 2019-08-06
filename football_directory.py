import requests
league = []
teams = []


def next_fixtures(x):
    urls = 'https://www.thesportsdb.com/api/v1/json/1/eventsnext.php?id=' + x
    data_f = requests.get(urls)
    fixtures = data_f.json()['events']
    for item in fixtures:
        print (item['dateEvent'], '---', item['strEvent'],'---', item['strLeague'])

def last_fixtures(x):
    urls = 'https://www.thesportsdb.com/api/v1/json/1/eventslast.php?id=' + x
    data_f = requests.get(urls)
    fixtures = data_f.json()['results']
    for item in fixtures:
        print (item['dateEvent'],'---',item['strEvent'],'({}-{})'.format(item['intHomeScore'],item['intAwayScore']),'---', item['strLeague'])

def all_players(x):
    urls = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=' + x
    data =  requests.get(urls)
    players = data.json()['player']
    for item in players:
        print(item['strNumber'],'---',item['strPlayer'])

def tablex (x,z):
    season = int(input('Select Season :\n1. 2018/2019\n2. 2017/2018\n3. 2016/2017\n4. 2015/2016\n5. 2014/2015\nMenu : '))
    if season == 1:
        y = 1819
        a = ('League Table 2018/2019')
    elif season == 2:
        y = 1718
        a = ('League Table 2017/2018')
    elif season == 3:
        y = 1617
        a = ('League Table 2016/2017')
    elif season == 4:
        y = 1516
        a = ('League Table 2015/2016')
    elif season == 5:
        y = 1415
        a = ('League Table 2014/2015')
    else:
        print('Please enter correctly!')
        tablex(league[-1],teams[-1])
    urls = 'https://www.thesportsdb.com/api/v1/json/1/lookuptable.php?l=' +x +'&s=' +str(y)
    data = requests.get(urls)
    table = data.json()['table']
    print(a)
    for loop in range (len(table)):
        if loop < 9:
            a = 24
        else:
            a = 23
        b = ''
        for loop1 in range (a - len(table[loop]['name'])):
            b += '-'
        if table[loop]['teamid'] == z:
            print('{}.'.format(loop+1),table[loop]['name'],b,table[loop]['played'],'--',table[loop]['win'],'-',table[loop]['draw'],'-',table[loop]['loss'],'---',table[loop]['goalsfor'],'-',table[loop]['goalsagainst'],'--',table[loop]['goalsdifference'],'---',table[loop]['total'],'(Your Team)')
        else:
            print('{}.'.format(loop+1),table[loop]['name'],b,table[loop]['played'],'--',table[loop]['win'],'-',table[loop]['draw'],'-',table[loop]['loss'],'---',table[loop]['goalsfor'],'-',table[loop]['goalsagainst'],'--',table[loop]['goalsdifference'],'---',table[loop]['total'])
    return
    
def mainmenu():
    menu = True
    team = input('\nWelcome to Sport Directory Data (beta version)\nChoose Your Team : ') 
    while (menu < 6):
        url = 'https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=' + team.lower()
        data = requests.get(url)
        

        if type(data.json()['teams']) == type([]):
            menu = int(input('Menu :\n1. Next 5 Fixtures \n2. Last 5 Fixtures\n3. All Player\n4. League Table \n5. Change Team\n6. Exit\nMenu : '))
            data_team = data.json()['teams'][0]
            league.append(data_team['idLeague'])
            teams.append(data_team['idTeam'])

            if menu == 1:
                next_fixtures(data_team['idTeam'])
            elif menu == 2:
                last_fixtures(data_team['idTeam']) 
            elif menu == 3:
                all_players(data_team['strTeam'])
            elif menu == 4:
                tablex(data_team['idLeague'],data_team['idTeam'])
            elif menu == 5:
                mainmenu()
            elif menu == 6:
                print('Thank You!')
                break
            else:
                print('Please enter correctly!')
                mainmenu()
        else:
            print('Sorry, your club data are not avalaible or you are not type it correctly!')
            mainmenu()

mainmenu()