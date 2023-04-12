# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 02:48:34 2023

@author: Dell
"""
#Problem statement which is a case cannot be attached since it will violate copyright issues.
from google.colab import files
#upload the data file
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['RestaurantGrades.csv'].decode('utf-8')))
print(df)

#Import libraries for anova
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Although reservations is considered the most likely candidate for dependent variable since it represents purchase,
#Still it makes sense to check for pageviews, calls for being dependent variables since different people use different ways to book/purchase in a restaurant.
#treatment remains independent variables (treatment groups are the ones where changes are tested)
#main effect
model = ols("pageviews ~ C(treatment,Sum)",data=df).fit()
aov_table = sm.stats.anova_lm(model,typ=3)
print (aov_table)

pd.options.display.float_format='{:,.2f}'.format
print(aov_table)

#main effect
model = ols("reservations ~ C(treatment,Sum)",data=df).fit()
aov_table = sm.stats.anova_lm(model,typ=3)
print (aov_table)

#main effect
model = ols("calls ~ C(treatment,Sum)",data=df).fit()
aov_table = sm.stats.anova_lm(model,typ=3)
print (aov_table)

#treatment is significant in all three above cases

#interaction effect
#Treatment group's interaction with covariate (restaurant type) is tested
model2 = ols("pageviews ~ C(treatment,Sum) + C(restaurant_type,Sum) + C(treatment,Sum):C(restaurant_type,Sum)",data=df).fit()
aov_table2=sm.stats.anova_lm(model2,typ=3)
print(aov_table2.round(3))

model2 = ols("reservations ~ C(treatment,Sum) + C(restaurant_type,Sum) + C(treatment,Sum):C(restaurant_type,Sum)",data=df).fit()
aov_table2=sm.stats.anova_lm(model2,typ=3)
print(aov_table2.round(3))

model2 = ols("calls ~ C(treatment,Sum) + C(restaurant_type,Sum) + C(treatment,Sum):C(restaurant_type,Sum)",data=df).fit()
aov_table2=sm.stats.anova_lm(model2,typ=3)
print(aov_table2.round(3))

#all are significant which means that the new layout of website would generate more pageviews, reservations and calls.
