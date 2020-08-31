#!/usr/bin/env python
# coding: utf-8

# # Analysis of domestic violence, sexual assault, and indecency in NSW

# Python code to analyze domestic violence, sexual crimes and other acts of indecency in NSW based on data from the NSW Bureau of Crime Statistics and Research.

# # Loading libraries

# Let's load relevant Python libraries.

# In[1]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib as mpl
import warnings
warnings.filterwarnings("ignore")


# # Loading data

# The dataset was acquired from https://www.bocsar.nsw.gov.au/Pages/bocsar_datasets/Datasets-.aspx. 

# In[2]:


filename = 'DomesticViolenceStatistics.xlsx';
data = pd.ExcelFile(filename)


# Let's list the sheets

# In[3]:


data.sheet_names


# # Analysis of types of premises

# Let's analyze premises where domestic violence, sexual crimes and other acts of indecency in NSW occur.

# In[4]:


premises = pd.read_excel(filename, 'Premises type')
premises.head(15)


# In[5]:


premises.tail(15)


# The first 4 rows need to be skipped and the last 11 rows need to be dropped. ('Total' is also not necessary.)
# All the columns except Premise type and 'Domestic violence related assault

# In[6]:


premises = pd.read_excel(filename, 'Premises type', skiprows=4)
premises = premises.iloc[:-11, :]


# In[7]:


premises.head()


# In[8]:


premises.tail()


# We are only interested in three columns and 'Premise type'. Let's keep only these four and drop the rest. 'Premise type' should be marked as index.

# In[9]:


data_of_interest = ['Premise type', 'Domestic violence related assault','Sexual assault', 'Indecent assault, act of indecency and other sexual offences']
premises = premises[data_of_interest]
premises = premises.set_index('Premise type')
premises.head()


# In[10]:


premises.plot.bar(figsize=(15, 5))
plt.ylabel('Number of cases')
plt.grid(color='gray', linestyle='dotted', linewidth=0.3)


# We can see from the above picture that domestic violence related assults mostly occur at home. Let's lower the maximum value of the bar chart to zoom into other bars.

# In[11]:


premises.plot.bar(figsize=(15, 5))
plt.grid(color='gray', linestyle='dotted', linewidth=0.3)
plt.ylabel('Number of cases')
plt.ylim(0, 3000)


# We can see from the above picture that domestic violence related assults and sexual offences mostly occur at home. Outdoor places are the second most common type of places where domestic violence occurs.

# In[12]:


premises.plot.bar(figsize=(15, 5))
plt.grid(color='gray', linestyle='dotted', linewidth=0.3)
plt.ylabel('Number of cases')
plt.ylim(0, 1000)


# # Seasonality

# Let's analyze seasonal patterns of domestic violence, sexual crimes and other acts of indecency in NSW.

# In[13]:


seasonality = pd.read_excel(filename, 'Month')
seasonality.head()


# As before, the first four rows should be skipped because they are part of the explanation text in the Exel file.

# In[14]:


seasonality = pd.read_excel(filename, 'Month', skiprows=4)


# In[15]:


seasonality.head()


# Let's only keep the three rows that we are interested in analyzing.

# In[16]:


data_of_interest = ['Domestic violence related assault','Sexual assault', 'Indecent assault, act of indecency and other sexual offences']
seasonality = seasonality[seasonality['Offence type'].isin(data_of_interest)]
seasonality.head()


# There are a few things that need to be done:
# 1. The offence type has to be set as index
# 2. The table has to be transposed
# 3. The date column has to be parsed as datetime

# In[17]:


seasonality.rename(columns={"Offence type": ""}, inplace=True)
seasonality = seasonality.set_index('')
seasonality = seasonality.T
seasonality.index = pd.to_datetime(seasonality.index, infer_datetime_format=True)
seasonality.head()


# In[18]:


seasonality['Domestic violence related assault'].plot(kind = 'line', color='r', label='Domestic violence related assault',linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))
#plt.legend(bbox_to_anchor=(1.05, 1))     
plt.xlabel('')              
plt.ylabel('Number of cases')    
plt.title('Domestic violence related assault')
plt.show()    


seasonality['Sexual assault'].plot(kind = 'line', color='b', label='Sexual assault', linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))
#plt.legend(bbox_to_anchor=(1.05, 1))     
plt.xlabel('')              
plt.ylabel('Number of cases')     
plt.title('Sexual assault')
plt.show()    

seasonality['Indecent assault, act of indecency and other sexual offences'].plot(kind = 'line', color='g',label = 'Indecent assault, act of indecency and other sexual offences',linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))
#plt.legend(bbox_to_anchor=(1.05, 1))     
plt.xlabel('')              
plt.ylabel('Number of cases') 
plt.title('Indecent assault, act of indecency and other sexual offences')
plt.show()    


