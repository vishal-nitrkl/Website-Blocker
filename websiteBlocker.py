# copywright : @vishalJaiswal

# import libraries -------------->>>>
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import datetime as dt
from tkinter import messagebox as msg
# global variable ---------------->>>>>
host_path="C:/Windows/System32/drivers/etc/hosts"
ip="127.0.0.1   "
today_date=dt.date.today()

social_media=['www.Snapchat.com', 'www.facebook.com', 'www.twitter.com', 'www.whatsapp.com', 'www.instagram.com']
Shopping_websites=['www.amazon.com', "www.eBay.com", "www.eBuyer.com" ,"www.Walmart.com", 'www.Target.com']
dating_websites=['www.Match.com','www.MeetMe.com' ,'www.OKCupid.com', 'www.Tinder.com', "www.Bumble.com" ]
Explicit_websites=['www.Pornhub.com', 'www.Kink.com', 'www.YouJizz.com' , 'www.8Tube.xxx' , 'Redtube.com'  ]
Chat_websites=['www.Omegle.com', 'TalkWithStranger.com', 'www.ChatRoulette.com', 'Chat-Avenue.com','PalTalk.com']
Poker_and_casino_websites=['BetOnline.ag', 'FreeSpin.com' , 'Bovada.lv' , 'SlotoCash.im'  ,  'RoyalAceCasino.com' ]

# *************************************************************************************************************


class Example1():
    def __init__(self, win):
        self.top = tk.Toplevel(win)

        self.cal = Calendar(self.top, font="Arial 14", selectmode='day', year=2020, month=6, day=20)
        self.cal.pack(fill="both", expand=True)
        ttk.Button(self.top, text="ok", command=self.print_sel).pack(pady=10)
        # ttk.Button(self.top, text="exit", command=self.quit1).pack()

        self.date = ''

        self.top.grab_set()

    def print_sel(self):
        self.date = self.cal.selection_get()
        self.top.destroy()



class App():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Website Blocker')
        s = ttk.Style(self.win)
        s.theme_use('clam')

        # lable---------------->>>>>>>>
        l1=tk.Label(self.win, text="My Sessions", font=("Arial Bold", 15), bg = 'purple', fg = 'white')
        lbl_heading=tk.Label(self.win, text="Schedule Your Session  :", font=("Arial Bold", 15))
        b1=tk.Label(self.win, text="My Blocklists", font=("Arial Bold", 15), bg = 'purple', fg = 'white')
        
        # self.lbl_var=tk.StringVar()
        # self.l=ttk.Label(self.win, text="__", textvariable=self.lbl)
        # self.l.grid(row=2, column=1)
        self.s=tk.Label(self.win, text="________", font=("Arial Bold", 13),  bg = 'purple' ,fg = 'white')
        self.s.grid(row=2, column=1)

        self.e=tk.Label(self.win, text="________", font=("Arial Bold", 13), bg = 'purple', fg = 'white')
        self.e.grid(row=3, column=1)

        b3=tk.Label(self.win, text=" -- Add these Sites In Your Blocklist --", font=("Arial Bold", 15))
        

        # entry box------------>>>>>>>>>
        self.site_var=tk.StringVar()
        self.site_entrybox=ttk.Entry(self.win, width=55, textvariable=self.site_var)
        

        # button-------------->>>>>>>
        ttk.Button(self.win, text='start Date', command=self.start).grid(row=2, column=0)
        ttk.Button(self.win, text='end Date', command=self.end).grid(row=3,column=0,padx=10, pady=10)
        save_btn=tk.Button(self.win, text="Save",  width=10, font=("Arial Bold", 12), bg='green', fg='white', command=self.store_var)
        Addsite_btn=tk.Button(self.win, text="Add Sites", width=10, font=("Arial Bold", 12), bg='green', fg='white', command=self.action_addSite)
        finalSave_btn=tk.Button(self.win, text="Save", width=10, font=("Arial Bold", 12), bg='green', fg='white', command=self.action_save)

        # grid positioning ---------->>>>>>>>.
        l1.grid(row=0, column=0)
        lbl_heading.grid(row=1, column=0, columnspan=2,  pady=20)
        save_btn.grid(row=4,column=0, columnspan=2, pady=30)
        b1.grid(row=5, column=0, pady=30, padx=10)
        self.site_entrybox.grid(row=6, columnspan=2, pady=5)
        Addsite_btn.grid(row=6, column=3 , pady=5)
        b3.grid(row=7,column=0, columnspan=2, padx=5, pady=10)
        finalSave_btn.grid(row=11, columnspan=2, padx=10, pady=30)

        # variable storing checkbox value : {0 or 1}--------->>>>>>
        self.CheckVar_social = tk.IntVar()
        self.CheckVar_shopping = tk.IntVar()
        self.CheckVar_new = tk.IntVar()
        self.CheckVar_game = tk.IntVar()
        self.CheckVar_timeWaster = tk.IntVar()
        self.CheckVar_adult = tk.IntVar()
        
        # checkbox widget and griding ----------------->>>>>
        self.C1 = tk.Checkbutton(self.win, text = "Social", font=("Arial Bold ", 12), variable = self.CheckVar_social, onvalue = 1, offvalue = 0, height=3, width = 7)
        self.C1.grid(row=8, column=0,sticky=tk.W, padx=30)

        self.C2 = tk.Checkbutton(self.win, text = "Shopping",font=("Arial Bold ", 12), variable = self.CheckVar_shopping, onvalue = 1, offvalue = 0, height=3, width = 7)
        self.C2.grid(row=9, column=0,sticky=tk.W, padx=40)

        self.C3 = tk.Checkbutton(self.win, text = "News", font=("Arial Bold ", 12), variable = self.CheckVar_new, onvalue = 1, offvalue = 0, height=3, width = 7)
        self.C3.grid(row=10, column=0,sticky=tk.W, padx=25)

        self.C4 = tk.Checkbutton(self.win, text = "Games", font=("Arial Bold ", 12), variable = self.CheckVar_game, onvalue = 1, offvalue = 0, height=3, width = 7)
        self.C4.grid(row=8, column=1,sticky=tk.W, padx=50)

        self.C5 = tk.Checkbutton(self.win, text = "Time Waster", font=("Arial Bold ", 12), variable = self.CheckVar_timeWaster, onvalue = 1, offvalue = 0, height=3, width = 15)
        self.C5.grid(row=9, column=1,sticky=tk.W, padx=30)

        self.C6 = tk.Checkbutton(self.win, text = "Adult", font=("Arial Bold ", 12), variable = self.CheckVar_adult, onvalue = 1, offvalue = 0, height=3, width = 7)
        self.C6.grid(row=10, column=1,sticky=tk.W, padx=40)

        # local variables-------->>>>> 
        self.start_date = ''
        self.end_date = ''
        self.websiteList1=[]

        self.win.mainloop()

