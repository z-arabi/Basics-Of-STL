import re
from league import Team, Match, Weeks, League

def read_data(name,year):
    with open(name,'r') as f:
        lines = f.readlines()
    
    for line in lines:
            if 'table' and '[' and ']' in line:
                table = line
    
    teams = re.findall(r'\w+', table)[1:]
    print(teams)
    for i in range(len(teams)):
        teams[i] = Team(teams[i])
    print(teams)
    leag = League(teams,year)
    weeks = {}
    matches =[]

    for line in lines:
        m = re.search(r'week\s*(\d+)\s*:(\s*\w+\s*\d+\s*-\s*\d+\s*\w+)',line)
        if (m):
            matches.append(Match(m[2]))
            print(m[1] , '------' , m[2])
            print(matches)
            if(m[1] not in weeks.keys()):
                print("need to create")
                weeks[m[1]]=Weeks(m[1])
            weeks[m[1]].add_match(matches[len(matches)-1])
            # print(matches[len(matches)-1])
            # print(weeks[m[1]])

    for week in weeks.values():
        leag.add_week(week)

    return leag
            
                