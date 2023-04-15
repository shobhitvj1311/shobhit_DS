# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:38:54 2023

@author: Dell
"""

from google.colab import files
uploaded = files.upload()

import io
import pandas as pd

import io
import pandas as pd
#negative-iskon contains data (reviews) which have negative sentiment.
#The objective is to obtain a wordcloud from negative reviews and find possible reasons for devotees' dissatisfaction
df_neg = pd.read_excel(io.BytesIO(uploaded['negative-iskon.xlsx']))
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

custom_stop_words=["place", "will", "temple", "good","go","people","visited", "many", "God","visit","iskcon","Krishna","one","inside","thing"]+list(STOPWORDS)
wordcloud=WordCloud(background_color="SALMON",stopwords=custom_stop_words).generate(total_neg_reviews)
import matplotlib.pyplot as pit
#display the generated image
#the matplotlib way:
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#The words which came out bigger were- commercial, shop, money, business etc. which indicate as if the iskcon has become a business in the eyes of devotees.
#Lot of commercial stuff could be visible within temple's premises and lot of money might be involved. All these thing might not actually be true,
#but just reflect the sentiments/perceptions of the devotees.