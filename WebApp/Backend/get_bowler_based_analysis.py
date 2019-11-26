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

data_delivery = pd.read_csv('bowler_based_analysis.csv')

team1=sys.argv[1]
team2=sys.argv[2]

rslt_df = data_delivery.loc[(
                                (data_delivery['Team1'].map(lambda x: (x)==team1))
                            ) 
                            & (
                                (data_delivery['Team2'].map(lambda x: (x)==team2))
                            )]

if(rslt_df.empty):
    print('0 0')
else:
    print(str(rslt_df["Inning_1"].item())+" "+str(rslt_df["inning_2"].item()))