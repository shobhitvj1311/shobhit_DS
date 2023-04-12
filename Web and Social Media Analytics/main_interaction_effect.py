# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:32:12 2023

@author: Dell
"""

from google.colab import files
#upload the data file
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['ad_test2.csv'].decode('utf-8')))
print(df)

#Import libraries for anova
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Website is making changes on three aspects- font, background color and button
#Which change is likely to drive conversions is the question?
#So ols is first used to fit the data and then anova is used to evaluate statistical signifance of the overall fit of OLS regression model.

#main effect 
model = ols("Conversion_rate ~ C(Font,Sum) + C(Backgroundcolor, Sum) + C(Click_button,Sum)",data=df).fit()
aov_table = sm.stats.anova_lm(model,typ=3)

print (aov_table)

print (aov_table.round(3))
#after executing I found that font and click button are significant (5% significance)

#now interaction effect - model 2
#interaction effect is useful in determining if there is a significant change in conversion rate due to combination of multiple independent variables/independent variables with some covariate
model2 = ols("Conversion_rate ~ C(Font,Sum) + C(Backgroundcolor,Sum) + C(Click_button,Sum) + C(Font,Sum):C(Backgroundcolor,Sum) + C(Font,Sum):C(Click_button,Sum) + C(Click_button,Sum):C(Backgroundcolor,Sum) + C(Font,Sum):C(Click_button,Sum):C(Backgroundcolor,Sum)",data=df).fit()
#after executing, only font and click button interaction are found to be significant enough

aov_table2=sm.stats.anova_lm(model2,typ=3)
print(aov_table2.round(3))


