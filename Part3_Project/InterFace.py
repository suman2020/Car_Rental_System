from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import ttk

class RentalSystem(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, CustomerEntry, VehicleEntry,RentalEntry,VehicleReturnEntry,CustomerView,VehicleView):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg = '#3d3d5c')
        self.controller = controller
        self.controller.title("Car Rental System")
        self.controller.geometry("720x720")
        heading_label = tk.Label(self, text="Welcome to the Car Rental System", font=('orbitron', 25, 'bold'),
                                 foreground = 'white', background = '#3d3d5c' )
        heading_label.pack( fill="x", pady=20)



        customer_entry_button = tk.Button(self,font= ('orbitron',10,'bold'), text="Customer Entry",
                            command=lambda: controller.show_frame("CustomerEntry"), relief = 'raised',
                            borderwidth = 5, width = 40, height =3)

        vehicle_entry_button = tk.Button(self,font= ('orbitron',10,'bold'), text="Vehicle Entry",
                            command=lambda: controller.show_frame("VehicleEntry"), relief = 'raised',
                            borderwidth = 5, width = 40, height =3)
        rental_entry_button = tk.Button(self, font=('orbitron', 10, 'bold'), text="Rental Entry",
                                                command=lambda: controller.show_frame("RentalEntry"),
                                                relief='raised',
                                                borderwidth=5, width=40, height=3)
        vehicle_return_entry_button = tk.Button(self, font=('orbitron', 10, 'bold'), text="Vehicle Return Entry",
                                         command=lambda: controller.show_frame("VehicleReturnEntry"), relief='raised',
                                         borderwidth=5, width=40, height=3)
        customer_view_button = tk.Button(self, font=('orbitron', 10, 'bold'), text="View Customer Info",
                                                command=lambda: controller.show_frame("CustomerView"),
                                                relief='raised',
                                                borderwidth=5, width=40, height=3)
        vehicle_view_button = tk.Button(self, font=('orbitron', 10, 'bold'), text="View Vehicle Info",
                                         command=lambda: controller.show_frame("VehicleView"),
                                         relief='raised',
                                         borderwidth=5, width=40, height=3)
        customer_entry_button.pack(pady=10)
        vehicle_entry_button.pack(pady=10)
        rental_entry_button.pack(pady=10)
        vehicle_return_entry_button.pack(pady=10)
        customer_view_button.pack(pady=10)
        vehicle_view_button.pack(pady=10)

class CustomerEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c' )
        self.controller = controller
        heading_label = tk.Label(self, text="New Customer Info", font=('orbitron', 25, 'bold'),
                                 foreground='white', background='#3d3d5c')
        heading_label.pack(fill="x", pady=20)


        self.name = tk.Label(self, text='Name', font=('bold', 20))
        self.name.place(x=30, y=90)
        self.name_entry = tk.Entry(self, width=30,font=('bold', 20))
        self.name_entry.place(x=120, y=90)

        self.phone = tk.Label(self, text='Phone', font=('bold', 20))
        self.phone.place(x=30, y=140)
        self.phone_entry = tk.Entry(self, width=30,font=('bold', 20))
        self.phone_entry.place(x=120, y=140)

        def insertCustomerInfo():
            if (self.name_entry.get() == "" or self.phone_entry.get() == ""):
                MessageBox.showinfo(" STATUS", "All fields are required to enter")

            else:

                mydb = mysql.connect(host="localhost", user="root", password="Miracle177636$", database="car_rental")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO CUSTOMER(Name, Phone) VALUES (%s,%s)",
                                 (self.name_entry.get(), self.phone_entry.get()))
                mydb.commit()
                MessageBox.showinfo("STATUS", "Data Stored successfully")
                self.name_entry.delete(0, 'end')
                self.phone_entry.delete(0, 'end')
                mydb.close()

        done = tk.Button(self, font=('orbitron', 7, 'bold'), text="Done",
                          command=insertCustomerInfo, relief='raised', borderwidth=5,
                          width=20, height=3, pady=10,  bg='#d1d1e0')
        done.place(x= 100, y= 200)
        home = tk.Button(self, font=('orbitron', 7, 'bold'), text="Home",
                            command=lambda: controller.show_frame("HomePage"), relief='raised', borderwidth=5,
                            width=20, height=3, pady =10, bg='#d1d1e0')

        home.place(x=100, y=280)




class VehicleEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg = '#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self, text="Vehicle Registration", font=('orbitron', 25, 'bold'),
                                 foreground='white', background='#3d3d5c')
        heading_label.pack(fill="x", pady=20)

        self.vin = tk.Label(self, text='VehicleID', font=('bold', 15))
        self.vin.place(x=30, y=90)
        self.vin_entry = tk.Entry(self, width=25,font=('bold', 15))
        self.vin_entry.place(x=140, y=90)

        self.vehicle = tk.Label(self, text='Description', font=('bold', 15))
        self.vehicle.place(x=30, y=140)
        self.vehicle_entry =tk.Entry(self, width=25,font=('bold', 15))
        self.vehicle_entry.place(x=140, y=140)

        self.year = tk.Label(self, text='Year', font=('bold', 15))
        self.year.place(x=30, y=190)
        self.year_entry = tk.Entry(self, width=25,font=('bold', 15))
        self.year_entry.place(x=140, y=190)

        self.type = tk.Label(self, text='Type', font=('bold', 15))
        self.type.place(x=30, y=240)
        self.type_entry = ttk.Combobox(self, width=23,font=('bold', 15), state = 'readonly')
        self.type_entry['values']= (' ', '1', '2','3', '4', '5', '6')
        self.type_entry.current(0)
        self.type_entry.place(x=140, y=240)

        self.type_entry1 = ttk.Combobox(self, width=13, font=('bold', 15), state='readonly')
        self.type_entry1['values'] = ('Type Info ', '1 : Compact', '2 : Medium ', '3 : Large', '4 : SUV ', '5 : Truck ', '6 : VAN ')
        self.type_entry1.current(0)
        self.type_entry1.place(x=430, y=240)

        self.category = tk.Label(self, text='Category', font=('bold', 15))
        self.category.place(x=30, y=290)
        self.category_entry = ttk.Combobox(self, width=23,font=('bold', 15),state ='readonly')
        self.category_entry['values'] = (' ', '0', '1')
        self.category_entry.current(0)
        self.category_entry.place(x=140, y=290)

        self.category_entry1 = ttk.Combobox(self, width=13, font=('bold', 15), state='readonly')
        self.category_entry1['values'] = (
                    'Category Info ', '0 : Basic', '1 : Luxury ')
        self.category_entry1.current(0)
        self.category_entry1.place(x=430, y=290)

        def insertVehicleInfo():
            if (self.vin_entry.get() == "" or self.vehicle_entry.get() == "" or self.year_entry.get() == "" or
                    self.type_entry.get() == "" or self.category_entry.get()==""):
                MessageBox.showinfo(" STATUS", "All fields are required to enter")

            else:
                year_int = int(self.year_entry.get())
                type_int = int(self.type_entry.get())
                category_int = int(self.category_entry.get())
                mydb = mysql.connect(host="localhost", user="root", password="Miracle177636$", database="car_rental")
                mycursor = mydb.cursor()
                mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
                mycursor.execute("INSERT INTO VEHICLE(VehicleID, Description, Year, Type, Category) VALUES (%s,%s,%s,%s,%s)",
                                 (self.vin_entry.get(), self.vehicle_entry.get(), year_int,type_int, category_int))
                mydb.commit()
                MessageBox.showinfo("STATUS", "Data Stored successfully")
                self.vin_entry.delete(0, 'end')
                self.year_entry.delete(0, 'end')
                self.vehicle_entry.delete(0, 'end')
                self.type_entry.current(0)
                self.type_entry1.current(0)
                self.category_entry.current(0)
                self.category_entry1.current(0)
                mydb.close()

        home = tk.Button(self, font=('orbitron', 7, 'bold'), text="Home",
                            command=lambda: controller.show_frame("HomePage"), relief='raised', borderwidth=5,
                            width=20, height=3,pady=10,  bg='#d1d1e0')
        done = tk.Button(self, font=('orbitron', 7, 'bold'), text="DONE",
                            command=insertVehicleInfo, relief='raised', borderwidth=5,
                            width=20, height=3, pady=10,  bg='#d1d1e0')
        done.place(x=100, y=360)
        home.place(x=100,y=430)

class RentalEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg = '#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self, text="Add a Rental Info", font=('orbitron', 25, 'bold'),
                                 foreground='white', background='#3d3d5c')
        heading_label.pack(fill="x", pady=20)



class VehicleReturnEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c' )
        self.controller = controller
        heading_label = tk.Label(self, text="Return Rented Car", font=('orbitron', 25, 'bold'),
                                 foreground='white', background='#3d3d5c')
        heading_label.pack(fill="x", pady=20)

        self.return_date = tk.Label(self, text='Return Date', font=('bold', 17))
        self.return_date.place(x=30, y=90)
        self.return_date_entry = tk.Entry(self, width=25, font=('bold', 18))
        self.return_date_entry.place(x=210, y=90)

        self.name = tk.Label(self, text='Customer Name', font=('bold', 17))
        self.name.place(x=30, y=140)
        self.name_entry = tk.Entry(self, width=25, font=('bold', 18))
        self.name_entry.place(x=210, y=140)

        self.vehicle = tk.Label(self, text='Vehicle ID', font=('bold', 17))
        self.vehicle.place(x=30, y=190)
        self.vehicle_entry = tk.Entry(self, width=25, font=('bold', 18))
        self.vehicle_entry.place(x=210, y=190)

        def updateRental():
            if (self.name_entry.get() == "" or self.vehicle_entry.get() == "" or self.return_date_entry.get() == ""):
                MessageBox.showinfo(" STATUS", "All fields are required to enter")

            else:
                mydb = mysql.connect(host="localhost", user="root", password="Miracle177636$", database="car_rental")
                mycursor = mydb.cursor()
                mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
                sql = ("SELECT TotalAmount FROM RENTAL,CUSTOMER WHERE ReturnDate = %s AND VehicleID = %s AND Name = %s AND RENTAL.CustID = CUSTOMER.CustID")
                values = (self.return_date_entry.get(),self.vehicle_entry.get(), self.name_entry.get(),)
                mycursor.execute(sql,values)
                myresult = mycursor.fetchall()
                row_count = mycursor.rowcount
                if row_count == 0:

                    MessageBox.showerror("STATUS", "No results found\nPlease input correct data")
                else:
                    MessageBox.showinfo("INFO", "Total Amount Due is %s" % myresult[0])
                    query = ("""UPDATE RENTAL, CUSTOMER
                                SET PaymentDate = CASE WHEN RENTAL.PaymentDate IS NULL THEN RENTAL.ReturnDate ELSE RENTAL.PaymentDate END, Returned = 1
                                WHERE ReturnDate = %s AND VehicleID = %s AND CUSTOMER.Name = %s AND RENTAL.CustID = CUSTOMER.CustID""")
                    values = (self.return_date_entry.get(), self.vehicle_entry.get(), self.name_entry.get(),)
                    mycursor.execute(query,values)

                    mydb.commit()
                    MessageBox.showinfo("STATUS", "Data Stored successfully")
                    self.name_entry.delete(0, 'end')
                    self.vehicle_entry.delete(0, 'end')
                    self.return_date_entry.delete(0, 'end')
                    mydb.close()

        done = tk.Button(self, font=('orbitron', 7, 'bold'), text="Done",
                         command=updateRental, relief='raised', borderwidth=5,
                         width=20, height=3, pady=10, bg='#d1d1e0')
        done.place(x=100, y=280)
        home = tk.Button(self, font=('orbitron', 7, 'bold'), text="Home",
                         command=lambda: controller.show_frame("HomePage"), relief='raised', borderwidth=5,
                         width=20, height=3, pady=10, bg='#d1d1e0')

        home.place(x=100, y=360)


