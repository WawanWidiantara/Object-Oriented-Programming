import tkinter as tk
import  tkinter.messagebox
from tkinter import ttk, END
import sqlite3
import pandas as pd
import self
import datetime
from openpyxl.workbook import Workbook



# This class manages all the operations around the main window.
#This allows data to be entered
class mainwindow():
    #This function manages the main window
    def __init__(self, master):
        self.master = master # Top level master, all windows work off this window.
        self.frameholder_LEDGER = tk.Frame(self.master)
        self.frameholder_ENTRY = tk.Frame(self.master)
        self.frameholder_LEDGER.pack()


        self.buttonfilter = tk.Button(self.master, text="Filter data", width=19, command = lambda: ledgerfilter.filterdata(self))
        self.buttonfilter.place(relx=0.86, rely=0.08)

        self.buttonexport = tk.Button(self.master, text="Export Data", width=19,command = lambda: exportdata.exporttoexcel(self))
        self.buttonexport.place(relx=0.86, rely=0.15)

        self.buttonexport = tk.Button(self.master, text="Exit", width=10, command=self.master.destroy)
        self.buttonexport.place(relx=0.90, rely=0.90)

        # This brings in the data to populate into the treeview
        conn = sqlite3.connect("tkinter_dbase.db")  # connect database
        c = conn.cursor()  # create cursor
        c.execute('select ROWID, * from LEDGER_POSTING')
        df = pd.DataFrame(c)
        df.columns = ['Record_ID', 'Date', 'Amount', 'ledger_no', 'posting_type', 'Debit/Credit']
        self.ledgernolist = list(set(df['ledger_no'])) # creates a unique list of ledger nos


        self.frameholder_LEDGER = tk.LabelFrame(master, text="General Ledger Entries")
        self.frameholder_LEDGER.place(height=200, width=800, relx=0.28, rely=0)

        self.tree = ttk.Treeview(self.frameholder_LEDGER)
        self.tree.place(relheight=1.0, relwidth=1.0)  # fill the whole container with the treeview
        self.tree["column"] = list(df.columns)
        self.tree["show"] = "headings"
        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.tree.insert("", "end", values=row)
        self.tree.column("Record_ID", anchor='center', width=8)
        self.tree.column("Date", anchor='center', width=68)
        self.tree.column("Amount", anchor='center', width=50)
        self.tree.column("ledger_no", anchor='center', width=30)
        self.tree.column("posting_type", anchor='center', width=100)
        self.tree.column("Debit/Credit", anchor='center', width=20)

        # adding scroolbars
        self.treescrolly = tk.Scrollbar(self.frameholder_LEDGER, orient="vertical", command=self.tree.yview)
        self.treescrollx = tk.Scrollbar(self.frameholder_LEDGER, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set)
        self.treescrollx.pack(side="bottom", fill="x")
        self.treescrolly.pack(side="right", fill="y")

        # LABEL CREATION
        # X = y positioning from the left of the window,
        # y is downward positioning from top of window

        self.label_LTNAME = tk.Label(self.master, text="Type")
        self.label_LTNAME.place(relx=0.02, rely=0.05)

        self.label_LTNO = tk.Label(self.master, text="Ledger No")
        self.label_LTNO.place(relx=0.02, rely=0.12)

        self.label_LTNO = tk.Label(self.master, text="DR/CR")
        self.label_LTNO.place(relx=0.02, rely=0.20)

        self.label_AMOUNT = tk.Label(self.master, text="AMOUNT")
        self.label_AMOUNT.place(relx=0.02, rely=0.30)

        #TEXTBOX CREATION

        self.text_LTNO = ttk.Entry(self.master, width = 25) # this is linked to whatever value is populated in label_LTNO
        self.text_LTNO.place(relx=0.08, rely=0.12)


        self.text_DRCR = ttk.Entry(self.master, width = 5) # put whatever value needed in here
        self.text_DRCR.place(relx=0.08, rely=0.20)

        self.text_AMOUNT = ttk.Entry(self.master, width = 25) # put whatever value needed in here
        self.text_AMOUNT.place(relx=0.08, rely=0.30)

        #Button

        self.buttonSUBMIT = tk.Button(self.master, text="Submit", command = lambda: mainwindow.buttonsubmit(self))
        self.buttonSUBMIT.place(x=20, y=170)

        #Dropdown creation - cound to combochange method
        self.combo_dropdown_values = ttk.Combobox(self.master,width=23)
        self.combo_dropdown_values.place(relx=0.08, rely=0.05)
        self.combo_dropdown_values.bind("<<ComboboxSelected>>", self.combochange)


        self.tree.bind("<ButtonRelease-1>",self.single_click)  # ===> This is the bind of the single click event to the function that will give us the information we need.

        self.buttonupdaterecord = tk.Button(self.master, text="Update/Delete Record",
                                            command=lambda: updaterecordclass.updaterecord(self), width=19)

        self.buttonupdaterecord.place(relx=0.86, rely=0.01)

        #### FILTERED SECTION ####

        self.conn = sqlite3.connect("tkinter_dbase.db")  # connect database
        self.c = conn.cursor()  # create cursor
        self.c.execute('select ROWID, * from LEDGER_POSTING')
        self.df_filter = pd.DataFrame(self.c)
        self.df_filter.columns = ['Record_ID', 'Date', 'Amount', 'ledger_no', 'posting_type', 'Debit/Credit']




        self.frameholder_ledger_filter = tk.LabelFrame(master, text="Filtered Ledger Entries")
        self.frameholder_ledger_filter.place(height=200, width=800, relx=0.28, rely=.50)

        self.treefilter = ttk.Treeview(self.frameholder_ledger_filter)
        self.treefilter.place(relheight=1.0, relwidth=1.0)  # fill the whole container with the treeview
        self.treefilter["column"] = list(df.columns)
        self.treefilter["show"] = "headings"




        for column in self.treefilter["columns"]:
            self.treefilter.heading(column, text=column)
        self.df_rows_filter = self.df_filter.to_numpy().tolist()
        for row in self.df_rows_filter:
            self.treefilter.insert("", "end", values=row)
        self.treefilter.column("Record_ID", anchor='center', width=8)
        self.treefilter.column("Date", anchor='center', width=68)
        self.treefilter.column("Amount", anchor='center', width=50)
        self.treefilter.column("ledger_no", anchor='center', width=30)
        self.treefilter.column("posting_type", anchor='center', width=100)
        self.treefilter.column("Debit/Credit", anchor='center', width=20)

        # adding scroolbars
        self.treescrolly = tk.Scrollbar(self.frameholder_ledger_filter, orient="vertical", command=self.treefilter.yview)
        self.treescrollx = tk.Scrollbar(self.frameholder_ledger_filter, orient="horizontal", command=self.treefilter.xview)
        self.treefilter.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set)
        self.treescrollx.pack(side="bottom", fill="x")
        self.treescrolly.pack(side="right", fill="y")

        self.populatecombobox(self)

    #treeview window single click
    #method to manage a single click on the main tree on the top on the main window, and capturing data for the row that was clicked.
    def single_click(self,event):
        self.rowfocus = event.widget.focus()  # ===> This focuses the program on the row single clicked
        self.rowid = event.widget.item(self.rowfocus)  # ===> This captures the row id that was clicked
        self.rowitems = self.rowid['values']  # ===> This captures the values in the row seperately clicked on.
        self.rowinformation = self.rowitems[0:6]  # ===> thie returns the values in the row for each column in a list
        #print("The row information is:", self.rowinformation)


        self.recordid = self.rowinformation[0]
        self.postingdate = self.rowinformation[1]
        self.amount = self.rowinformation[2]
        self.ledgerno = self.rowinformation[3]
        self.desc = self.rowinformation[4]
        self.ledgertype = self.rowinformation[5]



    def new_window(self):
        self.newWindow = tk.Toplevel(self.master) # Creates a new window as the main application window within this class

    #Step 1 - Loading of data to that will help to manage the user selection before submission to the database.

    #method to mange the population of the combobox values
    def populatecombobox(self,event):
        # This function populates the combobox and creates four dictionaries
        self.conn = sqlite3.connect("tkinter_dbase.db")  # connect database
        self.c = self.conn.cursor()  # create cursor
        self.c.execute('select * from POST_TYPE')
        self.posting_type = [] # creating a empty list
        self.ledger_no = [] #  creating a empty list
        self.combo_dropdown = [] #  creating a empty list
        self.drcr = [] #  creating a empty list

        #loops through the values returned from sql query
        for self.i in self.c.fetchall():
            self.posting_type.append(self.i[0])  # Adds in the values for each row in the first column
            self.ledger_no.append(self.i[1])  # Adds in the values for each row in the second column
            self.drcr.append(self.i[2]) # Adds in the values for each row in the third column
            self.combo_dropdown.append(self.i[3]) # Creates a list of values that can be populated into the combo dropdown (from 4th column)


        self.combo_dropdown_values['values'] = self.combo_dropdown  # this populates the combobox with the values from self.combo_dropdown.append(self.i[3])
        self.conn.close()  # ===> Important this is included, closes the database connection, good for security.
        # CREATION OF DICTIONARIES
        #CONVERTS LISTS ABOVE INTO DICTIONARIES, USEFUL FOR LOOPING THRUGH FURTHER DOWN AND COMPARING VALUES
        #KEY,VALUE PAIRS CREATED HERE
        self.posting_type = dict(enumerate(self.posting_type))  # converts list to dictionary with index values as keys.
        self.ledger_no = dict(enumerate(self.ledger_no))  # converts list to dictionary with index values as keys.
        self.combo_dropdown = dict(enumerate(self.combo_dropdown))  # converts list to dictionary with index values as keys.
        self.drcr = dict(enumerate(self.drcr))  # converts list to dictionary with index values as keys.
        return self.posting_type, self.ledger_no, self.combo_dropdown, self.drcr  # ===> Return values that are passed to combochange function


    #Method to manage the interface updates everytime the combobox value is changed
    def combochange(self,evemt):
        #Retrieves each dictionary from the  self.populatecombobox method
        self.ptype,self.ledgerno,self.combodrop,self.drcrval = self.populatecombobox(self)
        self.capturecombosel = self.combo_dropdown_values.get() # ===> Captures the values from the combobox dropdown box chosen as a tuple
        for self.keys, self.value in self.combodrop.items(): #Dict of values pulled from the database
            for self.i,self.j in self.ledgerno.items(): #Dict of values pulled from the database
                for self.ff, self.gg in self.drcrval.items(): #Dict of values pulled from the database
                  if self.value == self.capturecombosel and self.keys == self.i and self.keys == self.ff:
                      # Populating the textbox with the Ledger value associated with the capturecombosel value entered
                      self.text_LTNO.config(state=tk.NORMAL) #===> #Need this line in here, so that we can clear out the text box, when changing combox values
                      self.text_LTNO.delete('0', END)
                      self.text_LTNO.insert(END,self.j)
                      self.text_LTNO.config(state=tk.DISABLED)
                      #Populating the textbox with the DR/CR value associated with the capturecombosel value entered
                      self.text_DRCR.config(state=tk.NORMAL)  # ===> #Need this line in here, so that we can clear out the text box, when changing combox values
                      self.text_DRCR.delete('0', END)
                      self.text_DRCR.insert(END, self.gg)
                      self.text_DRCR.config(state=tk.DISABLED)

    #Step2 - Submission of the data to the database.

    # Inserts a record into the database
    def buttonsubmit(self):

        self.combobox_LTNAME_submit = self.combo_dropdown_values.get()
        self.text_LTNO_submit = self.text_LTNO.get()
        self.text_AMOUNT_submit = self.text_AMOUNT.get()
        self.text_DRCR_submit = self.text_DRCR.get()
        #Captures the date now to submit to the database.
        self.today = datetime.datetime.now()
        self.today_date = self.today.strftime("%d/%m/%Y")

        # Making sure all three fields populated before submitting to the database
        if (len(self.text_LTNO.get()) == 0) or (len(self.text_AMOUNT.get()) == 0 or len(self.combo_dropdown_values.get()) == 0):
            tkinter.messagebox.showinfo("Submit", "All fields need to be populated, nothing saved")
        else:
            self.conn = sqlite3.connect("tkinter_dbase.db")  # connect database
            self.c = self.conn.cursor()  # create cursor
            self.c.execute(
                "INSERT INTO LEDGER_POSTING (POSTING_DATE,AMOUNT, LEDGER_TYPE_NO,DESCRIPTION,LEDGER_TYPE) VALUES(?,?,?,?,?)",
                (self.today_date, self.text_AMOUNT_submit, self.text_LTNO_submit, self.combobox_LTNAME_submit, self.text_DRCR_submit))
            self.conn.commit()  # This line physcially enters the data onto the database, if excluded the code will run but the database will not update.
            self.conn.close()
            tkinter.messagebox.showinfo("Data saved", "Data saved, the table above should refresh with your new data")
            self.clearTextInput()
            self.refreshtree()

    #Method to clear out what was submitted so the data cant be entered twice in error.
    def clearTextInput(self):
        self.combo_dropdown_values.delete('0', END)
        self.text_LTNO.delete('0', END)
        self.text_AMOUNT.delete('0', END)
        self.text_DRCR.delete('0', END)

    #Method that refreshes the screen and populates the trees with the updated information from the database table.
    def refreshtree(self):
        self.master.destroy() #closes window
        main() #reopens window

