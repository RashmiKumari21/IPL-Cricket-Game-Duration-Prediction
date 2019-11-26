import sys 
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from scipy.stats import norm, entropy 
from scipy.stats import probplot
import matplotlib.pyplot as plt
from scipy.stats import logistic
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.utils import resample
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix, roc_curve
from sklearn.preprocessing import Imputer

##################################################################
#  use avg_balls_played.csv to create team_avg_balls_played.csv
##################################################################

#reading the complete file with players and their average balls played
df = pd.read_csv('avg_balls_played.csv')
df=df.rename(columns={"Unnamed: 0":"Player"})

#reading team player names
df_teamInfo = pd.read_csv('team_players.csv').drop(columns="Unnamed: 0")

#processing to get arrays with avaerage blass for both teams
arry=[]
totalBallsTeam1=0
totalBallsTeam2=0

#pushing values of players in an array arry
for i in df_teamInfo.columns:
    # print(i)
    arry.append(df_teamInfo[i].values)

#storing player names and avg balls in two different arrays   
all_players=df.Player.values
all_balls=df.Avg_Balls.values

# print("1--",all_players[0:10],"\n",arry)

def name(s): 
  
    # split the string into a list  
    l = s.split() 
    new = "" 
  
    # traverse in the list  
    for i in range(len(l)-1): 
        s = l[i]   
        # adds the capital first character  
        new += (s[0].upper())       
    # l[-1] gives last item of list l. We 
    # use title to print first character in 
    # capital. 
    new += l[-1].title()   
    return new 

new_name_arry0=[]
for i in arry[0]:
    new_name_arry0.append(name(i))
    
new_name_arry1=[]    
for i in arry[1]:
    new_name_arry1.append(name(i))
    
new_name_all_players=[]
for i in all_players:
    new_name_all_players.append(name(i))

# print("2---",new_name_arry)
    
team1_dict=[]
for i in range(len(new_name_arry0)): 
    if new_name_arry0[i] in new_name_all_players:
        team1_dict.append(all_balls[i])
    else:
        team1_dict.append(0)
        
team2_dict=[]
for i in range(len(new_name_arry1)): 
    if new_name_arry1[i] in new_name_all_players:
        team2_dict.append(all_balls[i])
    else:
        team2_dict.append(0)

# print("4--",team1_dict)
# print("5--",team2_dict)

# adding columns to dataframe
df_teamInfo["BallsTeam1"]=team1_dict
df_teamInfo["BallsTeam2"]=team2_dict

totalBallsTeam1=df_teamInfo["BallsTeam1"].sum()
totalBallsTeam2=df_teamInfo["BallsTeam2"].sum()

df_teamInfo["TotalBallsTeam1"]=totalBallsTeam1
df_teamInfo["TotalBallsTeam2"]=totalBallsTeam2


#creating CSV file
df_teamInfo.to_csv("team_avg_balls_played.csv")
# Takes first name and last name via command  
# line arguments and then display them 

print("Output from Python") 
print("Team 1: " + sys.argv[1]) 
print("Team 2: " + sys.argv[2]) 
print("Season: " + sys.argv[3]) 
print("Total Balls Team1: " + totalBallsTeam1)
print("Total Balls Team2: " + totalBallsTeam2)