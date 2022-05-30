import pandas as pd

df = pd.read_csv("Semaine 10\ForestRoad PV 3kwp.csv", sep=";", header=0)

def get_time_covered():
    print(f'Time covered : from {df["datetime"][1]} to {df.at[df.index[-1], "datetime"]}')
    f = open("Semaine 10\Readme.txt", "w")
    f.write(f'Time covered : from {df["datetime"][1]} to {df.at[df.index[-1], "datetime"]}')
    f.close()

get_time_covered()

# Fixing null values
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
        production = []
        for i in range(len(df)):
            if df.at[i, "datetime"][:10] == day:
                production.append(df.at[i, "P_GEN_MAX"])
        if len(production) == 0:
            print("There was no production on this day")
        else:
            print(f'Max production on {day} was {max(production)} kW')

get_max_prod()

def get_average_prod():
    print("\nGet the average production on a day")
    day = input("Enter a day (dd/mm/yyyy): ")
    if df["datetime"][1] <= day <= df.at[df.index[-1], "datetime"]:
        print("The day you entered is not in the dataframe")    
    else:    
        average = []
        for i in range(len(df)):
            if df.at[i, "datetime"][:10] == day:
                average.append(df.at[i, "P_GEN"])
        if len(average) == 0:
            print("There was no production on this day")
        else:
            print(f'Average production on {day} was around {round(sum(average)/len(average),3)} kW')

get_average_prod()