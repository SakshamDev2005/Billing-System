import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import date as dt


class CafeBillingSystem:
        
    def __init__(self, master):

        df = pd.read_csv('Files/Items.csv')
        file_range = len(df)
        self.store = {}

        self.master = master
        self.master.title("Cafe Billing System")
        self.master.geometry("1250x600")

        label1 = tk.Label(master, text = "Cafe Billing System", font = ('Arial',30))
        label1.pack(side = tk.TOP)

        self.varname = tk.StringVar()
        self.varphone = tk.StringVar()
        

        #labels 
        for i in range(file_range):
            name = df.at[i,'Items']
            x_pos = df.at[i,'X']
            y_pos = df.at[i,'Y']

            label = tk.Label(master , text = name , fg = "black" , font = ("Arial" , 25) ).place( x = x_pos , y = y_pos )


        #self.spinbox   
        self.spinbox1 = tk.Spinbox(master, to = 20)
        self.spinbox1.place(x = 450 , y = 210)

        self.spinbox2 = tk.Spinbox(master, to = 20)
        self.spinbox2.place(x = 450 , y = 260)
            
        self.spinbox3 = tk.Spinbox(master, to = 20)
        self.spinbox3.place(x = 450 , y = 310)
            
        self.spinbox4 = tk.Spinbox(master, to = 20)
        self.spinbox4.place(x = 450 , y = 360)
        

        #buttons for items
        btn1 = tk.Button(master, text = 'Send', command = lambda:self.Add(self.spinbox1.get(),'Cafe Latte'))
        btn1.place(x = 620 , y = 205)

        btn1 = tk.Button(master, text = 'Send', command = lambda:self.Add(self.spinbox2.get(),'Cappuccino'))
        btn1.place(x = 620 , y = 255)

        btn1 = tk.Button(master, text = 'Send', command = lambda:self.Add(self.spinbox3.get(),'Espresso'))
        btn1.place(x = 620 , y = 305)

        btn1 = tk.Button(master, text = 'Send', command = lambda:self.Add(self.spinbox4.get(),'Cold Coffee'))
        btn1.place(x = 620 , y = 355)


        #submit button   
        Button1 = tk.Button(master, text = "Submit Button", command = lambda:self.Gen())
        Button1.pack(side = tk.BOTTOM, pady = 10)


        #name page

        li1 = {1:['Name',850,250],2:['Phone Number',850,300]}

        for i in li1:
            lbl = tk.Label(master, text = li1[i][0])
            lbl.place(x = li1[i][1] , y = li1[i][2]  )

        self.entry1 = tk.Entry(master, textvariable = self.varname)
        self.entry1.place(x = 950 , y = 250 )

        self.entry2 = tk.Entry(master, textvariable = self.varphone)
        self.entry2.place(x = 950 , y = 300)
        


    def Add(self,value,key_name):
        qty = value
        key = key_name
        self.store.update({key:qty})

    def Validate(self):
        self.name = self.varname.get()
        self.phone = self.varphone.get()

        if self.name.isalpha():
            if self.phone.isdigit():
                if len(self.phone) == 10:
                    return True
                else:
                    messagebox.showerror(title = 'Details Entry', message = "Phone Number should be 10 digits only")
            else:
                messagebox.showerror(title = 'Details Entry', message = "Phone Number should be number only")        
        else:
            messagebox.showerror(title = 'Details Entry', message = "Name should be text only")


    def Gen(self):
        dot = dt.today()
        
        bill_db = pd.read_csv('Files/Bill.csv')
        price_db = pd.read_csv('Files/Items.csv')
        cust_db = pd.read_csv('Files/Customer-Details.csv')

        size1 = len(bill_db.index)
        size2 = len(cust_db.index)

        sub_total = 0


        for i,(key,value) in enumerate(self.store.items()):
            if (price_db.loc[(price_db['Items'] == key)]).bool:
                price = price_db.loc[(price_db['Items'] == key),'Price'].values[0]
                sub_total += (int(price) * int(value))                
        
        
        if self.Validate():
            gst = sub_total * 0.05
            total = sub_total + gst

            try:
                bill_db.loc[size1] = [dot,(size1+1),sub_total,gst,total]
                cust_db.loc[size2] = [dot,(size2+1),self.name,self.phone]

                bill_db.to_csv('Files/Bill.csv',index=False)
                cust_db.to_csv('Files/Customer-Details.csv',index=False)

                messagebox.showinfo(title = 'Details Entry', message = "Entry is made into the database")


                self.spinbox1.delete(0, tk.END) 
                self.spinbox1.insert(0,0)

                self.spinbox2.delete(0, tk.END) 
                self.spinbox2.insert(0,0)

                self.spinbox3.delete(0, tk.END) 
                self.spinbox3.insert(0,0)

                self.spinbox4.delete(0, tk.END) 
                self.spinbox4.insert(0,0)


                self.entry1.delete(0,'end')
                self.entry2.delete(0,'end')
                

            except Exception as e :
                messagebox.showerror(title = 'Details Entry', message = "There is an error while making the entry, Try Again")
                print(e)
        else:
            pass

    
def main():
    root = tk.Tk()
    cafe_billing_system = CafeBillingSystem(root)
    root.mainloop()

main()