#This exports the data to excel
class exportdata(mainwindow):


    def exporttoexcel(self):
        conn = sqlite3.connect("tkinter_dbase.db")  # connect database
        c = conn.cursor()  # create cursor
        c.execute('select ROWID, * from LEDGER_POSTING')
        df = pd.DataFrame(c)
        df.columns = ['Record_ID', 'Date', 'Amount', 'ledger_no', 'posting_type', 'Debit/Credit']

        rawdata = df

        rawdata.to_excel(r'C:/Users/haugh/OneDrive/dataanalyticsireland/YOUTUBE/TKINTER/connect_to_SQLITE_db_acc/crud.xlsx',
                         sheet_name='Export', index=False,engine='openpyxl')

#This updates the database records
class updaterecordclass():
            def __init__(self, root):
                self.master = root
                self.frame = tk.Frame(self.master)
                self.quitButton = tk.Button(self.master, text='Quit', width=25)
                self.quitButton.pack()
                self.frame.pack()

            def close_window(self):
               self.newWindowUpdate.destroy()

            #Creates newWindowUpdate window that will hold buttons, labels etc to allow data to be updated
            def updaterecord(self):
                self.newWindowUpdate = tk.Toplevel(self.master) # Is a child of the master within this class
                self.newWindowUpdate.title("Update/Delete Record")
                self.newWindowUpdate.geometry("300x250")

            # Labels

                self.label_ROWID = tk.Label(self.newWindowUpdate, text="Record ID")
                self.label_ROWID.place(relx=0.01, rely=0.01)

                self.label_AMOUNT = tk.Label(self.newWindowUpdate, text="Amount")
                self.label_AMOUNT.place(relx=0.01, rely=0.15)

                self.label_LedgerNo = tk.Label(self.newWindowUpdate, text="LedgerNo")
                self.label_LedgerNo.place(relx=0.01, rely=0.30)

                self.label_PTYPE = tk.Label(self.newWindowUpdate, text="Posting Type")
                self.label_PTYPE.place(relx=0.01, rely=0.45)

                self.label_DRCR = tk.Label(self.newWindowUpdate, text="Debit/Credit")
                self.label_DRCR.place(relx=0.01, rely=0.60)

                # Textbox

                self.text_ROWID = ttk.Entry(self.newWindowUpdate, width=25)  # this is linked to whatever value is populated in label_LTNO
                self.text_ROWID.place(relx=0.28, rely=0.01)
                self.text_ROWID.config(state=tk.DISABLED)

                self.text_AMOUNT = ttk.Entry(self.newWindowUpdate, width=25)  # this is linked to whatever value is populated in label_LTNO
                self.text_AMOUNT.place(relx=0.28, rely=0.15)

                self.text_LEDGERNO = ttk.Entry(self.newWindowUpdate, width=25)  # this is linked to whatever value is populated in label_LTNO
                self.text_LEDGERNO.place(relx=0.28, rely=0.30)
                self.text_LEDGERNO.config(state=tk.DISABLED)

                self.text_PTYPE = ttk.Entry(self.newWindowUpdate, width=25)  # this is linked to whatever value is populated in label_LTNO
                self.text_PTYPE.place(relx=0.28, rely=0.45)
                self.text_PTYPE.config(state=tk.DISABLED)

                self.text_DRCR = ttk.Entry(self.newWindowUpdate, width=25)  # this is linked to whatever value is populated in label_LTNO
                self.text_DRCR.place(relx=0.28, rely=0.60)
                self.text_DRCR.config(state=tk.DISABLED)

                self.buttonexit = tk.Button(self.newWindowUpdate, text="Exit", command=lambda: updaterecordclass.close_window(self), width=10)
                self.buttonexit.place(relx=0.65, rely=0.85)

                self.buttonupdatedbase = tk.Button(self.newWindowUpdate, text="Save changes",
                                                   command=lambda: updaterecordclass.updatedbase(self), width=10) #Call the class then the method
                self.buttonupdatedbase.place(relx=0.35, rely=0.85)

                self.buttonupdatedeldbase = tk.Button(self.newWindowUpdate, text="Delete record",
                                                      command=lambda: updaterecordclass.delfromdbase(self), width=10) #Call the class then the method
                self.buttonupdatedeldbase.place(relx=0.05, rely=0.85)

                self.recordid_noupdate = self.recordid
                self.amount_update = self.amount
                self.ledgerno_noupdate = self.ledgerno
                self.desc_noupdate = self.desc
                self.ledgertype_noupdate = self.ledgertype

                self.text_ROWID.config(state=tk.NORMAL)  # ===> #Need this line in here, so that we can clear out the text box, when changing combox values
                self.text_ROWID.delete('0', END)
                self.text_ROWID.insert(END, self.recordid_noupdate)
                self.text_ROWID.config(state=tk.DISABLED)

                self.text_AMOUNT.config(state=tk.NORMAL)  # ===> #Need this line in here, so that we can clear out the text box, when changing combox values
                self.text_AMOUNT.delete('0', END)
                self.text_AMOUNT.insert(END, self.amount_update)

                self.text_LEDGERNO.config(state=tk.NORMAL)  # ===> #Need this line in here, so that we can clear out the text box, when changing combox values
                self.text_LEDGERNO.delete('0', END)
                self.text_LEDGERNO.insert(END, self.ledgerno_noupdate)
                self.text_LEDGERNO.config(state=tk.DISABLED)

                self.text_PTYPE.config(state=tk.NORMAL)  # ===> #Need this line in here, so that we can clear out the text box, when changing combox values
                self.text_PTYPE.delete('0', END)
                self.text_PTYPE.insert(END, self.desc_noupdate)
                self.text_PTYPE.config(state=tk.DISABLED)

                self.text_DRCR.config(state=tk.NORMAL)  # ===> #Need this line in here, so that we can clear out the text box, when changing combox values
                self.text_DRCR.delete('0', END)
                self.text_DRCR.insert(END, self.ledgertype_noupdate)
                self.text_DRCR.config(state=tk.DISABLED)

            #Updates the database with the new amount
            def updatedbase(self):
                conn = sqlite3.connect("tkinter_dbase.db")  # connect to database
                c = conn.cursor()  # create cursor
                c.execute('UPDATE LEDGER_POSTING SET AMOUNT=? WHERE ROWID =?', (self.text_AMOUNT.get(), self.text_ROWID.get()))
                conn.commit()  # This line physcially enters the data onto the database, if excluded the code will run but the database will not update.
                c.close()
                tkinter.messagebox.showinfo("Record updated","Record no " + " " + self.text_ROWID.get() + " " + "updated with amount" + " " + self.text_AMOUNT.get())
                mainwindow.refreshtree(self)
            #deletes from the database
            def delfromdbase(self):
                conn = sqlite3.connect("tkinter_dbase.db")  # connect to database
                c = conn.cursor()  # create cursor
                c.execute('DELETE FROM LEDGER_POSTING WHERE ROWID =? AND AMOUNT=? AND LEDGER_TYPE_NO=? AND LEDGER_TYPE=?',
                          (self.text_ROWID.get(),self.text_AMOUNT.get(),self.text_LEDGERNO.get(),self.text_DRCR.get()))
                conn.commit()  # This line physcially enters the data onto the database, if excluded the code will run but the database will not update.
                c.close()
                tkinter.messagebox.showinfo("Record deleted ","Record no " + " " + self.text_ROWID.get() + " " + "deleted from the database")
                mainwindow.refreshtree(self)

                self.master.mainloop()