class CustomerView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        heading_label = tk.Label(self, text="Customer Info", font=('orbitron', 25, 'bold'),
                                 foreground='white', background='#3d3d5c')
        heading_label.pack(fill="x", pady=20)

        self.search = tk.Label(self, text='Search', font=('bold', 15))
        self.search.place(x=30, y=90)
        self.search_entry = tk.Entry(self, width=25, font=('bold', 15))
        self.search_entry.place(x=150, y=90)


        self.orderBy = tk.Label(self, text='OrderBy', font=('bold', 15))
        self.orderBy.place(x=30, y=140)
        self.orderBy_entry = ttk.Combobox(self, width=23, font=('bold', 15), state='readonly')
        self.orderBy_entry['values'] = ('SELECT ', 'CustomerID', 'CustomerName','RentalBalance')
        self.orderBy_entry.current(0)
        self.orderBy_entry.place(x=140, y=140)

        list = tk.Listbox(self, font = ('orbitron', 15, 'bold' ), height =15)
        list.place(x=50, y=290, width =500)

        list.delete(0, list.size())
        def resetValues():
            list.delete(0, list.size())
            self.orderBy_entry.current(0)

        def outputInformation():
            list.delete(0,list.size())


            if self.search_entry.get() == "":

                mydb = mysql.connect(host="localhost", user="root", password="Miracle177636$", database="car_rental")
                mycursor = mydb.cursor()

                if (str(self.orderBy_entry.get()) == 'CustomerID'):
                    mycursor.execute(
                        "SELECT CustomerID, CustomerName,SUM(RentalBalance) FROM vrentalinfo GROUP BY CustomerID ORDER BY CustomerID ")
                elif (str(self.orderBy_entry.get()) == 'CustomerName'):
                    mycursor.execute(
                        "SELECT CustomerID, CustomerName,SUM(RentalBalance) FROM vrentalinfo GROUP BY CustomerID ORDER BY CustomerName ")
                elif (str(self.orderBy_entry.get()) == "RentalBalance"):
                    mycursor.execute(
                        "SELECT CustomerID, CustomerName,SUM(RentalBalance) FROM vrentalinfo GROUP BY CustomerID ORDER BY RentalBalance ")
                else:
                    mycursor.execute(
                        "SELECT CustomerID, CustomerName,SUM(RentalBalance) FROM vrentalinfo GROUP BY CustomerID ORDER BY RentalBalance ")
                result = mycursor.fetchall()
                row_count = mycursor.rowcount
                list.insert(list.size() + 1, 'CustomerID       Name              RemainingBalance')

                for row in result:

                    float_value = "%0.2f"%(row[2],)
                    sign = '$'+str(float_value)
                    datA = f'{str(row[0]):<12}  {row[1]:<15} {sign:>20}'
                    list.insert(list.size() + 1, datA)

                count_row = "Total rows returned :" + str(row_count)
                list.insert(list.size() + 1, count_row)
                mydb.commit()
                self.search_entry.delete(0, 'end')

                mydb.close()

            else:
                mydb = mysql.connect(host="localhost", user="root", password="Miracle177636$", database="car_rental")
                mycursor = mydb.cursor()

                if (str(self.orderBy_entry.get()) == "RentalBalance"):
                    sql = (
                        "SELECT CustomerID, CustomerName,SUM(RentalBalance) FROM vrentalinfo WHERE CustomerID = %s OR CustomerName LIKE %s GROUP BY CustomerID ORDER BY RentalBalance ")
                elif (str(self.orderBy_entry.get()) == "CustomerID"):
                    sql = (
                        "SELECT CustomerID, CustomerName,SUM(RentalBalance) FROM vrentalinfo WHERE CustomerID = %s OR CustomerName LIKE %s GROUP BY CustomerID ORDER BY CustomerID ")
                elif(str(self.orderBy_entry.get()) == "CustomerName"):
                    sql = (
                        "SELECT CustomerID, CustomerName,SUM(RentalBalance) FROM vrentalinfo WHERE CustomerID = %s OR CustomerName LIKE %s GROUP BY CustomerID ORDER BY CustomerName ")

                else:
                    sql = (
                        "SELECT CustomerID, CustomerName,SUM(RentalBalance) FROM vrentalinfo WHERE CustomerID = %s OR CustomerName LIKE %s GROUP BY CustomerID ORDER BY RentalBalance")

                values = (self.search_entry.get(), "%" + self.search_entry.get() + "%",)
                mycursor.execute(sql, values)
                result = mycursor.fetchall()
                row_count = mycursor.rowcount
                if row_count == 0:
                    list.insert(list.size()+1,"Customer with the entered information not found.")
                    list.insert(list.size()+1, "Please validate your information")
                else:
                    list.insert(list.size()+1, 'CustomerID       Name              RemainingBalance')
                    for row in result:
                        float_value = "%0.2f" % (row[2],)
                        sign = '$' + str(float_value)
                        datA = str(row[0]) + '               '+ row[1]+'         '+ sign
                        list.insert(list.size()+1, datA)
                count_row = "Total rows returned :"+ str(row_count)
                list.insert(list.size()+1, count_row)
                mydb.commit()
                self.search_entry.delete(0, 'end')
                mydb.close()

        done = tk.Button(self, font=('orbitron', 5, 'bold'), text="Done",
                         command=outputInformation, relief='raised', borderwidth=5,
                         width=20, height=3, pady=10, bg='#d1d1e0')
        done.place(x=50, y=190)
        home = tk.Button(self, font=('orbitron', 5, 'bold'), text="Home",
                         command=lambda: controller.show_frame("HomePage"), relief='raised', borderwidth=5,
                         width=20, height=3, pady=10, bg='#d1d1e0')

        home.place(x=150, y=190)
        reset = tk.Button(self, font=('orbitron', 5, 'bold'), text="Reset",
                         command= resetValues, relief='raised', borderwidth=5,
                         width=20, height=3, pady=10, bg='#d1d1e0')

        reset.place(x=250, y=190)

