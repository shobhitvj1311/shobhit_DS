# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:47:55 2023

@author: Dell
"""

from google.colab import files
uploaded = files.upload()

import io
import pandas as pd
#Encoding ISO and 'cp1252' works for the review text as it has special characters
review_file = pd.read_csv(io.StringIO(uploaded['car.csv'].decode('ISO-8859-1')))
#Print the first few rows
print(review_file.head(2))

#Create a new dataframe to store comment and sentiment
df_new=pd.DataFrame()

#!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sent_obj = SentimentIntensityAnalyzer()   

#Loop throught the entire data frame to get the review column
for ind in review_file.index:
    comment=review_file['Review Text'][ind]
    print(comment)
    comment_sentiment=sent_obj.polarity_scores(comment) 
    print("Overall sentiment  ", comment_sentiment['compound'])
    aspect=review_file['Aspect'][ind]
    print(aspect)
    #Store the category, comment and the sentiment in a new row
    newrow= {'Aspect':aspect,'Review text':comment,'Sentiment': comment_sentiment['compound']}
    #Copy the row to a new file
    df_new = pd.concat([df_new, pd.DataFrame([newrow])], ignore_index=True)
    
#Check the newly created df. This has the sentiment
print(df_new.head(1))

print(df_new.columns)

#Plot Average sentiment based on the category i.e. product attribute
df_new.groupby(['Aspect']).mean("Sentiment").plot(legend=True)

#Store the results

df_new.to_csv('car-sentiment.csv', index=False)
#Download the files locally
files.download("car-sentiment.csv")

#now the data is filtered based on aspects because of which there is a positive sentiment. These aspects were- driving and performance.

from google.colab import files
uploaded = files.upload()

import io
import pandas as pd
df_neg = pd.read_excel(io.BytesIO(uploaded['car_highsentiment.xlsx']))
#Print the first few rows
print(df_neg.head(2))

print(len(df_neg))

#concat all reviews together
total_neg_reviews = "".join(text for text in df_neg.text)
#print(len(total_neg_reviews))
print(type(total_neg_reviews))

from wordcloud import WordCloud

wordcloud = WordCloud(background_color="SALMON").generate(total_neg_reviews)
import matplotlib.pyplot as plt
# Display the generated image:
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#stopwords
from wordcloud import WordCloud, STOPWORDS
print(type(STOPWORDS))
print (STOPWORDS)

custom_stop_words=["x27"]+list(STOPWORDS)
wordcloud=WordCloud(background_color="SALMON",stopwords=custom_stop_words).generate(total_neg_reviews)
import matplotlib.pyplot as pit
#display the generated image
#the matplotlib way:
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
#High sentiments are due to good mileage, engine, interior, and good transmission. Mileage and engine being the biggest factors.


#Likewise for negative reviews
custom_stop_words=["x27", "car", "vehicle", "Ford", "Nissan", "buy"]+list(STOPWORDS)
wordcloud=WordCloud(background_color="SALMON",stopwords=custom_stop_words).generate(total_neg_reviews)
import matplotlib.pyplot as pit
#display the generated image
#the matplotlib way:
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
#Negative sentiments are due to cost, maintenance, service and warranty(could be warranty for some parts).

