# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:07:58 2023

@author: Dell
"""

from google.colab import files
uploaded = files.upload()

import io
import pandas as pd
#Encoding ISO and 'cp1252' works for the review text as it has special characters
review_file = pd.read_csv(io.StringIO(uploaded['redmi6.csv'].decode('ISO-8859-1')))
#Print the first few rows
print(review_file.head(2))

#Create a new dataframe to store comment and sentiment
df_new=pd.DataFrame()

#!pip install vaderSentiment (install library by using suitable command, in colab it works like this)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sent_obj = SentimentIntensityAnalyzer()

#Loop throught the entire data frame to get the review column
for ind in review_file.index:
    comment=review_file['Comments'][ind]
    print(comment)
    comment_sentiment=sent_obj.polarity_scores(comment) 
    print("Overall sentiment  ", comment_sentiment['compound'])
    category=review_file['Category'][ind]
    print(category)
    #Store the category, comment and the sentiment in a new row
    newrow= {'Comment':comment, 'Category':category ,'Sentiment': comment_sentiment['compound']}
    #Copy the row to a new file
    df_new = pd.concat([df_new, pd.DataFrame([newrow])], ignore_index=True)
    
#Check the newly created df. This has the sentiment
print(df_new.head(1))

print(df_new.columns)

#Plot Average sentiment based on the category i.e. product attribute
df_new.groupby(['Category']).mean("Sentiment").plot(legend=True)

#Higher sentiment scores are driven by battery and display whereas lowest ones are driven by camera and others(aspect)

#Store the results

df_new.to_csv('redmi-sentiment.csv', index=False)
#Download the files locally
files.download("redmi-sentiment.csv")