import tkinter as tk
import pandas as pd
from datetime import date as da

root = tk.Tk()
root.geometry("600x500")

x_val = 260

qty1 , qty2 , qty3 = tk.IntVar() , tk.IntVar() , tk.IntVar()

dictt1 = {1:['Cafe Latte',30,70] , 2: ['Cappuccino',30,140], 3: ['Espresso',30,210]}
dot = da.today()
pricing = pd.read_csv("Files/Pricing.csv")
result = tk.Label(root , text = "" , fg = "black" , font = ("Arial",20)).place(x = 150  , y = 300 )


#Takes input and do the work of making bills
def gen():

    try:
        want_1 , want_2 , want_3 = qty1.get() , qty2.get() , qty3.get()
        sub_total = (want_1 * int(pricing.at[0,"Price"])) + (want_2 * int(pricing.at[1,"Price"])) + (want_3 * int(pricing.at[2,"Price"]))
        df = pd.read_csv("Files/Bill.csv")
        v = [dot , sub_total , .05 * sub_total , (sub_total + .05 * sub_total)]
        df.loc[len(df)] = v
        df.to_csv("Files/Bill.csv" , index = False)
        result.config(text = "Entry is done in the Book")
       
    except:
        result.config(text = "Error occured" , fg = "red")


#Using loop for making Labels
for i in dictt1:
    name = 0
    x_pos = 1
    y_pos = 2

    label = tk.Label(root , text = dictt1[i][name] , fg = "black" , font = ("Arial" , 25) ).place(x = dictt1[i][x_pos] , y = dictt1[i][y_pos] )


#Entries for taking Product Quantity  
entries = tk.Entry(root , bg = "black" , fg = "white" , width = 20 , bd = 10 , textvariable = qty1 ).place(x = x_val , y = 75 )
entries = tk.Entry(root , bg = "black" , fg = "white" , width = 20 , bd = 10 , textvariable = qty2).place(x = x_val , y = 145 )
entries = tk.Entry(root , bg = "black" , fg = "white" , width = 20 , bd = 10 , textvariable = qty3).place(x = x_val , y = 215 )

#Button to trigger Gen Function
button = tk.Button(root , text = "Submit" , font = ("Calibri",25) , bg = "black" , fg = "white" ,  command = gen).place(x = 250 , y = 380 )

root.mainloop()
