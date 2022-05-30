import pandas as pd

df = pd.read_csv("Semaine 10\ForestRoad PV 3kwp.csv", sep=";", header=0)

def get_time_covered():
    print(f'Time covered : from {df["datetime"][1]} to {df.at[df.index[-1], "datetime"]}')
    f = open("Semaine 10\Readme.txt", "w")
    f.write(f'Time covered : from {df["datetime"][1]} to {df.at[df.index[-1], "datetime"]}')
    f.close()

get_time_covered()

# Fixing Null values
df.replace(0.002, 0, inplace=True)
# Adding new column
df["P_GEN"] = (df["P_GEN_MAX"]+df["P_GEN_MIN"])/2
# Printing the fixes and additions to new file
df.to_csv("Semaine 10\Cleaned ForestRoad PV 3kwp.csv", sep=";", index=False)

def get_max_prod():
    print("\nGet the maximum production on a day")
    day = input("Enter a day (dd/mm/yyyy): ")
    if df["datetime"][1] <= day <= df.at[df.index[-1], "datetime"]:
        print("The day you entered is not in the dataframe")
    else:
        day_prod = []
        for i in range(len(df)):
            if df.at[i, "datetime"][:10] == day:
                day_prod.append(df.at[i, "P_GEN_MAX"])
        if len(day_prod) == 0:
            print("There is no production on this day")
        else:
            print(f'Max production on {day} was {max(day_prod)} kW')

get_max_prod()

def get_average_prod():
    print("\nGet the average production on a day")
    day = input("Enter a day (dd/mm/yyyy): ")
    if df["datetime"][1] <= day <= df.at[df.index[-1], "datetime"]:
        print("The day you entered is not in the dataframe")    
    else:    
        day_av = []
        for i in range(len(df)):
            if df.at[i, "datetime"][:10] == day:
                day_av.append(df.at[i, "P_GEN"])
        if len(day_av) == 0:
            print("There is no production on this day")
        else:
            print(f'Average production on {day} was around {round(sum(day_av)/len(day_av),3)} kW')

get_average_prod()