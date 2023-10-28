import pandas as pd
import os
import time
from csv2pdf import convert
from Backend.mian import makingpdf
from Backend.Plotter import plotting
from Backend.conclusion import concluding



def CalCulateUnits(name:list, watts:list, quantity:list, hours:list):
    Energy = { # CREATING EMPTY DICTIONARY FOR CREATING AN EMPTY DATAFRAME
        'Name_of_appliance':[] ,
        "Watts" :[] ,
        'Quantity' :[] ,
        'Total Watts' :[] ,
        'Number_of_Hours' :[] ,
        "Energy" :[]
    }

    df = pd.DataFrame(Energy) # CONVERTING THE DICTIONARY TO DATAFRAME


    # ----------- CALCULATING TOTAL WATTS ------------------
    Total_watts = []

    for i in range(len(watts)):
        watts[i] = int(watts[i])
        quantity[i] = int(quantity[i])

        Total_watts.append(watts[i] * quantity[i])
    # ------------------------------------------------------



    # --------------------- CALCULATING TOTAL ENERGY ----------------------
    Total_energy = []

    for i in range(len(watts)):
        hours[i] = int(hours[i])

        Total_energy.append(Total_watts[i] * hours[i])
    # -----------------------------------------------------------------------



    # ------------------ FILLING THE DATAFRAME --------------------------
    for i in range(len(watts)):
        NewEnergy = {
        'Name_of_appliance':name[i] ,
        "Watts" :watts[i] ,
        'Quantity' :quantity[i] ,
        'Total Watts' :Total_watts[i] ,
        'Number_of_Hours' :hours[i] ,
        "Energy" :Total_energy[i]
        }

        df = df._append(NewEnergy,
                        ignore_index = True) # APPENDING TO ORIGINAL EMPTY DATAFRAME
    # -------------------------------------------------------------------



    concluding(df.Name_of_appliance, df.Energy) # PASSING THE NAMES OF APPLIANCES AND TOTAL ENERGY USED COLUMNS FOR MAKING CONCLUSIONS


    # ---------------- CHECKING IF THE CSV FILE ALREADY EXISTS OR NOT ---------------------------
    csvfile = 'CalculatedData.csv'
    location = 'C:/Users/sunil/OneDrive/Desktop/green computing web app/'
    csvpath = os.path.join(location, csvfile)

    if os.path.exists(csvpath): # IF ALREADY EXISTS THEN IT WILL DELETE IT FIRST AND CREATE THE NEW ONE
        os.remove(csvpath)

        time.sleep(1)

        first = df.to_csv('CalculatedData.csv',
                      index = False)

    else:
        first = df.to_csv('CalculatedData.csv', # ELSE IT WILL DIRECTLY CREATE A NEW CSV FILE
                        index = False)
    # ---------------------------------------------------------------------------------------------

    time.sleep(2)

    plotting() # RUNNING THE PLOTTING FUNCTION TO CREATE VISUALIZATIONS FROM THE DATAFRAME

    time.sleep(2)

    makingpdf() # PASSING THE CSV FILE TO CONVERT IT PDF FORMAT



if __name__ == '__main__':
    CalCulateUnits()
