from tkinter import *
import tkinter.font as font
import mysql.connector
import numpy as np
from datetime import date, timedelta
from PIL import Image, ImageTk

conn = mysql.connector.connect(user="root", password="root", host="127.0.0.1", database="hoteldb",
                               auth_plugin="mysql_native_password")
cur = conn.cursor(buffered=True)

root = Tk()
# root.resizable(width=True, height=True)
image = Image.open("bg/vg5.jpg")
photo_image = ImageTk.PhotoImage(image)
background = Label(root, image=photo_image)
background.place(relx=.5, rely=.5, anchor="center")
background.lower()

facilities_image = Image.open("bg/vg6.jpg")
facilities_photo_image = ImageTk.PhotoImage(facilities_image)

booking_image = Image.open("bg/vg7.jpg")
booking_photo_image = ImageTk.PhotoImage(booking_image)

view_booking_image = Image.open("bg/vg2.jpg")
view_booking_photo_image = ImageTk.PhotoImage(view_booking_image)

update_booking_image = Image.open("bg/vg3.jpg")
update_booking_photo_image = ImageTk.PhotoImage(update_booking_image)

find_update_image = Image.open("bg/vg1.jpg")
find_update_photo_image = ImageTk.PhotoImage(find_update_image)

find_image = Image.open("bg/vg4.jpg")
find_photo_image = ImageTk.PhotoImage(find_image)

find_image = Image.open("bg/vg9.jpg")
update_photo_image = ImageTk.PhotoImage(find_image)

delete_find_image = Image.open("bg/vg10.jpg")
delete_find_photo_image = ImageTk.PhotoImage(delete_find_image)

delete_image = Image.open("bg/vg11.jpg")
delete_photo_image = ImageTk.PhotoImage(delete_image)

pay_image = Image.open("bg/vg8.jpg")
pay_photo_image = ImageTk.PhotoImage(pay_image)

vpay_image = Image.open("bg/vg12.jpg")
vpay_photo_image = ImageTk.PhotoImage(vpay_image)

root.configure(background='white')
root.geometry("1920x1080")
# root.iconify()
# root.state('zoomed')
# root.state('zoom')
# root.attributes('-fullscreen', True)


root.iconify()
root.title("RDBMS Hotel")
font1 = font.Font(family="Bebas Neue", size=70)
font2 = font.Font(family="Bebas Neue", size=40)
font3 = font.Font(family="Bison Bold", size=30)
font4 = font.Font(family="Bebas Kai", size=20)
font5 = font.Font(family="LibelSuitRg-Regular", size=18)
font6 = font.Font(family="LibelSuitRg-Regular", size=25)
font7 = font.Font(family="Calibri italic", size=30)
font8 = font.Font(family="hack", size=20)
font9 = font.Font(family="Calibri", size=20)
font10 = font.Font(family="Amarillo", size=40)
font11 = font.Font(family="highlight", size=70)

cur.execute("CREATE DATABASE IF NOT EXISTS hoteldb")
cur.execute("USE hoteldb")

cur.execute('''

 CREATE TABLE IF NOT EXISTS CUSTOMER
    (
        first_name char(50) NOT NULL,
        last_name char(50) NOT NULL,
        phone_number char(20) PRIMARY KEY,
        email char(50) NOT NULL UNIQUE,
        address char(100) NOT NULL,
        city char(50) NOT NULL,
        zipcode integer NOT NULL   
    );

''')
cur.execute('''

 CREATE TABLE IF NOT EXISTS BOOKING
    (
        room_number integer NOT NULL UNIQUE,
        check_in char(20) NOT NULL,
        verification char(20) NOT NULL,
        days integer NOT NULL,
        adults integer NOT NULL,
        children integer NOT NULL,
        room_type char(20) NOT NULL       
    );

''')

cur.execute('''

  CREATE TABLE IF NOT exists DATA AS 
    (
    SELECT * FROM CUSTOMER,BOOKING
    );

''')

label1 = Label(root, text="Rdbms Hotel", anchor=CENTER, bg="white")
label1["font"] = font10
label1.pack(pady=160)

label2 = Label(root, text="Enhancing Life around great food.\n 'Customers may forget what you said "
                          "\nbut they will never forget how you made them feel'", anchor=W, justify=CENTER, bg="white")
label2["font"] = font7
label2.pack(pady=1)

label3 = Label(root, text='''
622 Ventura Boulevard, 
Beverly Hills, 556644 
United States of America
U.S.A
''', justify=CENTER, anchor=CENTER, bg="white")
label3["font"] = font8
label3.pack(pady=20)


def home():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    button_next.destroy()


    global hlabel1
    hlabel1 = Label(root, text="HOTEL RDBMS WELCOMES YOU !", bg="white", anchor=CENTER)
    hlabel1["font"] = font1
    hlabel1.pack(pady=8)

    global frame1
    frame1 = LabelFrame(root, padx=200, pady=150, bg="white")
    frame1["font"] = font4
    frame1.pack(pady=4)

    global hlabel2
    hlabel2 = Label(frame1, text="List of contents", bg="white", anchor=CENTER)
    hlabel2["font"] = font11
    hlabel2.pack(pady=2)

    global button1
    button1 = Button(frame1, text="Facilities", bg="white", padx=15, pady=0, command=facilities)
    button1['font'] = font4
    button1.pack(pady=2)

    global button2
    button2 = Button(frame1, text="Booking", bg="white", padx=15, pady=0, command=booking)
    button2['font'] = font4
    button2.pack(pady=2)

    global button3
    button3 = Button(frame1, text="View Bookings", bg="white", padx=15, pady=0, command=view)
    button3['font'] = font4
    button3.pack(pady=2)

    global button4
    button4 = Button(frame1, text="Update Bookings", bg="white", padx=15, pady=0, command=update)
    button4['font'] = font4
    button4.pack(pady=2)

    global button5
    button5 = Button(frame1, text="Delete Bookings", bg="white", padx=15, pady=0, command=delete)
    button5['font'] = font4
    button5.pack(pady=2)

    global button6
    button6 = Button(frame1, text="View Payments", bg="white", padx=15, pady=0, command=view_payment)
    button6['font'] = font4
    button6.pack(pady=2)

    global button_exit
    button_exit = Button(frame1, text="Exit", bg="white", padx=15, pady=0, command=destroy_root)
    button_exit['font'] = font4
    button_exit.pack(pady=2)


def destroy_root():
    root.quit()


