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


def team_team_info(team1, team2, year):
    import pandas as pd
    path = "Data/%s.csv"%(year)
    data = pd.read_csv(path)
    team1 = data[team1]
    team2 = data[team2]
   
    teams = pd.concat([team1, team2], axis = 1)
    teams = teams.fillna('Player Name')
   
    return teams
df_team_players=team_team_info(sys.argv[1],sys.argv[2],sys.argv[3])
df_team_players.to_csv("team_players.csv")

print("Output from get_team_players") 
print("Team 1: " + sys.argv[1]) 
print("Team 2: " + sys.argv[2]) 
print("Season: " + sys.argv[3])