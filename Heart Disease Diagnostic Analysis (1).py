#!/usr/bin/env python
# coding: utf-8

# # Heart Disease Diagnostic Analysis

# In[1]:


#Importing Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style('whitegrid')


# In[2]:


#Extracting CSV Dataset From System using Pandas Library

data=pd.read_csv('Heart Disease data.csv')
data


# In[3]:


#All Columns in the Dataset

data.columns


# ##### There are thirteen features in Dataset
# age: The person's age in years
# 
# sex: The person's sex (1 = male, 0 = female)
# 
# cp: The chest pain experienced (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)
# 
# trestbps: The person's resting blood pressure (mm Hg on admission to the hospital)
# 
# chol: The person's cholesterol measurement in mg/dl
# 
# fbs: The person's fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
# 
# restecg: Resting electrocardiographic measurement or results (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)
# 
# thalach: The person's maximum heart rate achieved
# 
# exang: Exercise induced angina (1 = yes; 0 = no)
# 
# oldpeak: ST depression induced by exercise relative to rest
# 
# slope: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)
# 
# ca: The number of major vessels (0-3)
# 
# thal: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)
# 
# target: Heart disease (0 = no, 1 = yes)

# In[4]:


#Checking NULL Values

data.isnull().sum()


# ###### There is NO MISSING Values in our Dataset

# ## Percentage of how many people are having Heart Disease

# In[5]:


num = data.groupby('target').size()
num


# ###### 526 are having heart disease

# In[6]:


#Converting Numerical Data into Categorical Data

def heart_disease(row):
    if row==0:
        return 'Absence'
    elif row==1:
        return 'Presence'


# In[7]:


#Applying converted data into our dataset with new column - Heart_Disease

data['Heart_Disease'] = data['target'].apply(heart_disease)
data.head() 


# In[9]:


# Count the number of heart disease present using count fucntion

hd = data.groupby('Heart_Disease')['target'].count()
hd


# In[10]:


#Pie Chart creation of Heart Disease Population % using MatplotLib

plt.figure(figsize=(10,7))
plt.pie(hd, labels=['Absence','Presence'], autopct='%0.0f%%')
plt.title('Heart Disease Population %', fontsize=20)
plt.show()


# ###### From the overall population, people having heart disease (51%) are more than those who doesn't have heart disease(49%)

# In[11]:


#Countplot Creation of Population Age using MatplotLib and Seaborn

plt.figure(figsize=(15,7))
sns.countplot(x='age', data=data)
plt.title('Population Age', fontsize=17)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.show()


# ###### In this part, the best analysis can be divided into the elderly,middle-aged, young people by looking at the age ranges.
# 

# In[14]:


#Statistical Analysis of number of min. max and mean age of the poeple

Min_Age = data['age'].min()
Max_Age = data['age'].max()
Mean_Age = data['age'].mean()
print("Minimum Age =",Min_Age)
print("Maximum Age =",Max_Age)
print("Mean Age =",Mean_Age)


# In[13]:


#Categorical Analysis of number of young, mid and edlerly people

Young_Ages = data[(data['age']>=29) & (data['age']<40)]
Middle_Ages = data[(data['age']>=40) & (data['age']<55)]
Elderly_Ages = data[(data['age']>55)]
print('Young Ages =',len(Young_Ages))
print('Middle Ages =',len(Middle_Ages))
print('Elderly Ages =',len(Elderly_Ages))


# In[15]:


#Bar Plot Creation of Age Category using MatplotLib and Seaborn