def facilities():
    global win1
    win1 = Toplevel()
    # win1.configure(background='white')
    win1.geometry("1920x1080")
    # win1.attributes('-fullscreen', True)
    win1.title("Facilities")

    background = Label(win1, image=facilities_photo_image)
    background.place(relx=.5, rely=.5, anchor="center")
    background.lower()

    global label1
    label1 = Label(win1, text="Hotel Facilities", bg="white", anchor=CENTER)
    label1["font"] = font11
    label1.pack(pady=10)

    facilities = '''
• Airport Hotel Courtesy Desk• Bakery / Patisserie• Barbeque Facilities
• Beach• Beauty Parlour• Bicycle Trail
• Business Centre• Child Care Services• Children Playground
• Concierge• Drug Store• Dry Cleaning
• Executive Lounge• Express Check-In• Express Check-Out
• Fitness Centre / Health Club• Florist• Game Center / Room
• Gift Shop / Newstand• Golf - Mini Golf• Golf Course
• Hairdresser / Barber• Handicapped Facilities• Hiking Trails
• In Room Air Condition• In Room Video Games• Internet Service
• Jacuzzi• Jogging Track• Laundry
• Limousine Service• Parking• Parking - Valet• Penthouse
• Pharmacy• Pub/ Bar• Restaurant
• Room Service• Safe Deposit Box• Sauna
• Shopping Arcade• Shopping Center / Mall• Shuttle Service
• Spa• Sun Deck• Swimming - Children Waddle Pool
• Swimming Pool
    '''
    global label2
    label1 = Label(win1, text=facilities, bg="white", anchor=CENTER)
    label1["font"] = font9
    label1.pack()

    global button_exit
    button_exit = Button(win1, text="Exit", bg="white", padx=15, pady=0, command=destroy_facilites)
    button_exit['font'] = font4
    button_exit.pack(anchor=S)


def destroy_facilites():
    win1.destroy()


