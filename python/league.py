import copy 

class Match:
    def __init__(self,name):
        name_split = name.split()
        self.home = name_split[0]
        self.home_goals = int(name_split[1])
        self.away = name_split[4]
        self.away_goals = int(name_split[3])
        # print(f"{self.home}*{self.home_goals}*{self.away}*{self.away_goals}")

    def data(self):
        h_win = h_eq = h_lose = h_score = a_win = a_eq = a_lose = a_score = 0
        if (self.home_goals > self.away_goals):
            # print("winner")
            h_win = 1
            h_score = 3
            a_lose = 1
            a_score = 0
        elif (self.home_goals < self.away_goals):
            # print("loser")
            a_win = 1
            a_score = 3
            h_lose = 1
            h_score = 0
        elif (self.home_goals == self.away_goals):
            # print("equal")
            h_eq = 1
            h_score = 1
            a_eq = 1
            a_score = 1
        tup = ((1,h_win,h_eq,h_lose,self.home_goals,self.away_goals,self.home_goals-self.away_goals,h_score),
               (1,a_win,a_eq,a_lose,self.away_goals,self.home_goals,self.away_goals-self.home_goals,a_score))
        return tup

    def __str__(self):
        return f"{self.home} {self.home_goals} - {self.away_goals} {self.away} "
    
    def __repr__(self):
        return ("{} {} - {} {}".format(self.home,self.home_goals,self.away_goals,self.away))
         
class Weeks:
    
    def __init__(self,num,matches=None):
        self.num = num
        if matches == None:
            matches = []
        self.matches = matches
        # print(len(matches),len(self.matches))
        # for i in matches:
        #     print(i)
    
    def add_match(self,match):
        # print(len(self.matches))
        for game in self.matches:
            if(game.home == match.home or game.home == match.away or game.away == match.home or game.away == match.away):
                # print("equal teams")
                break
        else:
            # print('runs')
            self.matches.append(match)
    
    def __str__(self):
        for game in self.matches:
            print("{:>10} {} - {} {}".format(game.home,game.home_goals,game.away_goals,game.away))
        return ""

class Team:
    
    rank = 0
    def __init__(self,name):
        self.name = name
        Team.rank += 1
        self.rank = Team.rank
        self.mp = self.w = self.d = self.l = self.gf = self.ga = self.gd = self.pts = 0

    def add_match(self,match):
        tup = ()
        if (self.name == match.home):
            # print("mizban")
            tup = match.data()[0]
        elif (self.name == match.away):
            # print("mehman")
            tup = match.data()[1]
        else:
            # print("there is no profile for teams")
            tup = (0,0,0,0,0,0,0,0)

        tup_obj = (self.mp,self.w,self.d,self.l,self.gf,self.ga,self.gd,self.pts)
        self.mp,self.w,self.d,self.l,self.gf,self.ga,self.gd,self.pts = (sum(x) for x in zip(tup,tup_obj))

    def __str__(self):
        return f"{self.rank} {self.name} {self.mp} {self.w} {self.d} {self.l} {self.gf} {self.ga} {self.gd} {self.pts}"

class League:

    def __init__(self,tlist,year):
        self.year = year
        self.standing = tlist
        self.standing.sort(key=lambda x:x.rank) #sort output is NoneType!! && sort is Ascending based on rank
        middle = copy.deepcopy(self.standing)
        self.all_standing = [middle] #it passed by referance for lists
        # print(len(self.all_standing))
        # for i in self.all_standing[0]:
        #     print(i)
        self.all_weeks = []

    def __add_match(self,week):
        for game in week.matches:
            for team in self.standing:
                team.add_match(game)
                # print(game , game.data())
        standing_mid = copy.deepcopy(self.standing)
        self.standing.sort(key=lambda x:(x.pts,x.gd,x.gf,x.w),reverse=True)
        if(standing_mid == self.standing):   
            self.standing.sort(key=lambda x:x.name)
        for i,team in enumerate(self.standing):
            team.rank = i+1
        middle = copy.deepcopy(self.standing)
        self.all_standing.append(middle)
        # print(len(self.all_standing),'in add amtch')
        # for i in self.all_standing[0]:
        #     print(i)

    def add_week(self,week):
        self.all_weeks.append(week)
        self.__add_match(week)

    def __str__(self):
        print("#    team      mp   w    d    l    gf   ga   gd   pts  ")
        for team in self.standing:
            print("{:<5}{:<10}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}{:<5}"
                    .format(team.rank,team.name,team.mp,team.w,team.d,team.l,team.gf,team.ga,team.gd,team.pts))
        return ""

