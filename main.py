#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Lala Ghansham Ji is the local vendor of your locality who is running a grocery shop. He wants your help to
digitize his day to day transactions and monthly business. Find out whether he is making profit or loss on a daily
basis and what is his monthly income from the grocery shop? Can you help him out in doing so? You are free
to imagine your own real time set up for grocery shop and create user-defined functions to accomplish the task.
Formula: Result = Selling price – Cost price
NOTE: Once you have all 12 months turnover find the annual income of Lala Ji using lambda function.
'''

# built-in : random, append, sum, input ... 
# user-defined
# lambda functions


# In[1]:


# INCOME management 
# Monly income 
# randomly daily selling price + cost price set up => Result of daily 
# 30days repitaition -> sum of all results of daily (Monthly wise)
# 12months repitation -> sum of all results of monthly (yearly wise)
# Let's suppose month is same 30days

import random

year = input("Welcome to INCOME MANAGEMENT SYSTEM! How many years will you use this system?") 
print("\n")
        
day = int(year) * 360 #Operating dates
operating_dates = day #count variable

month_list = []
year_list = [] 
total_list = []

#Lambda functions
income_ld = lambda x : sum(x)
average_ld = lambda x : round(sum(x)/len(x))
    
def daily_report(day, result, selling, cost) : #Profit or Not
    if result > 0 : 
        print("Day : " + str(today) + " | "+"Selling, Cost : "+ str(selling) +", "+ str(cost)+ " | " +"Profit")
    else : # loss 
        print("Day : " + str(today) + " | "+"Selling, Cost : "+ str(selling) +", "+ str(cost)+ " | " +"Loss")
            
def monthly_report(month, result, average) : # Monthly income
    print("-----------Monthly Report-----------")
    print(str(month)+" Month" +" | "+"Total Month Income : "+str(result)+", "+ "Average income of this month : "+ str(average))
    print("------------------------------------")

while True : 
    
    #Counting dates
    today = day - operating_dates + 1 # 1,2,3...
    month_cnt = today // 30 
    year_cnt = month_cnt // 12 
        
    #Daily Income 
    daily_selling = random.randrange(1,30) # return ramdom number from 1 to 100
    daily_cost = random.randrange(1,30)
    daily_results = daily_selling - daily_cost
    
    #Daily report
    daily_report(today, daily_results, daily_selling, daily_cost)

    #Save daily income
    month_list.append(daily_results) 
  
    #Monthly report
    if today % 30 == 0 and today//30 >= 1 : 
        #Monthly Income
        total_monthly_results = sum(month_list)
        average_monthly_results = round(sum(month_list) / 30)
        #report
        monthly_report(month_cnt, total_monthly_results, average_monthly_results)
        month_list=[] # Initialization of Monthly list 
        # Save Monthly Income 
        year_list.append(total_monthly_results)
        # Yearly report
        if today % 360 == 0 and today//360 >= 1 : 
            #report
            print("============Yearly Report============")
            print(str(year_cnt)+ " Year" + " | "+"Total Annual Income : "+ str(income_ld(year_list))+", "+ "Average income of this year : "+ str(average_ld(year_list)))
            print("=====================================")
            yearly_income = income_ld(year_list)
            total_list.append(yearly_income)
            year_list = [] # Initialization of Yearly list 
    
    operating_dates -= 1 
    if operating_dates == 0 : 
        print("\nTODAY IS THE LAST DAY. THANK YOU.\n")

        print(">> TOTAL INCOME : " + str(income_ld(total_list))+ ", " + "TOTAL AVERAGE INCOME : "+ str(average_ld(total_list)))
        break