# Domestic violence and sexual assault seem to peak in January, coinciding with the holiday season. 'Indecent assault' does not seem to be influenced by season although it peaks in September. For more conclusive insights, more seasonal data from other years are necessary.

# # Alcohol related

# Let's analyze the effect of alcohol on domestic violence, sexual crimes and other acts of indecency in NSW.

# In[19]:


alcohol = pd.read_excel(filename, 'Alcohol related', skiprows=4)
alcohol.head()


# Let's correct the spelling on the 'Alcohol Related' column. We only need two columns and we can disgard the rest.

# In[20]:


alcohol.rename(columns={'Alcohol Related^':'Alcohol Related'}, inplace=True)
alcohol = alcohol[['Offence type','Alcohol Related','Not Alcohol Related']]
alcohol.head(10)


# In[21]:


data_of_interest = ['Domestic violence related assault','Sexual assault', 'Indecent assault, act of indecency and other sexual offences']
alcohol = alcohol[alcohol['Offence type'].isin(data_of_interest)]
alcohol.rename(columns={"Offence type": ""}, inplace=True)
alcohol = alcohol.set_index('')
alcohol = alcohol.T


# In[22]:


alcohol.head()


# Let's start analyzing.

# In[23]:


print("Domestic violence related assault")
print()
fig1, ax1 = plt.subplots()
ax1.pie(alcohol['Domestic violence related assault'], explode=(0, 0.1), labels=alcohol.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
#plt.title('Domestic violence related assault')
plt.show()
print()
print()
print("Sexual assault")
print()
fig1, ax1 = plt.subplots()
ax1.pie(alcohol['Sexual assault'], explode=(0, 0.1), labels=alcohol.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  
#plt.title('Sexual assault')
plt.show()
print()
print()
print("Indecent assault, act of indecency and other sexual offences")
print()
fig1, ax1 = plt.subplots()
ax1.pie(alcohol['Indecent assault, act of indecency and other sexual offences'], explode=(0, 0.1), labels=alcohol.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  
#plt.title('Indecent assault, act of indecency and other sexual offences')
plt.show()


# According to the recent NSW Population Health Survey, 32.8% of adults (41.2% of men and 22.8% of women) consume more than 2 standard alcoholic drinks on a day. Although it is impossible to prove causality, alcohol does seem to have influence on domestic violence. The percentages of alcohol related cases for sexual assault and indecent assault do not seem to be significant.

# # Time

# Let's analyze time-based patterns for domestic violence, sexual crimes and other acts of indecency in NSW.

# In[91]:


time = pd.read_excel(filename, 'Time', skiprows=4)
time.head()


# The headers seem to be nested. There are seven days (Sunday to Saturday) and for each day there are 4 time slots.

# In[92]:


time['Offence type'][0] = 'Time'
data_of_interest = ['Time','Domestic violence related assault','Sexual assault', 'Indecent assault, act of indecency and other sexual offences']


# In[93]:


time = time[time['Offence type'].isin(data_of_interest)]
time.head()


# In[94]:


for i in range(7):
    time.drop(['Unnamed: ' + str((i+1)*5)], axis=1, inplace=True)
for i in range(4):
    time.rename(columns={'Unnamed: ' + str(i+2): "Sunday"}, inplace=True)
    time.rename(columns={'Unnamed: ' + str(i+7): "Monday"}, inplace=True)
    time.rename(columns={'Unnamed: ' + str(i+12): "Tuesday"}, inplace=True)
    time.rename(columns={'Unnamed: ' + str(i+17): "Wednesday"}, inplace=True)
    time.rename(columns={'Unnamed: ' + str(i+22): "Thursday"}, inplace=True)
    time.rename(columns={'Unnamed: ' + str(i+27): "Friday"}, inplace=True)
    time.rename(columns={'Unnamed: ' + str(i+32): "Saturday"}, inplace=True)
time.head()


# Let's transpose the dataframe.

# In[95]:


time.rename(columns={"Offence type": ""}, inplace=True)
time.set_index('', inplace=True)
time = time.T
time.head()


# In[96]:


time.Time.replace("6pm - < 12pm", "6pm - < 12am", inplace=True)
time.reset_index(inplace=True)
time.rename(columns={"index": "Day"}, inplace=True)
time.head()


# In[97]:


time.set_index(['Day', 'Time'], inplace=True)
time.head(20)


# ### Day of week analysis

# Let's analyze the total number of cases for each day of the week.

# In[105]:


time.unstack(level=1)['Domestic violence related assault'].reindex(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']).sum(axis=1).plot(kind = 'line', color='r', label='Domestic violence related assault',linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))
plt.xlabel('')              
plt.ylabel('Number of cases')    
plt.title('Domestic violence related assault')
plt.show()   

time.unstack(level=1)['Sexual assault'].reindex(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']).sum(axis=1).plot(kind = 'line', color='g', label='Sexual assault',linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))   
plt.xlabel('')              
plt.ylabel('Number of cases')    
plt.title('Sexual assault')
plt.show()    

time.unstack(level=1)['Indecent assault, act of indecency and other sexual offences'].reindex(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']).sum(axis=1).plot(kind = 'line', color='b', label='Indecent assault, act of indecency and other sexual offences',linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))  
plt.xlabel('')              
plt.ylabel('Number of cases')    
plt.title('Indecent assault, act of indecency and other sexual offences')
plt.show()    


# As expected, domestic violence peaks on Saturdays and Sundays. This is consistant the the monthly seasonal pattern. Sexual assault and indecent assault peak on Tuesday and Monday respectively for unknown reasons. 

# ### Time of day analysis

# Let's analyze the total number of cases for each time segement.

# In[106]:


time.unstack(level=0)['Domestic violence related assault'].reindex(['12am - < 6am', '6am - < 12pm', '12pm - < 6pm', '6pm - < 12am']).sum(axis=1).plot(kind = 'line', color='r', label='Domestic violence related assault',linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))
plt.xlabel('')              
plt.ylabel('Number of cases')    
plt.title('Domestic violence related assault')
plt.show()   

time.unstack(level=0)['Sexual assault'].reindex(['12am - < 6am', '6am - < 12pm', '12pm - < 6pm', '6pm - < 12am']).sum(axis=1).plot(kind = 'line', color='g', label='Sexual assault',linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))   
plt.xlabel('')              
plt.ylabel('Number of cases')    
plt.title('Sexual assault')
plt.show()    

time.unstack(level=0)['Indecent assault, act of indecency and other sexual offences'].reindex(['12am - < 6am', '6am - < 12pm', '12pm - < 6pm', '6pm - < 12am']).sum(axis=1).plot(kind = 'line', color='b', label='Indecent assault, act of indecency and other sexual offences',linewidth=2,alpha = 1,grid = True,linestyle = '-', figsize=(12, 4))  
plt.xlabel('')              
plt.ylabel('Number of cases')    
plt.title('Indecent assault, act of indecency and other sexual offences')
plt.show()    


# As expected, domestic violence seem to peak after office hours (6pm to midnight). Sexual assault and indecent assult seem to peak at midnight.

# ### Individual days

# In[168]:


def plotDay(day):  
    fig,ax = plt.subplots(figsize=(12,4))
    date_of_interest = time.loc[day]
    ax.plot(date_of_interest.index, date_of_interest['Domestic violence related assault'], color='r', label='Domestic violence related assault',linewidth=2,alpha = 1,linestyle = '-')
    ax.set_xlabel('Time of day')      
    ax.set_ylabel('Number of cases of domestic violence')    
    ax.legend(loc='upper left') 
    
    ax2 = ax.twinx()
    ax2.plot(date_of_interest.index, date_of_interest['Sexual assault'], color='g', label='Sexual assault',linewidth=2,alpha = 1,linestyle = '-')
    ax2.set_xlabel('Time of day')      
    ax2.set_ylabel('Number of cases of sexual assault/indecent assault')    
    
    ax2.plot(date_of_interest.index, date_of_interest['Indecent assault, act of indecency and other sexual offences'], color='b', label='Indecent assault, act of indecency and other sexual offences',linewidth=2,alpha = 1,linestyle = '-')
    ax2.legend(loc='upper right') 
    plt.show()
        


# In[179]:


for day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
    print(day)    
    plotDay(day)
    print()


# Daily variations seem to be similar for all the days of the week from Sunday to Saturday.

# # Offenders

# Let's analyze ages and genders of offenders of domestic violence, sexual crimes and other acts of indecency in NSW.

# In[32]:


offenders = pd.read_excel(filename, 'Offenders', skiprows=4)
offenders.head()


# Let's delete unnecessary columns.

# In[33]:


offenders.rename(columns={"Alleged offender's gender; Alleged offender's age": "Gender"}, inplace=True)
offenders.rename(columns={"Unnamed: 1": "Age"}, inplace=True)
offenders = offenders[['Gender', 'Age', 'Domestic violence related assault','Sexual assault', 'Indecent assault, act of indecency and other sexual offences']]
offenders.head(20)


# Let's remove unnecessary rows.

# In[34]:


offenders = offenders.iloc[:20, :]
offenders = offenders[~offenders.index.isin([9, 10])]
offenders.tail()


# In[35]:


offenders.head(20)


# In[36]:


for i in range(0,9):
    offenders.Gender[i] = 'Male'
    offenders.Gender[i+11] = 'Female'
    
offenders.set_index(['Gender', 'Age'], inplace=True)
offenders.head(20)


# ### Gender analysis

# **Domestic violence related assault**

# In[184]:


data_of_interest = offenders.unstack(level=1)['Domestic violence related assault'].sum(axis=1)
print(data_of_interest)
fig1, ax1 = plt.subplots()
ax1.pie(data_of_interest, explode=(0, 0.1), labels=data_of_interest.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()


# As depicted above, around three quarters of the domestic violence offenders are male. 

# **Sexual assault**

# In[189]:


data_of_interest = offenders.unstack(level=1)['Sexual assault'].sum(axis=1)
print(data_of_interest)
fig1, ax1 = plt.subplots()
ax1.pie(data_of_interest, explode=(0, 0.2), labels=data_of_interest.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()


# As depicted above, almost all the sexual assault offenders are male.  

# **Indecent assault, act of indecency and other sexual offences**

# In[190]:


data_of_interest = offenders.unstack(level=1)['Indecent assault, act of indecency and other sexual offences'].sum(axis=1)
print(data_of_interest)
fig1, ax1 = plt.subplots()
ax1.pie(data_of_interest, explode=(0, 0.2), labels=data_of_interest.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()


# As depicted above, almost all the 'indecent assault' offenders are male.

# ### Age analysis

# **Domestic violence related assault**

# In[214]:


offenders.loc['Male']['Domestic violence related assault'].plot.bar(color='blue')
plt.ylabel('Number of cases')
plt.title('Male offenders of domestic violence related assault')
plt.show()

offenders.loc['Female']['Domestic violence related assault'].plot.bar(color='pink')
plt.ylabel('Number of cases')
plt.title('Female offenders of domestic violence related assault')
plt.show()


# The most common age group of domestic violence offenders for both sexes is 30-39.

# **Sexual assault**

# In[217]:


offenders.loc['Male']['Sexual assault'].plot.bar(color='blue')
plt.ylabel('Number of cases')
plt.title('Male offenders of sexual assault')
plt.show()

offenders.loc['Female']['Sexual assault'].plot.bar(color='pink')
plt.ylabel('Number of cases')
plt.title('Female offenders of sexual assault')
plt.show()


# The most common age group of sexual assault offenders for both sexes is 30-39. For females, the 25-29 age group is also as common as 30-39. There is a significant number of male offenders of under 18 years of age.

# **Indecent assault, act of indecency and other sexual offences**

# In[218]:


offenders.loc['Male']['Indecent assault, act of indecency and other sexual offences'].plot.bar(color='blue')
plt.ylabel('Number of cases')
plt.title('Male offenders of indecent assault, act of indecency and other sexual offences')
plt.show()

offenders.loc['Female']['Indecent assault, act of indecency and other sexual offences'].plot.bar(color='pink')
plt.ylabel('Number of cases')
plt.title('Female offenders of indecent assault, act of indecency and other sexual offences')
plt.show()


# The most common age group of 'indecent assault' offenders for male is 40-49 whereas it is 30-39 for females.

# # Victims

# Let's analyze ages and genders of victims of domestic violence, sexual crimes and other acts of indecency in NSW.

# In[37]:


victims = pd.read_excel(filename, 'Victims', skiprows=4)
victims.head()


# Let's drop irrelevant columns and rename some columns.

# In[38]:


victims.rename(columns={"Victim's gender": "Gender"}, inplace=True)
victims.rename(columns={"Victim's age": "Age"}, inplace=True)
data_of_interest = ['Gender','Age','Domestic violence related assault','Sexual assault', 'Indecent assault, act of indecency and other sexual offences']
victims = victims[data_of_interest]
victims.head(10)


# Let's use multi-indexing.

# In[39]:


victims = victims.iloc[:16, :]
victims = victims[~victims.index.isin([7, 8])]
victims.set_index(['Gender', 'Age'], inplace=True)
victims.head(10)


# Note that there are some missing values. Let's replace them with 0's. 

# In[242]:


victims['Sexual assault'][victims['Sexual assault']=='na']=0
victims['Indecent assault, act of indecency and other sexual offences'][victims['Indecent assault, act of indecency and other sexual offences']=='na']=0


# ### Gender analysis

# **Domestic violence related assault**

# In[243]:


data_of_interest = victims.unstack(level=1)['Domestic violence related assault'].sum(axis=1)
print(data_of_interest)
fig1, ax1 = plt.subplots()
ax1.pie(data_of_interest, explode=(0, 0.1), labels=data_of_interest.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()


# 63.7% of domestic violence victims are female and 23.3% of the victims are male.
# Note that this is contrary to the previous finding where around three quarters of domestic violence offenders are male. 
# 
# It means that some males are victims of other males.

# **Sexual assault**

# In[245]:


data_of_interest = victims.unstack(level=1)['Sexual assault'].sum(axis=1)
print(data_of_interest)
fig1, ax1 = plt.subplots()
ax1.pie(data_of_interest, explode=(0, 0.1), labels=data_of_interest.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()


# 91.2% of sexual assault victims are female while the rest are male. Again, this is contrary to the previous finding where 97.7% of sexual assault offenders are male.  It means that some males are victims of other males.
# 
# 

# **Indecent assault, act of indecency and other sexual offences**

# In[246]:


data_of_interest = victims.unstack(level=1)['Indecent assault, act of indecency and other sexual offences'].sum(axis=1)
print(data_of_interest)
fig1, ax1 = plt.subplots()
ax1.pie(data_of_interest, explode=(0, 0.1), labels=data_of_interest.index, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()


# 84.9% of the 'indecent assault' victims are female. Again, this is contrary to the previous finding where 95.6% of 'indecent assault' offenders are male.  It means that some males are victims of other males.

# ### Age analysis

# **Domestic violence related assault**

# In[248]:


victims.loc['Male']['Domestic violence related assault'].plot.bar(color='blue')
plt.ylabel('Number of cases')
plt.title('Male victims of domestic violence related assault')
plt.show()

victims.loc['Female']['Domestic violence related assault'].plot.bar(color='pink')
plt.ylabel('Number of cases')
plt.title('Female victims of domestic violence related assault')
plt.show()


# The most common age group of domestic violence victims for both sexes is 20-29. This is contrary to the previous finding where the 
# The most common age group of domestic violence offenders for both sexes is 30-39. It means offenders tend to be older than their victims.

# **Sexual assault**

# In[250]:


victims.loc['Male']['Sexual assault'].plot.bar(color='blue')
plt.ylabel('Number of cases')
plt.title('Male victims of sexual assault')
plt.show()

victims.loc['Female']['Sexual assault'].plot.bar(color='pink')
plt.ylabel('Number of cases')
plt.title('Female victims of sexual assault')
plt.show()


# The most common age group of sexual assault victims for both sexes is under 18. This is contrary to the previous finding where the most common age group of sexual assault offenders for both sexes is 30-39. Unfortunately, it means that old offenders tend to prey on younger victims.  

# **Indecent assault, act of indecency and other sexual offences**

# In[251]:


victims.loc['Male']['Indecent assault, act of indecency and other sexual offences'].plot.bar(color='blue')
plt.ylabel('Number of cases')
plt.title('Male victims of indecent assault, act of indecency and other sexual offences')
plt.show()

victims.loc['Female']['Indecent assault, act of indecency and other sexual offences'].plot.bar(color='pink')
plt.ylabel('Number of cases')
plt.title('Female victims of indecent assault, act of indecency and other sexual offences')
plt.show()


# Just like sexual assault victims, the most common age group of 'indecent assault' victims for both sexes is under 18.

# # POI relationship to victims

# Let's analyze relationships between offenders and victims of domestic violence, sexual crimes and other acts of indecency in NSW.

# In[40]:


relationship = pd.read_excel(filename, 'POI relationship to victim', skiprows=4)
relationship.head()


# In[41]:


relationship.rename(columns={"Alleged offenders relationship to victim": "Relationship"}, inplace=True)
data_of_interest = ['Relationship','Domestic violence related assault','Sexual assault', 'Indecent assault, act of indecency and other sexual offences']
relationship = relationship[data_of_interest]


# In[42]:


relationship.head()


# In[43]:


relationship.tail(12)


# Footer information got fused  into the data frame. Let's delete rows with ID 13 and and above and set 'Relationship' as index.

# In[44]:


relationship = relationship.iloc[:13]
relationship.set_index('Relationship', inplace=True)
relationship.tail()


# Since there are too many missing and unknown values for sexual assault and indecent assault, let's just analyze domestic violence related assault.

# In[254]:


relationship.head(20)


# In[261]:


relationship['Domestic violence related assault'].plot.barh(color='purple')
plt.xlabel('Number of cases')
plt.show()


# The most common type of relationship between offenders and victims is boy/girlfriend. The second most common type is spouse/partner.