class VehicleView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        heading_label = tk.Label(self, text="Vehicle Info", font=('orbitron', 25, 'bold'),
                                 foreground='white', background='#3d3d5c')
        heading_label.pack(fill="x", pady=20)

        self.search = tk.Label(self, text='Search', font=('bold', 15))
        self.search.place(x=30, y=90)
        self.search_entry = tk.Entry(self, width=25, font=('bold', 15))
        self.search_entry.place(x=150, y=90)


        self.orderBy = tk.Label(self, text='OrderBy', font=('bold', 15))
        self.orderBy.place(x=30, y=140)
        self.orderBy_entry = ttk.Combobox(self, width=23, font=('bold', 15), state='readonly')
        self.orderBy_entry['values'] = ('SELECT ', 'VIN', 'Description','AverageDailyPrice')
        self.orderBy_entry.current(0)
        self.orderBy_entry.place(x=140, y=140)

        list = tk.Listbox(self, font = ('orbitron', 15, 'bold' ), height =15)
        list.place(x=50, y=290, width =620)

        list.delete(0, list.size())
        def resetValues():
            list.delete(0, list.size())
            self.orderBy_entry.current(0)

        def outputInformation():
            list.delete(0,list.size())


            if self.search_entry.get() == "":

                mydb = mysql.connect(host="localhost", user="root", password="Miracle177636$", database="car_rental")
                mycursor = mydb.cursor()

                if (str(self.orderBy_entry.get()) == 'VIN'):
                    mycursor.execute(
                        "SELECT VIN, Vehicle, AVG(OrderAmount / TotalDays) AS AverageDailyPrice FROM vrentalinfo GROUP BY VIN ORDER BY VIN ")
                elif (str(self.orderBy_entry.get()) == 'Description'):
                    mycursor.execute(
                        "SELECT VIN, Vehicle,AVG(OrderAmount / TotalDays) AS AverageDailyPrice FROM vrentalinfo GROUP BY VIN ORDER BY Vehicle ")
                elif (str(self.orderBy_entry.get()) == "AverageDailyPrice"):
                    mycursor.execute(
                        "SELECT VIN, Vehicle,AVG(OrderAmount / TotalDays) AS AverageDailyPrice FROM vrentalinfo GROUP BY VIN ORDER BY AverageDailyPrice ")
                else:
                    mycursor.execute(
                        "SELECT VIN, Vehicle,AVG(OrderAmount / TotalDays) AS AverageDailyPrice FROM vrentalinfo GROUP BY VIN ORDER BY AverageDailyPrice ")
                result = mycursor.fetchall()
                row_count = mycursor.rowcount
                vin = 'VIN'
                vehicle = 'Vehicle'
                avg = 'AverageDailyPrice'
                headding = f'{vin:<38}  {vehicle:^25} {avg:>10}'
                list.insert(list.size() + 1, headding)

                for row in result:

                    float_value = "%0.2f"%(row[2],)
                    sign = '$'+str(float_value)
                    datA = f'{str(row[0]):<28} {row[1]:<20} {sign:>10}'
                    list.insert(list.size() + 1, datA)

                count_row = "Total rows returned :" + str(row_count)
                list.insert(list.size() + 1, count_row)
                mydb.commit()
                self.search_entry.delete(0, 'end')

                mydb.close()

            else:
                mydb = mysql.connect(host="localhost", user="root", password="Miracle177636$", database="car_rental")
                mycursor = mydb.cursor()
                if (str(self.orderBy_entry.get()) == 'AverageDailyPrice'):
                    sql = ("SELECT VIN, Vehicle, AVG(OrderAmount / TotalDays) AS AverageDailyPrice FROM vrentalinfo WHERE VIN = %s OR Vehicle LIKE %s  GROUP BY VIN ORDER BY AverageDailyPrice")
                else:
                    sql = (
                        "SELECT VIN, Vehicle, AVG(OrderAmount / TotalDays) AS AverageDailyPrice FROM vrentalinfo WHERE VIN = %s OR Vehicle LIKE  %s GROUP BY VIN ORDER BY AverageDailyPrice  ")
                values = (self.search_entry.get(), "%" + self.search_entry.get() + "%",)
                mycursor.execute(sql, values)
                result = mycursor.fetchall()
                row_count = mycursor.rowcount
                if row_count == 0:
                    list.insert(list.size()+1,"Vehicle with the entered information not found.")
                    list.insert(list.size()+1, "Please validate your information")
                else:
                    list.insert(list.size() + 1, 'VIN                                      VEHICLE              AverageDailyPrice')

                    for row in result:
                        float_value = "%0.2f" % (row[2],)
                        sign = '$' + str(float_value)
                        datA = str(row[0]) + '           '+ row[1]+'              '+ sign
                        list.insert(list.size()+1, datA)
                count_row = "Total rows returned :"+ str(row_count)
                list.insert(list.size()+1, count_row)
                mydb.commit()
                self.search_entry.delete(0, 'end')
                mydb.close()

        done = tk.Button(self, font=('orbitron', 5, 'bold'), text="Done",
                         command=outputInformation, relief='raised', borderwidth=5,
                         width=20, height=3, pady=10, bg='#d1d1e0')
        done.place(x=50, y=190)
        home = tk.Button(self, font=('orbitron', 5, 'bold'), text="Home",
                         command=lambda: controller.show_frame("HomePage"), relief='raised', borderwidth=5,
                         width=20, height=3, pady=10, bg='#d1d1e0')

        home.place(x=150, y=190)
        reset = tk.Button(self, font=('orbitron', 5, 'bold'), text="Reset",
                         command= resetValues, relief='raised', borderwidth=5,
                         width=20, height=3, pady=10, bg='#d1d1e0')

        reset.place(x=250, y=190)


if __name__ == "__main__":

    interface = RentalSystem()
    interface.mainloop()