#This filters the data by ledger no
class ledgerfilter(mainwindow):

    def __init__(self, master):
        self.master = root
        self.frame = tk.Frame(self.master)
        self.quitButton.pack()
        self.frame.pack()



    def filterdata(self):
        #### FILTERED SECTION ####
        self.filterwindow = tk.Toplevel(self.master)
        self.filterwindow.title("Filter Data")
        self.filterwindow.geometry("300x150")  # width X Heigth
        self.filterwindow.attributes('-topmost', True) # Keeps the popup window to the front.

        self.label_date_filter = tk.Label(self.filterwindow, text="Ledger No")
        self.label_date_filter.place(relx=0.02, rely=0.10)

        self.ledgernofilter = ttk.Entry(self.filterwindow, width=25)
        self.ledgernofilter.place(relx=0.25, rely=0.10)

        self.applyfilter = tk.Button(self.filterwindow, text="Apply Filter", width=10,
                                     command=lambda: ledgerfilter.filtertreeview(self))
        self.applyfilter.place(relx=0.35, rely=0.25)

        self.buttonclose = tk.Button(self.filterwindow, text="Exit", width=10,
                                     command=lambda: ledgerfilter.close_window(self))
        self.buttonclose.place(relx=0.65, rely=0.65)

    def checkledgerlist(self):
        for self.i in self.ledgernolist:
            valentered = self.ledgernofilter.get()
            if str(self.i) == valentered: # Convert i to a string to allow comparison as it initially returns as am integer
                return True

    def filtertreeview(self):

        if self.ledgernofilter.get() == "":
           tkinter.messagebox.showinfo("Empty Value","Empty values not allowed, please supply a ledger no")
        elif self.ledgernofilter.get() != "" and ledgerfilter.checkledgerlist(self) == True:


            self.conn = sqlite3.connect("tkinter_dbase.db")  # connect database
            self.c = self.conn.cursor()  # create cursor
            self.c.execute('select ROWID, * FROM LEDGER_POSTING WHERE LEDGER_TYPE_NO =?',(self.ledgernofilter.get(),))
            self.df_filter_rows = pd.DataFrame(self.c)
            self.df_filter_rows.columns = ['Record_ID', 'Date', 'Amount', 'ledger_no', 'posting_type', 'Debit/Credit']

            self.frameholder_ledger_filter = tk.LabelFrame(self.master, text="Filtered Ledger Entries")
            self.frameholder_ledger_filter.place(height=200, width=800, relx=0.28, rely=.50)

            self.treefilter = ttk.Treeview(self.frameholder_ledger_filter)
            self.treefilter.place(relheight=1.0, relwidth=1.0)  # fill the whole container with the treeview
            self.treefilter["column"] = list(self.df_filter_rows.columns)
            self.treefilter["show"] = "headings"
            self.filterwindow.destroy()
        else:
            tkinter.messagebox.showinfo("Incorrect value", "Value entered not valid, please enter a correct one.")
            self.filterwindow
            self.filterwindow.attributes('-topmost', True)  # Keeps the popup window to the front.





        for column in self.treefilter["columns"]:
            self.treefilter.heading(column, text=column)
        self.df_rows_filter = self.df_filter_rows.to_numpy().tolist()

        for row in self.df_rows_filter:
            self.treefilter.insert("", "end", values=row)
        self.treefilter.column("Record_ID", anchor='center', width=8)
        self.treefilter.column("Date", anchor='center', width=68)
        self.treefilter.column("Amount", anchor='center', width=50)
        self.treefilter.column("ledger_no", anchor='center', width=30)
        self.treefilter.column("posting_type", anchor='center', width=100)
        self.treefilter.column("Debit/Credit", anchor='center', width=20)

        # adding scroolbars
        self.treescrolly = tk.Scrollbar(self.frameholder_ledger_filter, orient="vertical",
                                        command=self.treefilter.yview)
        self.treescrollx = tk.Scrollbar(self.frameholder_ledger_filter, orient="horizontal",
                                        command=self.treefilter.xview)
        self.treefilter.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set)
        self.treescrollx.pack(side="bottom", fill="x")
        self.treescrolly.pack(side="right", fill="y")

    def close_window(self):
        self.filterwindow.destroy()

        self.master.mainloop()
def main(): # You manage the main window look and feel through here
    root = tk.Tk()
    root.geometry("1400x450")  # ===> width X Height
    root.title("Accounting Entry")  # screen title
    frameholder_ENTRY = tk.LabelFrame(root, text="Data entry")
    frameholder_ENTRY.place(height=335, width=300, relx=0.01, rely=0)
    app = mainwindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()


