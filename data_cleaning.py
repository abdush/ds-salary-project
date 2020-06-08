# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:36:18 2020

@author: abdu
"""

import pandas as pd
import datetime

df = pd.read_csv("glassdoor_jobs.csv")

######### Salary parsing #################

# file doesn't have those - just in case
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['emp_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

# remove where no salary value was set
df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
salary_clean = salary.apply(lambda x: x.lower().replace('$', '').replace('k', '')
                                                    .replace('per hour', '').replace('employer provided salary', ''))
df['min_salary'] = salary_clean.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = salary_clean.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

###### Company name ######
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)


###### State field #####
#Todo handle when no state is provided
df['no_state'] = df['Location'].apply(lambda x: 0 if ',' in x else 1)
df['state'] = df['Location'].apply(lambda x: x.split(',')[1].strip() if ',' in x else x)
df.state.value_counts()
#location_no_state = df[df['Location'].str.contains(',') == False].Location
df['location_same_hq'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0, axis=1)

#company age
df['company_age'] = df.Founded.apply(lambda x: x if x < 0 else datetime.datetime.now().year - x)

#job description
df['has_python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['has_R'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r.studio' in x.lower() else 0)
df['has_spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['has_aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['has_excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['has_ML'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0)

df['has_python'].value_counts()
df['has_R'].value_counts()
df['has_spark'].value_counts()
df['has_aws'].value_counts()
df['has_excel'].value_counts()
df['has_ML'].value_counts()


df.columns
#df_out = df.drop(['Unnamed: 0'], axis=1)

df.to_csv('salary_data_cleaned.csv', index=False)

#pd.read_csv('salary_data_cleaned.csv')