def booking():
    global win2
    win2 = Toplevel()
    win2.configure(background='white')
    win2.geometry("1920x1080")
    # win2.attributes('-fullscreen', True)
    win2.title("Booking")

    background = Label(win2, image=booking_photo_image)
    background.place(relx=.5, rely=.5, anchor="center")
    background.lower()

    global blabel1, blabel2, blabel3, blabel4, blabel5, blabel6, blabel7, blabel8, \
        blabel9, blabel10, blabel11, blabel12, blabel13, blabel14, blabel15
    global first_name, last_name, phone, email, address, city, zip, \
        room_number, check_in, verification, days, adults, children, rtype

    blabel1 = Label(win2, text="Booking Details", bg="white")
    blabel1["font"] = font11

    blabel2 = Label(win2, text="First Name", bg="white")
    blabel3 = Label(win2, text="Last Name", bg="white")
    blabel4 = Label(win2, text="Phone Number", bg="white")
    blabel5 = Label(win2, text="Email", bg="white")
    blabel6 = Label(win2, text="Address", bg="white")
    blabel7 = Label(win2, text="City", bg="white")
    blabel8 = Label(win2, text="Zipcode", bg="white")
    blabel9 = Label(win2, text="Room Number", bg="white")
    blabel10 = Label(win2, text="Check In", bg="white")
    blabel11 = Label(win2, text="Verification", bg="white")
    blabel12 = Label(win2, text="No. of Days", bg="white")
    blabel13 = Label(win2, text="No. of Adults", bg="white")
    blabel14 = Label(win2, text="No. of Children", bg="white")
    blabel15 = Label(win2, text="Room Type", bg="white")

    blabel1.place(x=1200, y=20)
    blabel2.place(x=400, y=200)
    blabel3.place(x=400, y=300)
    blabel4.place(x=400, y=400)
    blabel5.place(x=400, y=500)
    blabel6.place(x=400, y=600)
    blabel7.place(x=400, y=700)
    blabel8.place(x=400, y=800)
    blabel9.place(x=1000, y=200)
    blabel10.place(x=1000, y=300)
    blabel11.place(x=1000, y=400)
    blabel12.place(x=1000, y=500)
    blabel13.place(x=1000, y=600)
    blabel14.place(x=1000, y=700)
    blabel15.place(x=1000, y=800)

    blabel2["font"] = font9
    blabel3["font"] = font9
    blabel4["font"] = font9
    blabel5["font"] = font9
    blabel6["font"] = font9
    blabel7["font"] = font9
    blabel8["font"] = font9
    blabel9["font"] = font9
    blabel10["font"] = font9
    blabel11["font"] = font9
    blabel12["font"] = font9
    blabel13["font"] = font9
    blabel14["font"] = font9
    blabel15["font"] = font9

    large_font = ('Verdana', 15)

    first_name = Entry(win2, width=20, borderwidth=2, font=large_font)
    last_name = Entry(win2, width=20, borderwidth=2, font=large_font)
    phone = Entry(win2, width=20, borderwidth=2, font=large_font)
    email = Entry(win2, width=20, borderwidth=2, font=large_font)
    address = Entry(win2, width=25, borderwidth=2, font=large_font)
    city = Entry(win2, width=20, borderwidth=2, font=large_font)
    zip = Entry(win2, width=20, borderwidth=2, font=large_font)

    rooms_list = np.arange(100, 151, 1)
    rooms_list = list(rooms_list)
    room_number_clicked = IntVar()
    room_number_clicked.set(100)
    room_number = OptionMenu(win2, room_number_clicked, *rooms_list)
    room_number.config(bg="white", borderwidth=0, font=large_font)

    sdate = date(2020, 1, 1)  # start date
    edate = date(2020, 1, 31)  # end date

    delta = edate - sdate  # as timedelta

    check_in_list = []
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        check_in_list.append(day)

    check_in_list_clicked = StringVar()
    check_in_list_clicked.set("2020-01-01")
    check_in = OptionMenu(win2, check_in_list_clicked, *check_in_list)
    check_in.config(bg="white", borderwidth=0, font=large_font)

    verfication_list = ["Aadhar Card", "Passport", "Driver's Licence", "ID Card"]
    verification_clicked = StringVar()
    verification_clicked.set("Aadhar Card")
    verification = OptionMenu(win2, verification_clicked, *verfication_list)
    verification.config(bg="white", borderwidth=0, font=large_font)

    days_list = np.arange(1, 8, 1)
    days_list = list(days_list)
    days_list_clicked = IntVar()
    days_list_clicked.set(1)
    days = OptionMenu(win2, days_list_clicked, *days_list)
    days.config(bg="white", borderwidth=0, font=large_font)

    adults_list = np.arange(1, 4, 1)
    adults_list = list(adults_list)
    adults_list_clicked = IntVar()
    adults_list_clicked.set(1)
    adults = OptionMenu(win2, adults_list_clicked, *adults_list)
    adults.config(bg="white", borderwidth=0, font=large_font)

    children_list = np.arange(0, 5, 1)
    children_list = list(children_list)
    children_list_clicked = IntVar()
    children_list_clicked.set(1)
    children = OptionMenu(win2, children_list_clicked, *children_list)
    children.config(bg="white", borderwidth=0, font=large_font)

    rtype = ["Standard", "Deluxe", "Luxury"]
    rtype_clicked = StringVar()
    rtype_clicked.set("Standard")
    rtype = OptionMenu(win2, rtype_clicked, *rtype)
    rtype.config(bg="white", borderwidth=0, font=large_font)

    first_name.place(x=620, y=210)
    last_name.place(x=620, y=310)
    phone.place(x=620, y=410)
    email.place(x=620, y=510)
    address.place(x=620, y=610)
    city.place(x=620, y=710)
    zip.place(x=620, y=810)
    room_number.place(x=1300, y=200)
    check_in.place(x=1300, y=300)
    verification.place(x=1300, y=400)
    days.place(x=1300, y=500)
    adults.place(x=1300, y=600)
    children.place(x=1300, y=700)
    rtype.place(x=1300, y=800)

    def save():
        f_name = first_name.get()
        l_name = last_name.get()
        pno = phone.get()
        mail = email.get()
        addr = address.get()
        cit = city.get()
        zp = zip.get()
        rno = room_number_clicked.get()
        cin = check_in_list_clicked.get()
        ver = verification_clicked.get()
        day = days_list_clicked.get()
        adl = adults_list_clicked.get()
        chld = children_list_clicked.get()
        rt = rtype_clicked.get()

        null1 = (None, None, None, None, None, None, None)
        null2 = (None, None, None, None, None, None, None)
        null3 = (None, None, None, None, None, None, None, None, None, None, None, None, None, None)

        query1 = "INSERT INTO CUSTOMER (first_name,last_name,phone_number,email,address,city,zipcode)" \
                 "VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val1 = (f_name, l_name, pno, mail, addr, cit, zp)

        query2 = "INSERT INTO BOOKING (room_number,check_in,verification,days,adults,children,room_type)" \
                 "VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val2 = (rno, cin, ver, day, adl, chld, rt)

        query3 = "INSERT INTO DATA (first_name,last_name,phone_number,email,address,city,zipcode," \
                 "room_number,check_in,verification,days,adults,children,room_type) " \
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val3 = (f_name, l_name, pno, mail, addr, cit, zp, rno, cin, ver, day, adl, chld, rt)

        if (((len(f_name) > 0 and len(l_name) > 0) and (len(pno) > 0 and len(mail) > 0) and (
                len(addr) > 0 and len(cit) > 0))):
            print("Successful Insert Not Null !")
            cur.execute(query1, val1)
            cur.execute(query2, val2)
            cur.execute(query3, val3)
            # conn.commit()

        else:
            print("Unsuccessful Insert Not Null !")
            cur.execute(query1, null1)
            cur.execute(query2, null2)
            cur.execute(query3, null3)

        first_name.delete(0, END)
        last_name.delete(0, END)
        phone.delete(0, END)
        email.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        zip.delete(0, END)

    def payment():
        global win10
        win10 = Toplevel()
        win10.configure(background='white')
        win10.geometry("1920x1080")
        # win10.attributes('-fullscreen', True)
        win10.title("Payment")

        background = Label(win10, image=pay_photo_image)
        background.place(relx=.5, rely=.5, anchor="center")
        background.lower()

        global plabel1, plabel2, plabel3, plabel4, plabel5, plabel6, plabel7, plabel8, \
            plabel9, plabel10, plabel11, plabel12, plabel13, plabel14, plabel15

        plabel1 = Label(win10, text="Payment Screen", bg="white")
        plabel1["font"] = font11

        plabel2 = Label(win10, text="First Name", bg="white")
        plabel3 = Label(win10, text="Last Name", bg="white")
        plabel4 = Label(win10, text="Phone Number", bg="white")
        plabel5 = Label(win10, text="Mode of Payment", bg="white")
        plabel6 = Label(win10, text="Payment ID", bg="white")
        plabel7 = Label(win10, text="Amount", bg="white")

        large_font = ('Verdana', 15)

        first_name = Entry(win10, width=20, borderwidth=2, font=large_font)
        last_name = Entry(win10, width=20, borderwidth=2, font=large_font)
        phone = Entry(win10, width=20, borderwidth=2, font=large_font)
        pay = Entry(win10, width=25, borderwidth=2, font=large_font)
        amount = Entry(win10, width=20, borderwidth=2, font=large_font)

        mode_list = ["Credit/Debit Card", "Cash", "PayTm", "Net Banking"]
        mode_clicked = StringVar()
        mode_clicked.set("Credit/Debit Card")
        mode = OptionMenu(win10, mode_clicked, *mode_list)
        mode.config(bg="white", borderwidth=0, font=large_font)

        plabel1.pack(pady=20)
        plabel2.place(x=700, y=200)
        plabel3.place(x=700, y=300)
        plabel4.place(x=700, y=400)
        plabel5.place(x=700, y=500)
        plabel6.place(x=700, y=600)
        plabel7.place(x=700, y=700)

        first_name.place(x=930, y=205)
        last_name.place(x=930, y=305)
        phone.place(x=930, y=405)
        mode.place(x=930, y=505)
        pay.place(x=930, y=605)
        amount.place(x=930, y=705)

        plabel2["font"] = font9
        plabel3["font"] = font9
        plabel4["font"] = font9
        plabel5["font"] = font9
        plabel6["font"] = font9
        plabel7["font"] = font9

        def pay_amount():
            f_name = first_name.get()
            l_name = last_name.get()
            pno = phone.get()
            mop = mode_clicked.get()
            pid = pay.get()
            amt = amount.get()

            cur.execute('''
             CREATE TABLE IF NOT EXISTS PAYMENT
                (
                    first_name char(50) NOT NULL,
                    last_name char(50) NOT NULL,
                    phone_number char(20),
                    mode_of_payment char(50) NOT NULL,
                    pid char(100) PRIMARY KEY,
                    amount char(50) NOT NULL,
                    FOREIGN KEY (phone_number) REFERENCES CUSTOMER(phone_number) ON UPDATE CASCADE
                );
            ''')

            null = (None, None, None, None, None, None, None)

            query = "INSERT INTO PAYMENT (first_name,last_name,phone_number,mode_of_payment,pid,amount)" \
                    "VALUES (%s,%s,%s,%s,%s,%s);"
            val = (f_name, l_name, pno, mop, pid, amt)

            if (((len(f_name) > 0 and len(l_name) > 0) and (len(pno) > 0 and len(mop) > 0) and (
                    len(pid) > 0 and len(amt) > 0))):
                print("Successful Insert Not Null !")
                cur.execute(query, val)
                conn.commit()

            else:
                print("Unsuccessful Insert Not Null !")
                cur.execute(query, null)

            first_name.delete(0, END)
            last_name.delete(0, END)
            phone.delete(0, END)
            pay.delete(0, END)
            amount.delete(0, END)

        global pay_exit
        pay_exit = Button(win10, text="Pay & Exit", bg="white", padx=15, pady=0,
                          command=lambda: [pay_amount(), destroy_payment()])
        pay_exit['font'] = font4
        pay_exit.place(x=880, y=900)

    global button_save
    button_save = Button(win2, text="Pay", bg="white", padx=15, pady=0,
                         command=lambda: [save(), payment()])
    button_save['font'] = font4
    button_save.place(x=800, y=900)

    global booking_exit
    booking_exit = Button(win2, text="Exit", bg="white", padx=15, pady=0, command=destroy_booking)
    booking_exit['font'] = font4
    booking_exit.place(x=980, y=900)


def destroy_payment():
    win10.destroy()


def destroy_booking():
    win2.destroy()


def view():
    global win3
    win3 = Toplevel()
    win3.configure(background='white')
    win3.geometry("1920x1080")
    # win3.attributes('-fullscreen', True)
    win3.title("Booking")

    background = Label(win3, image=view_booking_photo_image)
    background.place(relx=.5, rely=.5, anchor="center")
    background.lower()

    global vlabel1, vlabel2, vlabel3, vlabel4, vlabel5
    global first_name, last_name, phone

    vlabel1 = Label(win3, text="Find Customer Details", bg="white")
    vlabel1["font"] = font11

    vlabel2 = Label(win3, text="First Name", bg="white")
    vlabel3 = Label(win3, text="Last Name", bg="white")
    vlabel4 = Label(win3, text="Phone Number", bg="white")

    vlabel1.place(x=300, y=50)
    vlabel2.place(x=600, y=400)
    vlabel3.place(x=600, y=500)
    vlabel4.place(x=600, y=600)

    vlabel2["font"] = font3
    vlabel3["font"] = font3
    vlabel4["font"] = font3

    large_font = ('Verdana', 15)
    first_name = Entry(win3, width=30, borderwidth=2, font=large_font)
    last_name = Entry(win3, width=30, borderwidth=2, font=large_font)
    phone = Entry(win3, width=30, borderwidth=2, font=large_font)

    first_name.place(x=950, y=410)
    last_name.place(x=950, y=510)
    phone.place(x=950, y=610)

    def find():
        global win4
        win4 = Toplevel()
        win4.configure(background='white')
        win4.geometry("1920x1080")
        # win4.attributes('-fullscreen', True)
        win4.title("Booking")

        background = Label(win4, image=find_photo_image)
        background.place(relx=.5, rely=.5, anchor="center")
        background.lower()

        global flabel1, flabel2, flabel3, flabel4, flabel5, flabel6, flabel7, flabel8, \
            flabel9, flabel10, flabel11, flabel12, flabel13, flabel14, flabel15

        f_name = first_name.get()
        l_name = last_name.get()
        pno = phone.get()

        sql = '''
        SELECT * FROM DATA
        WHERE first_name = %s and last_name = %s and phone_number = %s
        '''
        val = (str(f_name), str(l_name), int(pno))
        cur.execute(sql, val)

        results = cur.fetchone()
        find_list = []

        for x in results:
            print(x)
            find_list.append(x)

        first_name.delete(0, END)
        last_name.delete(0, END)
        phone.delete(0, END)

        find_dict = {"First Name": find_list[0], "Last Name": find_list[1], "Phone Number": find_list[2],
                     "Email": find_list[3], "Address": find_list[4], "City": find_list[5], "Zipcode": find_list[6],
                     "Room Number": find_list[7], "Check In": find_list[8], "Verification": find_list[9],
                     "No. of Days": find_list[10],
                     "No. of Adults": find_list[11], "No. of Children": find_list[12], "Room Type": find_list[13]
                     }

        print(find_dict)
        print(find_list[0])
        print(type(find_list[0]))

        flabel1 = Label(win4, text="Booking Details", bg="white")
        flabel1["font"] = font11

        flabel2 = Label(win4, text="First Name: {}".format(find_list[0]), bg="white")
        flabel3 = Label(win4, text="Last Name: {}".format(find_list[1]), bg="white")
        flabel4 = Label(win4, text="Phone Number: {}".format(find_list[2]), bg="white")
        flabel5 = Label(win4, text="Email: {}".format(find_list[3]), bg="white")
        flabel6 = Label(win4, text="Address: \n{}".format(find_list[4]), bg="white", justify=LEFT, wraplength=500)
        flabel7 = Label(win4, text="City: {}".format(find_list[5]), bg="white")
        flabel8 = Label(win4, text="Zipcode: {}".format(find_list[6]), bg="white")
        flabel9 = Label(win4, text="Room Number: {}".format(find_list[7]), bg="white")
        flabel10 = Label(win4, text="Check In: {}".format(find_list[8]), bg="white")
        flabel11 = Label(win4, text="Verification: {}".format(find_list[9]), bg="white")
        flabel12 = Label(win4, text="No. of Days: {}".format(find_list[10]), bg="white")
        flabel13 = Label(win4, text="No. of Adults: {}".format(find_list[11]), bg="white")
        flabel14 = Label(win4, text="No. of Children: {}".format(find_list[12]), bg="white")
        flabel15 = Label(win4, text="Room Type: {}".format(find_list[13]), bg="white")

        flabel1.place(x=780, y=70)
        flabel2.place(x=600, y=200)
        flabel3.place(x=600, y=300)
        flabel4.place(x=600, y=400)
        flabel5.place(x=600, y=500)
        flabel6.place(x=600, y=600)
        flabel7.place(x=600, y=700)
        flabel8.place(x=600, y=800)
        flabel9.place(x=1100, y=200)
        flabel10.place(x=1100, y=300)
        flabel11.place(x=1100, y=400)
        flabel12.place(x=1100, y=500)
        flabel13.place(x=1100, y=600)
        flabel14.place(x=1100, y=700)
        flabel15.place(x=1100, y=800)

        flabel2["font"] = font9
        flabel3["font"] = font9
        flabel4["font"] = font9
        flabel5["font"] = font9
        flabel6["font"] = font9
        flabel7["font"] = font9
        flabel8["font"] = font9
        flabel9["font"] = font9
        flabel10["font"] = font9
        flabel11["font"] = font9
        flabel12["font"] = font9
        flabel13["font"] = font9
        flabel14["font"] = font9
        flabel15["font"] = font9

        global find_exit
        find_exit = Button(win4, text="Exit", bg="white", padx=15, pady=0, command=destroy_find)
        find_exit['font'] = font4
        find_exit.place(x=880, y=900)

    global button_find
    button_find = Button(win3, text="Find", bg="white", padx=15, pady=0, command=find)
    button_find['font'] = font4
    button_find.place(x=800, y=900)

    global button_exit
    button_exit = Button(win3, text="Exit", bg="white", padx=15, pady=0, command=destroy_view)
    button_exit['font'] = font4
    button_exit.place(x=980, y=900)