# ****************************************************************************************************************

# Methods of the App class----->>>>>> 

   # main function : write sites from website_list (user defined) into host file------->>>>>    
    def blocker(self,website_list):
        while True:
            if self.start_date <=today_date <self.end_date:
                with open(host_path,'r+') as file:
                    content=file.read()
                    for i in website_list:
                        if i in content:
                            pass
                            # print(f'{i} : Blocked')
                        else:
                            file.write(f'{ip } {i}\n')
                # print('all sites are blocked')
                break
        
            else: #end_date<today_date or len(website_list)==0: 
                with open(host_path, 'r+') as file:
                    content=file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(i in line  for i in website_list):
                            file.write(line) 
                    file.truncate()
                # print('All site unblocked')
                break
    
    # clear sites from the host file : if  start_date >current_date || current_date  >=end_date ------->>>>>>
    def clean(self,website_list):
        with open(host_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(i in line  for i in website_list):
                    file.write(line) 
            file.truncate()
        # print('All site unblocked')
        # msg.showinfo('Website Blocker', 'Unblocked Successfully')

    # Start date will be selected on button click---------->>>>>>>>>
    def start(self):
        cal = Example1(self.win)
        self.win.wait_window(cal.top)
        self.start_date = cal.date

    # End date will be selected on button click------------>>>>>>>>>
    def end(self):
        cal = Example1(self.win)
        self.win.wait_window(cal.top)
        self.end_date = cal.date
    
    # Start and End Date is stored into sdate and edate variable respectively----------->>>>>>
    def store_var(self):
        sdate=self.start_date
        edate=self.end_date
        self.s.config(text=sdate)
        self.e.config(text=edate)

        # print(sdate)
        # print(edate)
        if sdate=="" or edate=="":
            msg.showwarning('Website Blocker','Please select the Start and End Date')

    # Site taken in an entry box (by the user) will be blocked---------->>>>>>   
    def action_addSite(self):
        try :
            site=self.site_var.get()
            self.websiteList1.append(site)
            # print(self.websiteList1)
            self.site_entrybox.delete(0,tk.END)
            self.blocker(self.websiteList1)



        except TypeError:
            msg.showerror('Website Blocker', 'Please select the Start and End Date' )
        
        if self.start_date <=today_date <self.end_date:
            
            msg.showinfo('Website Blocker', "Blocked Successfully")
        else:
            msg.showinfo('Website Blocker', "UnBlocked Successfully")

    # Save the input provided by the user and block the sites if provided date satidfy the contion----------->>>>>>
    def action_save(self):
        
        if self.CheckVar_social.get()==1:
            self.blocker(social_media)
        else:
            self.clean(social_media)
    
        if self.CheckVar_shopping.get()==1:
            self.blocker(Shopping_websites)
        else:
            self.clean(Shopping_websites)

        if self.CheckVar_adult.get()==1:
            self.blocker(Explicit_websites)
        else:
            self.clean(Explicit_websites)

        if self.CheckVar_timeWaster.get()==1:
            self.blocker(dating_websites)
            self.blocker(Chat_websites)
        else:
            self.clean(dating_websites)
            self.clean(Chat_websites)
        
        if self.CheckVar_game.get()==1:
            self.blocker(Poker_and_casino_websites)
        else:
            self.clean(Poker_and_casino_websites)
        

        # self.CheckVar_social = 0
        # self.CheckVar_shopping = 0
        # self.CheckVar_new = 0
        # self.CheckVar_game = 0
        # self.CheckVar_timeWaster = 0
        # self.CheckVar_adult = 0

        if self.start_date <=today_date <self.end_date:
            msg.showinfo('Website Blocker', "Websites ; Blocked Successfully")
        else:
            msg.showinfo('Website Blocker', "Websites ; UnBlocked Successfully")

# ******************************************************************************************************************

app = App()
# Start_date=app.start_date
# End_date=app.end_date
# print(Start_date)





