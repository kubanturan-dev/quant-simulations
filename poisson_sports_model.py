import numpy as np
import matplotlib.pyplot as plt
def main():
    def func1():
        global teams,attackpoint,defencepoint
        teams=np.array([['Galatasaray '],['Fenerbahçe '],['Beşiktaş '],['Trabzonspor '],['Başakşehir '],['Sivasspor '],['Alanyaspor '],['Konyaspor '],['Gaziantep '],['FKAntalyaspor ']])
        attackpoint=np.array(np.random.randint(50,101,10))
        defencepoint=np.array(np.random.randint(50,101,10))
    func1()
    def func2():
        global games
        teams1=teams.reshape(1,10)
        games=np.char.add(teams,teams1)
        np.fill_diagonal(games,'')
        print(games)
    func2()
    def func3():
        defencepoint1=defencepoint.reshape(10,1)
        attackpoint1=attackpoint.reshape(10,1)
        away_goals=attackpoint-defencepoint1
        home_goals=attackpoint1-defencepoint  
        home_goals= np.divide(home_goals,20)
        home_goals=np.add(home_goals,2.5)
        away_goals= np.divide(away_goals,20)
        away_goals=np.add(away_goals,2.5)
        away_goals1=np.random.poisson(away_goals)
        home_goals1=np.random.poisson(home_goals) 
        home_wins=home_goals1>away_goals1
        away_wins=away_goals1>home_goals1
        draws=home_wins==away_wins
        homepoint=(home_wins*3)+(draws*1)
        awaypoint=(away_wins*3)+(draws*1)
        total_home_points=np.sum(homepoint, axis=1)
        total_away_points=np.sum(awaypoint, axis=0)
        total_points = total_home_points + total_away_points   
    func3()
main()
        
        
            
            
            
            

        