def destroy_view():
    win3.destroy()


def destroy_find():
    flabel1.destroy()
    flabel2.destroy()
    flabel3.destroy()
    flabel4.destroy()
    flabel5.destroy()
    flabel6.destroy()
    flabel7.destroy()
    flabel8.destroy()
    flabel9.destroy()
    flabel10.destroy()
    flabel11.destroy()
    flabel12.destroy()
    flabel13.destroy()
    flabel14.destroy()
    flabel15.destroy()
    win4.destroy()


def update():
    global win5
    win5 = Toplevel()
    win5.configure(background='white')
    win5.geometry("1920x1080")
    # win5.attributes('-fullscreen', True)
    win5.title("Booking")

    background = Label(win5, image=update_booking_photo_image)
    background.place(relx=.5, rely=.5, anchor="center")
    background.lower()

    global ulabel1, ulabel2, ulabel3, ulabel4, ulabel5
    global first_name, phone

    ulabel1 = Label(win5, text="Update Customer Details", bg="white")
    ulabel1["font"] = font11

    ulabel2 = Label(win5, text="First Name", bg="white")
    ulabel3 = Label(win5, text="Phone Number", bg="white")
    ulabel4 = Label(win5, text="Room Number", bg="white")

    ulabel1.pack(pady=20)
    ulabel2.place(x=600, y=400)
    ulabel3.place(x=600, y=500)
    ulabel4.place(x=600, y=600)

    ulabel2["font"] = font3
    ulabel3["font"] = font3
    ulabel4["font"] = font3

    large_font = ('Verdana', 15)
    first_name = Entry(win5, width=30, borderwidth=2, font=large_font)
    phone = Entry(win5, width=30, borderwidth=2, font=large_font)

    uurooms_list_update = np.arange(100, 151, 1)
    uurooms_list_update = list(uurooms_list_update)
    uroom_number_clicked_update = IntVar()
    uroom_number_clicked_update.set(100)
    uroom_number_update = OptionMenu(win5, uroom_number_clicked_update, *uurooms_list_update)
    uroom_number_update.config(bg="white", borderwidth=0, font=large_font)

    first_name.place(x=900, y=410)
    phone.place(x=900, y=510)
    uroom_number_update.place(x=900, y=610)

    def find_update():
        global win6
        win6 = Toplevel()
        win6.configure(background='white')
        win6.geometry("1920x1080")
        # win6.attributes('-fullscreen', True)
        win6.title("Booking")

        background = Label(win6, image=find_update_photo_image)
        background.place(relx=.5, rely=.5, anchor="center")
        background.lower()

        global fulabel1, fulabel2, fulabel3, fulabel4, fulabel5, fulabel6, fulabel7, fulabel8, \
            fulabel9, fulabel10, fulabel11, fulabel12, fulabel13, fulabel14, fulabel15

        f_name = first_name.get()
        pno = phone.get()
        urno = uroom_number_clicked_update.get()

        sql = '''
        SELECT * FROM DATA
        WHERE first_name = %s and phone_number = %s and room_number = %s
        '''
        val = (str(f_name), str(pno), int(urno))
        cur.execute(sql, val)

        results = cur.fetchone()
        find_list = []

        for x in results:
            print(x)
            find_list.append(x)

        first_name.delete(0, END)
        phone.delete(0, END)

        fulabel1 = Label(win6, text="Update Customer Details", bg="white", anchor=CENTER)
        fulabel1["font"] = font11

        fulabel2 = Label(win6, text="First Name: {}".format(find_list[0]), bg="white")
        fulabel3 = Label(win6, text="Last Name: {}".format(find_list[1]), bg="white")
        fulabel4 = Label(win6, text="Phone Number: {}".format(find_list[2]), bg="white")
        fulabel5 = Label(win6, text="Email: {}".format(find_list[3]), bg="white")
        fulabel6 = Label(win6, text="Address: \n{}".format(find_list[4]), bg="white", justify=LEFT, wraplength=500)
        fulabel7 = Label(win6, text="City: {}".format(find_list[5]), bg="white")
        fulabel8 = Label(win6, text="Zipcode: {}".format(find_list[6]), bg="white")
        fulabel9 = Label(win6, text="Room Number: {}".format(find_list[7]), bg="white")
        fulabel10 = Label(win6, text="Check In: {}".format(find_list[8]), bg="white")
        fulabel11 = Label(win6, text="Verification: {}".format(find_list[9]), bg="white")
        fulabel12 = Label(win6, text="No. of Days: {}".format(find_list[10]), bg="white")
        fulabel13 = Label(win6, text="No. of Adults: {}".format(find_list[11]), bg="white")
        fulabel14 = Label(win6, text="No. of Children: {}".format(find_list[12]), bg="white")
        fulabel15 = Label(win6, text="Room Type: {}".format(find_list[13]), bg="white")

        fulabel1.place(x=680, y=70)
        fulabel2.place(x=600, y=200)
        fulabel3.place(x=600, y=300)
        fulabel4.place(x=600, y=400)
        fulabel5.place(x=600, y=500)
        fulabel6.place(x=600, y=600)
        fulabel7.place(x=600, y=700)
        fulabel8.place(x=600, y=800)
        fulabel9.place(x=1100, y=200)
        fulabel10.place(x=1100, y=300)
        fulabel11.place(x=1100, y=400)
        fulabel12.place(x=1100, y=500)
        fulabel13.place(x=1100, y=600)
        fulabel14.place(x=1100, y=700)
        fulabel15.place(x=1100, y=800)

        fulabel2["font"] = font9
        fulabel3["font"] = font9
        fulabel4["font"] = font9
        fulabel5["font"] = font9
        fulabel6["font"] = font9
        fulabel7["font"] = font9
        fulabel8["font"] = font9
        fulabel9["font"] = font9
        fulabel10["font"] = font9
        fulabel11["font"] = font9
        fulabel12["font"] = font9
        fulabel13["font"] = font9
        fulabel14["font"] = font9
        fulabel15["font"] = font9

        def update_details():

            global win7
            win7 = Toplevel()
            win7.configure(background='white')
            win7.geometry("1920x1080")
            # win7.attributes('-fullscreen', True)
            win7.title("Booking")

            background = Label(win7, image=update_photo_image)
            background.place(relx=.5, rely=.5, anchor="center")
            background.lower()

            global udlabel1, udlabel2, udlabel3, udlabel4, udlabel5, udlabel6, udlabel7, udlabel8, \
                udlabel9, udlabel10, udlabel11, udlabel12, udlabel13, udlabel14, udlabel15

            global detector1, detector2
            detector1 = first_name.get()
            detector2 = phone.get()

            udlabel1 = Label(win7, text="Update Customer Details", bg="white")
            udlabel1["font"] = font11

            udlabel2 = Label(win7, text="First Name", bg="white")
            udlabel3 = Label(win7, text="Last Name", bg="white")
            udlabel4 = Label(win7, text="Phone Number", bg="white")
            udlabel5 = Label(win7, text="Email", bg="white")
            udlabel6 = Label(win7, text="Address", bg="white")
            udlabel7 = Label(win7, text="City", bg="white")
            udlabel8 = Label(win7, text="Zipcode", bg="white")
            udlabel9 = Label(win7, text="Room Number", bg="white")
            udlabel10 = Label(win7, text="Check In", bg="white")
            udlabel11 = Label(win7, text="Verification", bg="white")
            udlabel12 = Label(win7, text="No. of Days", bg="white")
            udlabel13 = Label(win7, text="No. of Adults", bg="white")
            udlabel14 = Label(win7, text="No. of Children", bg="white")
            udlabel15 = Label(win7, text="Room Type", bg="white")

            udlabel1.place(x=700, y=70)
            udlabel2.place(x=500, y=200)
            udlabel3.place(x=500, y=300)
            udlabel4.place(x=500, y=400)
            udlabel5.place(x=500, y=500)
            udlabel6.place(x=500, y=600)
            udlabel7.place(x=500, y=700)
            udlabel8.place(x=500, y=800)
            udlabel9.place(x=1100, y=200)
            udlabel10.place(x=1100, y=300)
            udlabel11.place(x=1100, y=400)
            udlabel12.place(x=1100, y=500)
            udlabel13.place(x=1100, y=600)
            udlabel14.place(x=1100, y=700)
            udlabel15.place(x=1100, y=800)

            udlabel2["font"] = font9
            udlabel3["font"] = font9
            udlabel4["font"] = font9
            udlabel5["font"] = font9
            udlabel6["font"] = font9
            udlabel7["font"] = font9
            udlabel8["font"] = font9
            udlabel9["font"] = font9
            udlabel10["font"] = font9
            udlabel11["font"] = font9
            udlabel12["font"] = font9
            udlabel13["font"] = font9
            udlabel14["font"] = font9
            udlabel15["font"] = font9

            large_font = ('Verdana', 15)

            first_name_update = Entry(win7, width=20, borderwidth=2, font=large_font)
            last_name_update = Entry(win7, width=20, borderwidth=2, font=large_font)
            phone_update = Entry(win7, width=20, borderwidth=2, font=large_font)
            email_update = Entry(win7, width=20, borderwidth=2, font=large_font)
            address_update = Entry(win7, width=25, borderwidth=2, font=large_font)
            city_update = Entry(win7, width=20, borderwidth=2, font=large_font)
            zip_update = Entry(win7, width=20, borderwidth=2, font=large_font)

            first_name_update.place(x=720, y=210)
            last_name_update.place(x=720, y=310)
            phone_update.place(x=720, y=410)
            email_update.place(x=720, y=510)
            address_update.place(x=720, y=610)
            city_update.place(x=720, y=710)
            zip_update.place(x=720, y=810)

            rooms_list_update = np.arange(100, 151, 1)
            rooms_list_update = list(rooms_list_update)
            room_number_clicked_update = IntVar()
            room_number_clicked_update.set(100)
            room_number_update = OptionMenu(win7, room_number_clicked_update, *rooms_list_update)
            room_number_update.config(bg="white", borderwidth=0, font=large_font)

            sdate = date(2020, 1, 1)  # start date
            edate = date(2020, 1, 31)  # end date

            delta = edate - sdate  # as timedelta

            check_in_list_update = []
            for i in range(delta.days + 1):
                day = sdate + timedelta(days=i)
                check_in_list_update.append(day)

            check_in_list_clicked_update = StringVar()
            check_in_list_clicked_update.set("2020-01-01")
            check_in_update = OptionMenu(win7, check_in_list_clicked_update, *check_in_list_update)
            check_in_update.config(bg="white", borderwidth=0, font=large_font)

            verfication_list_update = ["Aadhar Card", "Passport", "Driver's Licence", "ID Card"]
            verification_clicked_update = StringVar()
            verification_clicked_update.set("Aadhar Card")
            verification_update = OptionMenu(win7, verification_clicked_update, *verfication_list_update)
            verification_update.config(bg="white", borderwidth=0, font=large_font)

            days_list_update = np.arange(1, 8, 1)
            days_list_update = list(days_list_update)
            days_list_clicked_update = IntVar()
            days_list_clicked_update.set(1)
            days_update = OptionMenu(win7, days_list_clicked_update, *days_list_update)
            days_update.config(bg="white", borderwidth=0, font=large_font)

            adults_list_update = np.arange(1, 4, 1)
            adults_list_update = list(adults_list_update)
            adults_list_clicked_update = IntVar()
            adults_list_clicked_update.set(1)
            adults_update = OptionMenu(win7, adults_list_clicked_update, *adults_list_update)
            adults_update.config(bg="white", borderwidth=0, font=large_font)

            children_list_update = np.arange(0, 5, 1)
            children_list_update = list(children_list_update)
            children_list_clicked_update = IntVar()
            children_list_clicked_update.set(1)
            children_update = OptionMenu(win7, children_list_clicked_update, *children_list_update)
            children_update.config(bg="white", borderwidth=0, font=large_font)

            rtype_update = ["Standard", "Deluxe", "Luxury"]
            rtype_clicked_update = StringVar()
            rtype_clicked_update.set("Standard")
            rtype_update = OptionMenu(win7, rtype_clicked_update, *rtype_update)
            rtype_update.config(bg="white", borderwidth=0, font=large_font)

            room_number_update.place(x=1300, y=200)
            check_in_update.place(x=1300, y=300)
            verification_update.place(x=1300, y=400)
            days_update.place(x=1300, y=500)
            adults_update.place(x=1300, y=600)
            children_update.place(x=1300, y=700)
            rtype_update.place(x=1300, y=800)

            def save_update():
                f_name_update = first_name_update.get()
                l_name_update = last_name_update.get()
                pno_update = phone_update.get()
                mail_update = email_update.get()
                addr_update = address_update.get()
                cit_update = city_update.get()
                zp_update = zip_update.get()
                rno_update = room_number_clicked_update.get()
                cin_update = check_in_list_clicked_update.get()
                ver_update = verification_clicked_update.get()
                day_update = days_list_clicked_update.get()
                adl_update = adults_list_clicked_update.get()
                chld_update = children_list_clicked_update.get()
                rt_update = rtype_clicked_update.get()

                cur.execute("SET SQL_SAFE_UPDATES = 0;")
                sql1 = '''
                UPDATE DATA
                SET first_name=%s,last_name=%s,phone_number=%s,email=%s,address=%s,city=%s,
                zipcode=%s,room_number=%s,check_in=%s,verification=%s,days=%s,adults=%s,
                children=%s,room_type=%s
                WHERE first_name = %s and phone_number = %s
                '''
                val1 = (f_name_update, l_name_update, pno_update, mail_update, addr_update,
                        cit_update, zp_update, rno_update, cin_update, ver_update, day_update, adl_update,
                        chld_update, rt_update, str(f_name), str(pno))
                cur.execute(sql1, val1)

                sql2 = '''
                UPDATE CUSTOMER
                SET first_name=%s,last_name=%s,phone_number=%s,email=%s,address=%s,city=%s,
                zipcode=%s
                WHERE first_name = %s and phone_number = %s
                '''
                val2 = (f_name_update, l_name_update, pno_update, mail_update, addr_update,
                        cit_update, zp_update, str(f_name), str(pno))
                cur.execute(sql2, val2)

                sql3 = '''
                UPDATE PAYMENT
                SET first_name=%s,last_name=%s
                WHERE phone_number = %s
                '''
                val3 = (f_name_update, l_name_update, pno_update)
                cur.execute(sql3, val3)

                sql4 = '''
                UPDATE BOOKING
                SET room_number=%s,check_in=%s,verification=%s,days=%s,adults=%s,
                children=%s,room_type=%s
                WHERE room_number = %s 
                '''
                val4 = (rno_update, cin_update, ver_update, day_update, adl_update,
                        chld_update, rt_update, int(urno))
                cur.execute(sql4, val4)

                conn.commit()

            global button_update
            button_update = Button(win7, text="Update & Exit", bg="white", padx=15, pady=0,
                                   command=lambda: [save_update(), destroy_update_details(), destroy_find_update()])
            button_update['font'] = font4
            button_update.place(x=880, y=900)

        global update_table
        update_table = Button(win6, text="Update", bg="white", padx=15, pady=0, command=lambda: [update_details()])
        update_table['font'] = font4
        update_table.place(x=800, y=900)

        global find_update_exit
        find_update_exit = Button(win6, text="Exit", bg="white", padx=15, pady=0,
                                  command=lambda: [destroy_find_update()])
        find_update_exit['font'] = font4
        find_update_exit.place(x=980, y=900)

    global button_find
    button_find = Button(win5, text="Find", bg="white", padx=15, pady=0, command=find_update)
    button_find['font'] = font4
    button_find.place(x=800, y=900)

    global update_exit
    update_exit = Button(win5, text="Exit", bg="white", padx=15, pady=0, command=destroy_update)
    update_exit['font'] = font4
    update_exit.place(x=980, y=900)


def destroy_update():
    win5.destroy()


def destroy_find_update():
    fulabel1.destroy()
    fulabel2.destroy()
    fulabel3.destroy()
    fulabel4.destroy()
    fulabel5.destroy()
    fulabel6.destroy()
    fulabel7.destroy()
    fulabel8.destroy()
    fulabel9.destroy()
    fulabel10.destroy()
    fulabel11.destroy()
    fulabel12.destroy()
    fulabel13.destroy()
    fulabel14.destroy()
    fulabel15.destroy()
    win6.destroy()


def destroy_update_details():
    win7.destroy()


def delete():
    global win8
    win8 = Toplevel()
    win8.configure(background='white')
    win8.geometry("1920x1080")
    # win8.attributes('-fullscreen', True)
    win8.title("Delete Booking")

    background = Label(win8, image=delete_photo_image)
    background.place(relx=.5, rely=.5, anchor="center")
    background.lower()

    global dlabel1, dlabel2, dlabel3, dlabel4, dlabel5
    global first_name, phone

    dlabel1 = Label(win8, text="Delete Customer Details", bg="white")
    dlabel1["font"] = font11

    dlabel2 = Label(win8, text="First Name", bg="white")
    dlabel3 = Label(win8, text="Phone Number", bg="white")
    dlabel4 = Label(win8, text="Room Number", bg="white")

    dlabel1.pack(pady=20)
    dlabel2.place(x=600, y=400)
    dlabel3.place(x=600, y=500)
    dlabel4.place(x=600, y=600)

    dlabel2["font"] = font3
    dlabel3["font"] = font3
    dlabel4["font"] = font3

    large_font = ('Verdana', 15)
    first_name = Entry(win8, width=30, borderwidth=2, font=large_font)
    phone = Entry(win8, width=30, borderwidth=2, font=large_font)

    rooms_list = np.arange(100, 151, 1)
    rooms_list = list(rooms_list)
    room_number_clicked = IntVar()
    room_number_clicked.set(100)
    room_number = OptionMenu(win8, room_number_clicked, *rooms_list)
    room_number.config(bg="white", borderwidth=0, font=large_font)


    first_name.place(x=900, y=410)
    phone.place(x=900, y=510)
    room_number.place(x=900, y=610)

    def find_delete():
        global win9
        win9 = Toplevel()
        win9.configure(background='white')
        win9.geometry("1920x1080")
        # win9.attributes('-fullscreen', True)
        win9.title("Delete Booking")

        background = Label(win9, image=delete_find_photo_image)
        background.place(relx=.5, rely=.5, anchor="center")
        background.lower()

        global fdlabel1, fdlabel2, fdlabel3, fdlabel4, fdlabel5, fdlabel6, fdlabel7, fdlabel8, \
            fdlabel9, fdlabel10, fdlabel11, fdlabel12, fdlabel13, fdlabel14, fdlabel15

        f_name = first_name.get()
        pno = phone.get()
        drno = room_number_clicked.get()
        print(drno)

        sql = '''
                SELECT * FROM DATA
                WHERE first_name = %s and phone_number = %s and room_number = %s
                '''
        val = (str(f_name), str(pno), int(drno))
        cur.execute(sql, val)

        results = cur.fetchone()
        find_list = []

        for x in results:
            print(x)
            find_list.append(x)

        first_name.delete(0, END)
        phone.delete(0, END)

        fdlabel1 = Label(win9, text="Delete Customer Details", bg="white", anchor=CENTER)
        fdlabel1["font"] = font11

        fdlabel2 = Label(win9, text="First Name: {}".format(find_list[0]), bg="white")
        fdlabel3 = Label(win9, text="Last Name: {}".format(find_list[1]), bg="white")
        fdlabel4 = Label(win9, text="Phone Number: {}".format(find_list[2]), bg="white")
        fdlabel5 = Label(win9, text="Email: {}".format(find_list[3]), bg="white")
        fdlabel6 = Label(win9, text="Address: \n{}".format(find_list[4]), bg="white", justify=LEFT, wraplength=500)
        fdlabel7 = Label(win9, text="City: {}".format(find_list[5]), bg="white")
        fdlabel8 = Label(win9, text="Zipcode: {}".format(find_list[6]), bg="white")
        fdlabel9 = Label(win9, text="Room Number: {}".format(find_list[7]), bg="white")
        fdlabel10 = Label(win9, text="Check In: {}".format(find_list[8]), bg="white")
        fdlabel11 = Label(win9, text="Verification: {}".format(find_list[9]), bg="white")
        fdlabel12 = Label(win9, text="No. of Days: {}".format(find_list[10]), bg="white")
        fdlabel13 = Label(win9, text="No. of Adults: {}".format(find_list[11]), bg="white")
        fdlabel14 = Label(win9, text="No. of Children: {}".format(find_list[12]), bg="white")
        fdlabel15 = Label(win9, text="Room Type: {}".format(find_list[13]), bg="white")

        fdlabel1.place(x=700, y=70)
        fdlabel2.place(x=600, y=200)
        fdlabel3.place(x=600, y=300)
        fdlabel4.place(x=600, y=400)
        fdlabel5.place(x=600, y=500)
        fdlabel6.place(x=600, y=600)
        fdlabel7.place(x=600, y=700)
        fdlabel8.place(x=600, y=800)
        fdlabel9.place(x=1100, y=200)
        fdlabel10.place(x=1100, y=300)
        fdlabel11.place(x=1100, y=400)
        fdlabel12.place(x=1100, y=500)
        fdlabel13.place(x=1100, y=600)
        fdlabel14.place(x=1100, y=700)
        fdlabel15.place(x=1100, y=800)

        fdlabel2["font"] = font9
        fdlabel3["font"] = font9
        fdlabel4["font"] = font9
        fdlabel5["font"] = font9
        fdlabel6["font"] = font9
        fdlabel7["font"] = font9
        fdlabel8["font"] = font9
        fdlabel9["font"] = font9
        fdlabel10["font"] = font9
        fdlabel11["font"] = font9
        fdlabel12["font"] = font9
        fdlabel13["font"] = font9
        fdlabel14["font"] = font9
        fdlabel15["font"] = font9

        def delete_entry():
            cur.execute("SET SQL_SAFE_UPDATES = 0;")

            query1 = '''
            DELETE FROM DATA
            WHERE first_name = %s and phone_number = %s;
            '''
            val1 = (str(f_name), str(pno))
            cur.execute(query1, val1)


            query2 = '''
            DELETE FROM PAYMENT
            WHERE first_name = %s and phone_number = %s;
            '''
            val2 = (str(f_name), str(pno))
            cur.execute(query2, val2)

            query3 = '''
            DELETE FROM CUSTOMER
            WHERE first_name = %s and phone_number = %s;
            '''
            val3 = (str(f_name), str(pno))
            cur.execute(query3, val3)

            cur.execute('''
            DELETE FROM BOOKING
            WHERE room_number = {}'''.format(drno))


            conn.commit()

        global button_delete
        button_delete = Button(win9, text="Delete", bg="white", padx=15, pady=0,
                               command=lambda: [delete_entry(), destroy_find_delete()])
        button_delete['font'] = font4
        button_delete.place(x=800, y=900)

        global button_delete_exit
        button_delete_exit = Button(win9, text="Exit", bg="white", padx=15, pady=0,
                                    command=lambda: [destroy_find_delete()])
        button_delete_exit['font'] = font4
        button_delete_exit.place(x=980, y=900)

    global delete_find
    delete_find = Button(win8, text="Find", bg="white", padx=15, pady=0, command=lambda: [find_delete()])
    delete_find['font'] = font4
    delete_find.place(x=800, y=900)

    global delete_exit
    delete_exit = Button(win8, text="Exit", bg="white", padx=15, pady=0,
                         command=lambda: [destroy_delete()])
    delete_exit['font'] = font4
    delete_exit.place(x=980, y=900)