sns.barplot(x=['Young_Ages','Middle_Ages','Elderly_Ages'], y=[len(Young_Ages), len(Middle_Ages), len(Elderly_Ages)], palette='YlGn_r')
plt.title('Age Category', fontsize=17)
plt.xlabel('Age Range', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.show()


# In[16]:


#Converting Numerical Data into Categorical Data

def gender(row):
    if row==1:
        return 'Male'
    elif row==0:
        return 'Female'


# In[18]:


#Applying converted data into our dataset with new column - sex1

data['sex1'] = data['sex'].apply(gender)
data.head()


# In[19]:


#Converting Numerical Data into Categorical Data

def age_range(row):
    if row>=29 and row<40:
        return 'Young Age'
    elif row>=40 and row<55:
        return 'Middle Age'
    elif row>55:
        return 'Elder Age'


# In[20]:


#Applying converted data into our dataset with new column - Age_Range

data['Age_Range'] = data['age'].apply(age_range)
data.head()


# In[21]:


#Swarm Plot Creation of Gender Based Age Category using MatplotLib and Seaborn

plt.figure(figsize=(10,7))
sns.swarmplot(x='Age_Range', y='age', hue='sex1', data=data, order=['Young Age','Middle Age','Elder Age'], palette='Oranges_r')
plt.title('Gender Based Age Category', fontsize=17)
plt.xlabel('Age Category', fontsize=15)
plt.ylabel('Age', fontsize=15)
plt.show()


# ###### In this population, number of males are more in middle age category and females are more in elder age category
# 

# In[24]:


#Count Plot Creation of Heart Disease Based On Age Category using MatplotLib and Seaborn

plt.figure(figsize=(7,5))
hue_order=['Young Age', 'Middle Age', 'Elder Age']
sns.countplot(x='Heart_Disease', hue='Age_Range', data=data, order=['Presence','Absence'], hue_order=hue_order, palette='Pastel1')
plt.title('Heart Disease based on Age', fontsize=17)
plt.xlabel('Heart Disease', fontsize=15)
plt.ylabel('Counts', fontsize=15)
plt.show()


# ######  Middle aged people are most affected by heart disease AND Elder aged people are mostly free from any kind of heart disease
# 

# In[25]:


#Count Plot Creation of Heart Disease Based on Gender using MatplotLib and Seaborn

plt.figure(figsize=(7,5))
sns.countplot(x=data['Heart_Disease'], hue='sex1', data=data, palette='BuGn_r')
plt.xlabel('Heart Disease', fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.legend(labels=['Male','Female'])
plt.title('Heart Disease Based on Gender',fontsize=17)
plt.show()


# ###### We can see that males are more prone to heart disease
# 

# In[26]:


#Count Plot Creation of Chest Pain Experienced using MatplotLib and Seaborn

sns.countplot(x=data['Heart_Disease'], hue='cp', data=data, order=['Presence','Absence'])
plt.title('Chest Pain Experienced', fontsize=17)
plt.xlabel('Heart Disease',fontsize=15)
plt.ylabel('Counts',fontsize=15)
plt.legend(labels=['Typical Angina','Atypical Angina','Non-Anginal pain','Asymptomatic'])
plt.show()


# ######  People having 'Non-Anginal chest pain' have a higher chance of heart disease.
# Nonanginal chest pain, also known as non-cardiac chest pain (NCCP), is a common symptom of many conditions that don't involve heart disease.
# 

# In[27]:


#Count Plot Creation of Chest Pain Based On Gender using MatplotLib and Seaborn

sns.countplot(x=data['sex1'], hue='cp', data=data)
plt.title('Chest Pain Based On Gender', fontsize=17)
plt.xlabel('Sex', fontsize=15)
plt.ylabel('Counts', fontsize=15)
plt.legend(labels=['Typical Angina','Atypical Angina','Non-Anginal pain','Asymptomatic'])
plt.show()


# ###### We can see that a higher number of men are suffering from 'Typical Angina' type of Chest Pain

# In[28]:


#Count Plot Creation of Chest Pain Based On Age Category using MatplotLib and Seaborn

sns.countplot(x=data['Age_Range'], hue='cp', data=data, order=['Young Age', 'Middle Age', 'Elder Age'], palette='BrBG')
plt.title('Chest Pain Based On Age Category', fontsize=17)
plt.xlabel('Age Category', fontsize=15)
plt.ylabel('Counts', fontsize=15)
plt.legend(labels=['Typical Angina','Atypical Angina','Non-Anginal pain','Asymptomatic'])
plt.show()


# ###### There is very high number of Typical Angina Pain in Elderly age Category
# 

# In[29]:


#Bar Plot Creation of Person's Resting Blood Pressure (mm Hg) using MatplotLib and Seaborn

sns.barplot(x='sex1', y='trestbps', data=data, palette='plasma')
plt.title("Blood Pressure", fontsize=17)
plt.xlabel('Sex',fontsize=15)
plt.ylabel("Person's Resting Blood Pressure (mm Hg)", fontsize=12)
plt.show()


# ###### Blood Pressure Rate is almost equal in both males and females
# 

# In[31]:


#Bar Plot Creation of Cholestrol Level Based On Gender using MatplotLib and Seaborn

sns.barplot(x='sex1', y='chol', data=data, palette='turbo')
plt.title("Cholestrol Level Based On Gender", fontsize=17)
plt.xlabel('Sex',fontsize=15)
plt.ylabel("Cholestrol", fontsize=15)
plt.show()


# ###### Females have little bit of higher cholesterol than males
# 

# In[32]:


#Bar Plot Creation of Cholestrol VS Heart Disease using MatplotLib and Seaborn

sns.barplot(x='Heart_Disease', y='chol', data=data, palette='ocean_r')
plt.title('Cholestrol VS Heart Disease', fontsize=17)
plt.xlabel('Heart Disease', fontsize=15)
plt.ylabel('Cholestrol', fontsize=15)
plt.show()


# ###### Absence of Cholestrol Level results in high chances Of Heart Disease
# In this dataset, cholestrol has no relation with increase of heart disease
# 

# In[33]:


#Bar Plot Creation of Blood Pressure VS Heart Disease using MatplotLib and Seaborn

sns.barplot(x='Heart_Disease', y='trestbps', data=data, palette='tab20b_r')
plt.title('Blood Pressure VS Heart Disease', fontsize=17)
plt.xlabel('Heart Disease', fontsize=15)
plt.ylabel('Blood Pressure', fontsize=15)
plt.show()


# ###### Absence of Blood Pressure Level results in high chances Of Heart Disease
# In this dataset, blood pressure has no relation with increase of heart disease
# 

# In[34]:


#Line Plot Creation of Blood Pressure VS Age using MatplotLib and Seaborn

sns.lineplot(x='age', y='trestbps', data=data, color='r')
plt.title('Blood Pressure VS Age', fontsize=17)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Blood Pressure', fontsize=15)
plt.show()


# ###### Here, we can observe that Blood Pressure increases from mid 50s to 70s.
# 

# In[35]:


#Line Plot Creation of Cholestrol VS Age using MatplotLib and Seaborn

sns.lineplot(x='age', y='chol', data=data, color='b')
plt.title('Cholestrol VS Age', fontsize=17)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Cholestrol', fontsize=15)
plt.show()


# ###### ###### Here, we can observe that cholestrol increases from mid 50s to 70s.
# 

# In[36]:


#Line Plot Creation of ST Depression VS Age using MatplotLib and Seaborn

sns.lineplot(x='age', y='oldpeak', data=data, color='g')
plt.title('ST Depression VS Age', fontsize=17)
plt.xlabel('Age', fontsize=15)
plt.ylabel('ST depression', fontsize=15)
plt.show()


# ###### We can observe from here that ST depression mostly increases bw the age group of 30-40
# ST depression refers to a finding on an electrocardiogram, wherein the trace in the ST segment is abnormally low below the baseline.
# 

# In[37]:


#Bar Plot Creation of ST depression VS Heart Disease using MatplotLib and Seaborn

sns.barplot(x='sex1', y='oldpeak', data=data, palette='twilight_r')
plt.title('ST depression VS Heart Disease', fontsize=17)
plt.xlabel('Sex', fontsize=15)
plt.ylabel('ST depression', fontsize=15)
plt.show()


# ###### ST depression is seen more in male than female
# 

# In[38]:


#Bar Plot Creation of Exercise With Angina VS Heart Disease using MatplotLib and Seaborn

sns.barplot(x='Heart_Disease', y='exang', data=data, palette='viridis')
plt.title('Exercise With Angina VS Heart Disease', fontsize=17)
plt.xlabel('Heart Disease', fontsize=15)
plt.ylabel('Exercise With Angina', fontsize=15)
plt.show()


# ###### If you suffer from Angina, absence of exercise might be the cause for heart disease
# 

# In[39]:


#Bar Plot Creation of Exercise With Angina VS Gender using MatplotLib and Seaborn

sns.barplot(x='sex1', y='exang', data=data, palette='binary_r')
plt.title('Exercise With Angina VS Gender', fontsize=17)
plt.xlabel('Sex', fontsize=15)
plt.ylabel('Exercise With Angina', fontsize=15)
plt.show()


# ###### Exercising might risk the chances of angina within males
# Angina is chest pain or discomfort caused when your heart muscle doesn't get enough oxygen-rich blood

# In[40]:


#Bar Plot Creation of Fasting Blood Sugar VS Gender using MatplotLib and Seaborn

sns.barplot(y='fbs', x='sex1', data=data, palette='hsv')
plt.title(' Fasting Blood Sugar VS Gender', fontsize=17)
plt.xlabel('Sex', fontsize=15)
plt.ylabel('Fasting Blood Sugar', fontsize=15)
plt.show()


# ###### Males have high number of Fasting Blood Sugar over 120
# 

# In[43]:


#Heatmap Creation using Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Dropping non-numeric columns
numeric_data = data.select_dtypes(include=[float, int])

# Heatmap Creation using Seaborn
plt.figure(figsize=(16,9))
sns.heatmap(numeric_data.corr(), annot=True, linewidth=3)
plt.show()


# In[ ]:





# In[ ]:




