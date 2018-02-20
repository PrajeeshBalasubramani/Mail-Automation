from __future__ import print_function
import smtplib
from tkinter import *
import numpy as np
from tkinter import ttk 
import tkinter 
import tkinter as tk
import pandas as pd
import time
import datetime
import urllib
import urllib.request as ur
import sys
import os
import logging
import logging.config
import threading
import  tkinter.messagebox
import random
try:
    import Tkinter as tk
    import Queue as qu
except ImportError:
    import tkinter as tk
    import queue as qu
now = datetime.datetime.now()
l=now.strftime("%Y ")
l=l+now.strftime("%m ")
l=l+now.strftime("%d ")
  
logging.basicConfig(filename='{0}_logfile.log'.format(l),level=logging.DEBUG)

from email.mime.text import MIMEText
APP_TITLE = "Mail Automation"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 800
APP_HEIGHT = 300
UPDATE_TIME = 1000 # Milliseconds

QUEUE_SIZE = 500
POLLING_TIME = 1000
p=[] 
a=[]
b=[]
p1=[] 
a1=[]
b1=[]
prop=[]
class mainwindow(object):
    ls=[] 
    lt=[]
    xs=[] 
    ys=[] 
    lg=[] 
    lh=[] 
    vs=[]
    ar=0
    imr=0
    br=0
    cr=0 
    def  __init__(self):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
    
        self.g=open('EnterSampleEmails.txt','r')
        self.gr=self.g.read()
        mainwindow.lg = self.gr.split(",")
        time.sleep(3)
        self.h=open("EnterSampleNames.txt",'r')
        self.th=self.h.read()
        mainwindow.lh=self.th.split(",")
        time.sleep(3)
        self.v=open('EnterIDs.txt','r')#inquotes
        self.vr=self.v.read()
        mainwindow.vs =self.vr.split(",")
        self.x=open('prajeesh.txt','r')#inquotes
        self.xr=self.x.read()
        mainwindow.xs = self.xr.split(",")
        self.y=open('prajeeshpass.txt','r')#inquotes
        self.yr=self.y.read()
        mainwindow.ys =self.yr.split(",")
        self.s= open('clgmail.txt','r')
        self.sr=self.s.read()
        mainwindow.ls = self.sr.split(",")
        time.sleep(3)
        self.t=open("EnterRecevierNames.txt",'r')
        self.tr=self.t.read()
        mainwindow.lt=self.tr.split(",")
        time.sleep(3)
        self.c= open('Entersubject.txt','r')
        mainwindow.cr=self.c.read()#inquotes
        self.a = open('EntertheHTMLPart-I.txt','r')
        mainwindow.ar=self.a.read()
        self.im= open('EnterImagePart.txt','r')
        mainwindow.imr=self.im.read()
        self.b= open('EntertheHTMLPart-II.txt','r')
        mainwindow.br=self.b.read()
        secondmain()
        
    def internetcheck(self):
        try:
            ur.urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=aNA8WtaQBayIX7Dop5gGm', timeout=1) #to check internet
            return True
        except ur.URLError as err:
            return False
    def first(self,parent):
        self.parent=parent
        parent.title=("Mail Automation Application" )
        
        self.welcome=Label(parent,text="Welcome to Mail Automation Application")
        self.welcome.grid(sticky=E)
        self.Sample= Button(parent, text='Scheduled')
        self.Sample.grid(row=8)
        self.Actual= Button(parent, text='Regular',command=secondmain) 
        self.Actual.grid(row=6, column=0,sticky=N)
 
class secondwindow(mainwindow):
    def __init__(self,master):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        global ment
        self.g=open('quotesone.txt','r',encoding="utf8")
        self.gr=self.g.read()
        prop = self.gr.split("||")
        quote=random.choice(prop)
        self.master = master
        self.intruction = Label(self.master, text='VEDIC FOLKS',font='Italic 25 bold',fg="green")
        
        self.intruction.grid(row=0, column=1, sticky=W)
        #self.image = tk.PhotoImage(file="image.jpg")
        self.image = tk.PhotoImage(file="image.gif")
        self.label = tk.Label(image=self.image)
        self.label.grid(row=0,column=0)
        self.title = Label(self.master, text='Mail Automation',font='Italic 15 bold',fg="black")
        
        self.title.grid(row=1, column=2, sticky=W)
        self.name = Label(self.master, text='Select:',font='Helvetica 13 bold')
        self.name.grid(row=3,column=1,sticky=E)
        self.Sample= Button(self.master, text='Sample',command=self.sample,bg="blue",fg="white",)
        self.Sample.grid(row=5,column=2,sticky=W)
        self.name1 = Label(self.master, text=' ',font='Helvetica 13 bold')
        self.name1.grid(row=4,column=2)
        self.Actual= Button(self.master, text='Regular',command=self.receviernumber,bg="blue",fg="white",) 
        self.Actual.grid(row=3, column=2,sticky=W)
        self.name1 = Label(self.master, text=' ',font='Helvetica 13 bold')
        self.name1.grid(row=6,column=2)
        #self.bottom_frm = tk.Frame(self.master)
        self.btn_frm_r = tk.Frame(self.master, background='yellow', width=600, height=50)
        self.btn_frm_r.grid(column=0, row=8 , columnspan= 10)
        self.name1 = Label(self.btn_frm_r, text=quote,font='Helvetica 13 bold')
        self.name1.grid()
        #elf.bottom_frm.grid(side="bottom",fill="x",expand=False)

    def error(self):
        roots=Tk()
        self.k = 300 
        self.s = 100
        self.wk = roots.winfo_screenwidth() 
        self.hw = roots.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2) 
        self.text=Entry(self.master)
        self.text.grid(row=3)
        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        roots.mainloop() 
    def sample(self):
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        logging.debug('Selected Sample Option')
        for i in range(0, len(self.lg)):
            logging.debug('enterd interation No:%d'%i)
            title = self.lh[i]
            msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
                title=title)
            msg_01content = self.ar
            msg_02content = self.imr
            msg_03content = self.br
            msg = msg_00content + msg_01content + msg_02content + msg_03content
            message = MIMEText(msg, 'html')
            message['From'] =self.vs[i]
            message['To'] = self.ls[0]
            message['Subject'] = self.cr
            msg_full = message.as_string()
            if i <= 10:
                try:
                    if self.internetcheck() == False:
                        tkinter.messagebox.showwarning('Warning','Network Failure,waiting for connections')
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0,1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    break
                            else:
                            
                                tkinter.messagebox.showinfo('Information','Awake from sleep, Got connection...')
                                
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                break      
                        
                    else:
                        
                        server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                        server.starttls()  # asking server to start
                        server.login(self.xs[0], self.ys[0])  # Sender Mail, Sender Mail Password
                        server.sendmail(self.xs[0], [self.lg[i]], msg_full)
                        
                        p.append(self.xs[0])
                        a.append(self.lg[i])
                        b.append(self.cr)
                        
                        logging.debug('Sending to : %s'%self.lh[i])
                        
                           
                except smtplib.SMTPException:
                    if self.internetcheck() == False:
                        tkinter.messagebox.showinfo('Information','Network Failure,waiting for connections')
                        
                        
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0, 1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                tkinter.messagebox.showinfo('Information','Sleeping until internet connects...Trying %d times' % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    break
                            else:
                                
                                
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                
                    else:
                        roots=Tk()
                        self.k = 300 
                        self.s = 100
                        self.wk = roots.winfo_screenwidth() 
                        self.hw = roots.winfo_screenheight()
                        self.z = (self.wk/2) - (self.k/2)
                        self.u = (self.hw/2) - (self.s/2) 
                        self.text=Text(roots)
                        self.text.grid(row=3)
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        file = open("Errorlog.txt", "w")
                        file.write("Date Time:{}".format(str(now)))
                        file.write("Error: MailerID {} /n".format(self.xs[0]))
                        file.write("Error: MailerID {} /n".format(i))
                        file.close()
                        self.d1="Date Time:{}".format(str(now))
                        tkinter.messagebox.showinfo('Information',"Date Time:{}".format(str(now)))
                        tkinter.messagebox.showinfo('Information',"Error: MailID {}".format(self.xs[0]))
                        tkinter.messagebox.showinfo('Information',"Error: Sent upto {}".format(i))
                        self.text.insert(END,"Date Time:{} \n".format(str(now)))
                        self.text.insert(END,"Error: MailID {} \n".format(xs[0]))
                        self.text.insert(END,"Error: Sent upto {} \n".format(i))
                        logging.error("Unexpected Error Occured")
                        logging.error(str(now))
                        logging.error("Sent upto:%d"%i)
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        roots.mainloop()
                        break
            else:
                logging.debug('Contact Developer...Needs Renovation.')
                print("Contact Developer...Needs Renovation.")
        main()
    def receviernumber(self):
        global numberentry
        global codeentry
        global lg
        global lh
        global ar
        global im
        global imr
        global b
        global br
        global vs
        global ls
        global cr
        global xs
        roots=Tk()
        self.k = 300 
        self.s = 100
        self.wk = roots.winfo_screenwidth() 
        self.hw = roots.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        roots.title("Mail Automation") 
        self.receviernumber = Label(roots, text='Recevier Number:')
        self.receviernumber.grid(row=2)
        self.code = Label(roots, text='Specific Code')
        self.code.grid(row=3)
        self.numberentry= tk.Entry(roots)
        self.numberentry.grid(row=2, column=1)
        self.codeentry= tk.Entry(roots)
        self.codeentry.grid(row=3, column=1)
        self.B1=Button(roots, text=" Start  ",bg="blue",fg="white",command=self.actual
            ).grid(row=5,column=1)
        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        roots.mainloop()

    def actual(self):
        global numberentry
        global codeentry
        global ment
        #ment=StringVar()
        logging.debug('Selected Actual Customers Option')
        j=0
        k=1
        df=self.codeentry.get()
        self.uo=self.numberentry.get()
        self.uo=int(self.uo)
        print(self.uo)
        for i in range(self.uo, len(mainwindow.ls)):
            logging.debug('enterd interation No:%d'%i)
            title = self.lt[i]
            msg_00content = '<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(
                title=title)
            msg_01content = self.ar
            msg_02content = self.imr
            msg_03content = self.br
            msg = msg_00content + msg_01content + msg_02content + msg_03content
            message = MIMEText(msg, 'html')
            message['From'] =self.vs[j]
            message['To'] = self.ls[0]
            bk=',Feedback-ID:{df}:{fd}:01:01'.format(df=df,fd=i)
            message['Subject'] = self.cr+bk
            msg_full = message.as_string()
            if i <= 500:
                try:
                    if self.internetcheck() == False:
                        
                        
                        tkinter.messagebox.showwarning('Warning',"Network Failue,waiting for connections")

                        
                    
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                    
                        for u in range(0,1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    break
                            else:
                                tkinter.messagebox.showwarning('Warning',"Awake from sleep, Got connection...")
                                #print("Awake from sleep, Got connection...", end='\r')
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                        
                                
                    else:
                        server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                        server.starttls()  # asking server to start
                        server.login(self.xs[0], self.ys[0])  # Sender Mail, Sender Mail Password
                        server.sendmail(self.xs[0], [self.ls[0]], msg_full)
                        p1.append(self.xs[0])
                        a1.append(self.ls[0])
                        b1.append(self.cr)
                        #print(" \n Sent to ", i, self.lt[i])
                        server.quit()  # asking server to quit
                        time.sleep(10)
                        logging.debug('Sending to : %s'%self.lt[i])
                        if k!=0:
                            if j<30:
                                j=1
                            elif j>30 and j<60:
                                j=2
                            elif j>60 and j<90:
                                j=3
                            elif j>90 and j<120:
                                j=4
                            elif j>120 and j<150:
                                j=5
                            elif j>150 and j<180:
                                j=6
                            elif j>180 and j<210:
                                j=7
                            elif j>210 and j<240:
                                j=8
                            elif j>240 and j<270:
                                j=9
                            elif j>300 and j<330:
                                j=10
                            elif j>330 and j<360:
                                j=11
                            elif j>360 and j<390:
                                j=12
                            elif j>390 and j<420:
                                j=13
                            elif j>420 and j<450:
                                j=14
                            elif j>450 and j<480:
                                j=15
                            elif j>480 and j<510:
                                j=16
                            elif j>510 and j<540:
                                j=17
                            elif j>540 and j<580:
                                j=18
                except smtplib.SMTPException:
                    if self.internetcheck() == False:
                        ment="Network Failue,waiting for connections"
                        self.text.insert(END,ment)
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0, 1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    break
                            else:
                                tkinter.messagebox.showwarning('Warning',"Awake from sleep, Got connection...")
                                sys.stdout.flush()
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                break
                    else:
                        roots=Tk()
                        self.k = 300 
                        self.s = 100
                        self.wk = roots.winfo_screenwidth() 
                        self.hw = roots.winfo_screenheight()
                        self.z = (self.wk/2) - (self.k/2)
                        self.u = (self.hw/2) - (self.s/2) 
                        self.text=Text(roots)
                        self.text.grid(row=3)
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        file = open("Errorlog.txt", "w")
                        file.write("Date Time:{}".format(str(now)))
                        file.write("Error: MailerID {} /n".format(self.xs[j]))
                        file.write("Error: MailerID {} /n".format(i))
                        file.close()
                        self.text.insert(END,"Date Time:{} \n".format(str(now)))
                        self.text.insert(END,"Error: MailID {} \n".format(self.xs[0]))
                        self.text.insert(END,"Error: Sent upto {} \n".format(i))
                        self.text.insert(END,"Error section j=",j)
                        logging.error("Unexpected Error Occured")
                        logging.error(str(now))
                        logging.error("Sent upto: %d"%i)
                        logging.error("Sent with: %d"%j)
                        j=j+1
                        k=0
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        roots.mainloop()
                        continue 
            elif i>=500:
                logging.debug('Contact Developer...Needs Renovation.')
                print("Contact Developer.... Needs Renovation.")
        main1()

#-------------sample--------------------------------------------------------------------#                
class appThread(threading.Thread):
    def __init__(self, queue1=None,queue2=None,queue3=None):
        
        self.queue1 = queue1
        self.queue2 = queue2
        self.queue3 = queue3
        threading.Thread.__init__(self,target=self.run1)
        
        threading.Thread.__init__(self,target=self.run)
        self.start()
    def run(self):
        msg=b[0]
        self.update_queue3(msg)
        self.run1()   
    def run1(self):
        
        #for i in range(0,len(p)):
        num_count=p[0]
        self.update_queue1(num_count)
            
        self.run2()    #print("4",v)
        
    def run2(self):
        for i in range(0,len(a)):
            num=a[i]
            self.update_queue2(num)

    def update_queue1(self,num_count):
        self.queue1.put(num_count)
        self.queue1.join()
    def update_queue2(self,num):
        self.queue2.put(num)
        self.queue2.join()
    def update_queue3(self,msg):
        self.queue3.put(msg)
        self.queue3.join()
class application(tk.Frame):
    
    def __init__(self, master):
        

        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Frame.__init__(self, master)
         
        
        self.app_thread = None
         
        self.frame_head = tk.Frame(self, width=600, height=50)
        self.frame_head.grid(column=0, row=0 , columnspan= 10)
        self.title = Label(self.frame_head, text='Mail Automation',font='Italic 15 bold',fg="black")
        self.title.grid(row=0, column=0, sticky=W)
        self.frame_body = tk.Frame(self, width=600, height=500)
        self.frame_body.grid(column=0, row=1 , columnspan= 10)
        tk.Label(self.frame_body, text=b[0],font='Italic 13 bold',fg="green").grid(column=0, row=2, stick='W') 
        #self.name1 = Label(self.control_frame, text=b1[0],font='Helvetica 13 bold')
        #self.name1.grid()  
        #self.subject = Label(self.control_frame, text='Sending Subject:')
        self.frame_body2 = tk.Frame(self, width=600, height=500)
        self.frame_body2.grid(column=0, row=5 , columnspan= 10)
        self.sender = Label(self.frame_body2, text='From:')
        self.recevier = Label(self.frame_body2, text='To:')
        self.sender.grid(row=2, sticky=W)
        self.recevier.grid(row=3, sticky=W)
        #self.subjectentry= Entry(self.control_frame )
        self.senderentry= Entry(self.frame_body2)
        self.recevierentry= Entry(self.frame_body2)
        #self.subjectentry.grid(row=1, column=1)
        self.senderentry.grid(row=2, column=1)
        self.recevierentry.grid(row=3, column=1)
        
        
        self.B1=Button(self.frame_body2, text=" Start  ",bg="purple",fg="white",
            command=self.start_thread).grid(row=5,column=1)
        
        self.queue1 = qu.Queue(QUEUE_SIZE)
        self.queue2 = qu.Queue(QUEUE_SIZE)
        self.queue3 = qu.Queue(QUEUE_SIZE)  
        self.queue_polling()
         
    def start_thread(self):
        
        if self.app_thread == None:
            self.app_thread = appThread(
                self.queue1,self.queue2,self.queue3)
        else:
            if not self.app_thread.isAlive():
                self.app_thread = appThread(
                self.queue1,self.queue2,self.queue3)
       

    def queue_polling(self):
        if self.queue3.qsize() :
            try:
                
                data3 = self.queue3.get()
            
                #self.subjectentry.delete(0,'end')
                #self.subjectentry.insert(0,data3)

                self.queue3.task_done()
                
                
            except qu.Empty:
                pass
                print("hai")
        if self.queue1.qsize() :
            try:
                
                data1 = self.queue1.get()
               
                #print("37",self.max_number)
                
                
                self.senderentry.delete(0,'end')
                self.senderentry.insert(0,data1)

                self.queue1.task_done()
                
                
            except qu.Empty:
                pass
                print("hai")
        if self.queue2.qsize():
            try:
                
                
                data2 = self.queue2.get()
                
                self.recevierentry.delete(0,'end')
                self.recevierentry.insert(0,data2)                
                self.queue2.task_done()
                
            except qu.Empty:
                pass
                print("hai")        
        self.after(POLLING_TIME, self.queue_polling)
                 
    def close(self):
        print("Application-Shutdown")
        self.app_thread.join()
        self.master.destroy()
#--------------------error---------------------------------------------------------------------------#
#------------------------------------------actual----------------------------------------------------#    
class AppThread(threading.Thread):
    def __init__(self, queue1=None,queue2=None,queue3=None):
        
        self.queue1 = queue1
        self.queue2 = queue2
        self.queue3 = queue3
        threading.Thread.__init__(self,target=self.run1)
        
        threading.Thread.__init__(self,target=self.run)
        self.start()
    def run(self):
        msg=b1[0]
        self.update_queue3(msg)
        self.run1()   
    def run1(self):
        
        #for i in range(0,len(p)):
        num_count=p1[0]
        self.update_queue1(num_count)
            
        self.run2()    #print("4",v)
        
    def run2(self):
        for i in range(0,len(a1)):
            num=a1[0]
            self.update_queue2(num)
  
    def update_queue1(self,num_count):
        self.queue1.put(num_count)
        self.queue1.join()
    def update_queue2(self,num):
        self.queue2.put(num)
        self.queue2.join()
    def update_queue3(self,msg):
        self.queue3.put(msg)
        self.queue3.join()
class Application(tk.Frame):
    
    def __init__(self, master):
        

        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Frame.__init__(self, master)
         
        
        self.app_thread = None
        self.frame_head = tk.Frame(self, width=600, height=50)
        self.frame_head.grid(column=0, row=0 , columnspan= 10)
        self.title = Label(self.frame_head, text='Mail Automation',font='Italic 15 bold',fg="black")
        self.title.grid(row=0, column=0, sticky=W)
        self.frame_body = tk.Frame(self, width=600, height=500)
        self.frame_body.grid(column=0, row=1 , columnspan= 10)
        tk.Label(self.frame_body, text=b1[0],font='Italic 13 bold',fg="green").grid(column=0, row=2, stick='W') 
        #self.name1 = Label(self.control_frame, text=b1[0],font='Helvetica 13 bold')
        #self.name1.grid()  
        #self.subject = Label(self.control_frame, text='Sending Subject:')
        self.frame_body2 = tk.Frame(self, width=600, height=500)
        self.frame_body2.grid(column=0, row=5 , columnspan= 10)
        self.sender = Label(self.frame_body2, text='From:')
        self.recevier = Label(self.frame_body2, text='To:')
        self.sender.grid(row=2, sticky=W)
        self.recevier.grid(row=3, sticky=W)
        #self.subjectentry= Entry(self.control_frame )
        self.senderentry= Entry(self.frame_body2)
        self.recevierentry= Entry(self.frame_body2)
        #self.subjectentry.grid(row=1, column=1)
        self.senderentry.grid(row=2, column=1)
        self.recevierentry.grid(row=3, column=1)
        
        
        self.B1=Button(self.frame_body2, text=" Start  ",bg="purple",fg="white",
            command=self.start_thread).grid(row=5,column=1)
        
        self.queue1 = qu.Queue(QUEUE_SIZE)
        self.queue2 = qu.Queue(QUEUE_SIZE)
        self.queue3 = qu.Queue(QUEUE_SIZE)  
        self.queue_polling()
         
    def start_thread(self):
        
        if self.app_thread == None:
            self.app_thread = AppThread(
                self.queue1,self.queue2,self.queue3)
        else:
            if not self.app_thread.isAlive():
                self.app_thread = AppThread(
                self.queue1,self.queue2,self.queue3)
       

    def queue_polling(self):
        if self.queue3.qsize() :
            try:
                
                data3 = self.queue3.get()
               
                #self.subjectentry.delete(0,'end')
                #self.subjectentry.insert(0,data3)

                self.queue3.task_done()
                
                
            except qu.Empty:
                pass
                print("hai")
        if self.queue1.qsize() :
            try:
                
                data1 = self.queue1.get()
               
                
                
                self.senderentry.delete(0,'end')
                self.senderentry.insert(0,data1)

                                
                self.queue1.task_done()
                
                
            except qu.Empty:
                pass
                print("hai")
        if self.queue2.qsize():
            try:
                
                
                data2 = self.queue2.get()
                
                self.recevierentry.delete(0,'end')
                self.recevierentry.insert(0,data2)                
                self.queue2.task_done()
                
            except qu.Empty:
                pass
                print("hai")        
        self.after(POLLING_TIME, self.queue_polling)
                 
    def close(self):
        print("Application-Shutdown")
        self.app_thread.join()
        self.master.destroy()
  
  

def main1():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
     
    app = Application(app_win).pack(fill='both', expand=True)
     
    app_win.mainloop()
def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
     
    app = application(app_win).pack(fill='both', expand=True)
     
    app_win.mainloop()    
#--------------------------------------------------------------------------------------------------------#    
def secondmain():
    app_win = tk.Tk()
    app_win.title("Mail Automation")
    #app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
    #app_win.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))    
        #roots.mainloop() 
    app = secondwindow(app_win)
     
    app_win.mainloop()

mainwindow()
