from webbrowser import get
import pandas as pd

df = pd.read_csv("Semaine 10\ForestRoad PV 3kwp.csv", sep=";", header=0)

def get_time_covered():
    print(f'Time covered : from {df["datetime"][1]} to {df.at[df.index[-1], "datetime"]}')
    f = open("Semaine 10\Readme.txt", "w")
    f.write(f'Time covered : from {df["datetime"][1]} to {df.at[df.index[-1], "datetime"]}')
    f.close()

get_time_covered()

def fix_null_prod():
    df.replace(0.002, 0, inplace=True)

fix_null_prod()

def create_new_column():
    df["P_GEN"] = (df["P_GEN_MAX"]+df["P_GEN_MIN"])/2

create_new_column()

df.to_csv("Semaine 10\Cleaned ForestRoad PV 3kwp.csv", sep=";", index=False)

def get_max_prod():
    day = input("Enter a day (dd/mm/yyyy): ")
    day_prod = []
    for i in range(len(df)):
        if df.at[i, "datetime"][:10] == day:
            day_prod.append(df.at[i, "P_GEN_MAX"])
    print(f'Max production on {day} was {max(day_prod)} kW')

# get_max_prod()

def get_average_prod():
    day = input("Enter a day (dd/mm/yyyy): ")
    day_av = []
    for i in range(len(df)):
        if df.at[i, "datetime"][:10] == day:
            day_av.append(df.at[i, "P_GEN"])
    print(f'Average production on {day} was around {round(sum(day_av)/len(day_av),4)} kW')

get_average_prod()