import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

### reading the file
df = pd.read_csv("stock_data/ICICIBANK.NS.csv")
# print(df)

#clearing out the 0 values and inplace=true for saving changes, axis = 0 for colomn wise
df.dropna(inplace=True, axis = 0, how = "any")

#use of loc and iloc (loc for namewise and iloc for index wise)
# print(df.iloc[73])

#idk why tf we modify date colomn like this
df['Date'] = pd.to_datetime(df['Date'])

#making a new colomn named as percentage change
df['Perc_Change'] = df['Close'].pct_change() * 100
# df.to_csv("NIFTY50_Stocks/icicicici.csv")
#writing the new changes on the same file / new file
df.to_csv("stock_data/NIFTY50_Stocks/my_icici_1st.csv")

def perc_change():
    date_inp = input("Enter date in YYYY-MM-DD format: ")
    print(date_inp)
    choice_inp = input("press 1 for day change or press 2 for date of your choice")
    while True:
        if choice_inp == "1":
            print()
            print(f"percentage change is {df.loc[df['Date']== date_inp, 'Perc_Change'].round(2).item()}%")
            b= input("press e to exit or anything else to start over ")
            if b == "e" or b == "E":
                return False
            else:
                perc_change()
            # print(a)
        elif choice_inp == "2":
            date_inp2 = input("enter second date")
            a = df.loc[df['Date']== date_inp2 , 'Close'].item()
            b = df.loc[df['Date']== date_inp , 'Close'].item()
            percentage = ((b-a)/b)*100
            print(f"percentage change from {date_inp} to {date_inp2} is {round(percentage,2)}%")
            c= input("press e to exit or anything else to start over ")
            if c == "e" or c == "E":
                return False
            else:
                perc_change()
        else:
            print("Invalid choice")
            a= input("press e to exit or anything else to start over ")
            if a == "e" or a == "E":
                return 
            else:
                perc_change()      

def stock_data_stats():
    while True:
        starting_date = input("Enter a starting date in format YYYY-MM-DD : ")
        ending_date = input("Enter an ending date in format YYYY-MM-DD : ")
        df['Date'] = pd.to_datetime(df['Date'])
        df_dates = df[(df['Date']> starting_date )& (df['Date'] < ending_date)]
        meann = df_dates['Close'].mean()
        print(f"the mean closing is {meann}")
        print(df_dates["Close"].describe())
        a = input("enter 1 to start over or e to exit")
        if a == "1":
            stock_data_stats()
        elif a == "e" or a == "E":
            return False

def moving_average():
    while True:
        # df['Date'] = pd.to_datetime(df['Date'])
        _date = input("Enter a date in format YYYY-MM-DD : ")
        # _date = pd.to_datetime(_date)
        # _date = _date.date()
        print(_date)

        num_input = input("press 1 for for 5 day average, 2 for 10 day average and 3 for 50 day average")
        if num_input == "1":
            windoww = 5
        if num_input == "2":
            windoww = 10
        if num_input == "3":
            windoww =50
        df_dates = df[df['Date']<= _date].copy()
        # print(df_dates)
        df_dates[f'{windoww}_Day_MA'] = df_dates['Close'].rolling(window=windoww).mean()
        print(df_dates[f'{windoww}_Day_MA'])
        x = (df_dates[['Date','Close', f'{windoww}_Day_MA']])
        print(x)
        plt.plot(['Date'], x['Close'])
        plt.show()
        # print(df_dates.loc[f'{windoww}_Day_MA', f'{_date}'])
        # df.to_csv("NIFTY50_Stocks/icicicici_with10dayavg.csv")
        a = input("enter 1 to start over or e to exit")
        if a == "1":
            moving_average()
        elif a == "e" or a == "E":
            return False

while True:
    inp= input("press 1 for perc change, 2 for stats, 3 for movinng avg or press e to exit")
    if inp == "1":
        perc_change()
    elif inp =="2":
        stock_data_stats()
    elif inp== "3":
        moving_average()
    elif inp == "e" or inp == "E":
        False
    else:
        print("invalid input")


            
# perc_change()



        

# stock_data_stats()


# def dates_input():
#     starting_date = input("Enter a starting date in format YYYY-MM-DD : ")
#     ending_date = input("Enter an ending date in format YYYY-MM-DD : ")
#     df['Date'] = pd.to_datetime(df['Date'])
#     df_dates = df[(df['Date']> starting_date )& (df['Date'] < ending_date)]
#     return df_dates
# # a = dates_input()
# # print(a)




# # moving_average()