def destroy_delete():
    win8.destroy()


def destroy_find_delete():
    win9.destroy()


def view_payment():
    global win11
    win11 = Toplevel()
    win11.configure(background='white')
    win11.geometry("1920x1080")
    # win11.attributes('-fullscreen', True)
    win11.title("Payments")

    background = Label(win11, image=vpay_photo_image)
    background.place(relx=.5, rely=.5, anchor="center")
    background.lower()

    sql = '''
    SELECT PAYMENT.first_name, PAYMENT.last_name,CUSTOMER.email ,
    PAYMENT.phone_number, PAYMENT.mode_of_payment,PAYMENT.pid,PAYMENT.amount
    FROM PAYMENT
    INNER JOIN CUSTOMER 
    ON PAYMENT.phone_number=CUSTOMER.phone_number;
    '''
    cur.execute(sql)

    results = cur.fetchall()

    count = len(results)

    vplabel1 = Label(win11, text="Payment Details", bg="white", anchor = CENTER)
    vplabel1["font"] = font11
    vplabel1.place(x = 800,y=80)

    pos = 1
    for x in range(count):
        pos = pos + 1
        print(str(results[x])[1:-1])
        x = Label(win11, text="{}.  {}\n".format(x+1, (", ".join(results[x]))), bg="white", anchor = CENTER)
        x.place(x=550, y=(pos * 50 + 100))
        x["font"] = font9

    global find_exit
    find_exit = Button(win11, text="Exit", bg="white", padx=15, pady=0, command=destroy_view_payment)
    find_exit['font'] = font4
    find_exit.place(x=900, y=900)


def destroy_view_payment():
    win11.destroy()


button_next = Button(root, text="Next", bg="white", padx=20, command=home)
button_next['font'] = font4
button_next.pack(pady=3)

root.mainloop()