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

from pyspark.ml.recommendation import ALS
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.sql.session import SparkSession
import math
from sklearn import preprocessing
import json

column_names=["player","balls"]
data_delivery = pd.read_csv('team_avg_balls_played_SVD.csv')

batsman=sys.argv[1]
bowler=sys.argv[2]

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

batsman=name(batsman)
bowler=name(bowler)

rslt_df = data_delivery.loc[(
                                (data_delivery['Batsman'].map(lambda x: name(x)==batsman)) | 
                                (data_delivery['Batsman'].map(lambda x: (x)==batsman))
                            ) 
                            & (
                                (data_delivery['Bowler'].map(lambda x: name(x)==bowler)) |
                                (data_delivery['Bowler'].map(lambda x: (x)==bowler))
                            )]


if(rslt_df.empty or rslt_df["balls"].isnull):
    print('0')
else:
    print(str(rslt_df["balls"].item()))