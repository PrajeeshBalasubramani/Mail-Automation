from __future__ import print_function
import smtplib
from tkinter import *
import numpy as np
from tkinter import ttk 
import tkinter 
import tkinter as tk
import time
import datetime
import urllib
import urllib.request as ur
import sys
import os
import schedule
import logging
import logging.config
import threading
import  tkinter.messagebox
import random
import glob
import logging.handlers
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
APP_WIDTH = 900
APP_HEIGHT = 300
UPDATE_TIME = 1000 # Milliseconds

QUEUE_SIZE = 500
POLLING_TIME = 1000
from email.mime.text import MIMEText
global tri
global bac
tri=0
bac=0
class mainwindow(object):
    ls=[] #recevier emailids
    lt=[]#recevier names
    xs=[] #signin emailids
    ys=[] #signin passwords
    lg=[]  #sample emailids
    lh=[] #sample names
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
        self.x=open('EntersigninEmailID.txt','r')#inquotes
        self.xr=self.x.read()
        mainwindow.xs = self.xr.split(",")
        self.y=open('EntersigninEmailPassword.txt','r')#inquotes
        self.yr=self.y.read()
        mainwindow.ys =self.yr.split(",")
        self.s= open('EnterRecevierEmails.txt','r')
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
        numberentry=0
        codeentry=0
        self.g=open('quotesone.txt','r',encoding="utf8")
        self.gr=self.g.read()
        prop = self.gr.split("||")
        quote=random.choice(prop)
        self.master = master
        self.intruction = Label(self.master, text='VEDIC FOLKS',font='Italic 25 bold',fg="green")
        
        self.intruction.grid(row=0, column=2, sticky=W)
        
        self.image = tk.PhotoImage(file="image.gif")
        self.label = tk.Label(image=self.image)
        self.label.grid(row=0,column=0)
        self.title = Label(self.master, text='Mail Automation',font='Italic 15 bold',fg="black")
        
        self.title.grid(row=1, column=2, sticky=W)
        self.name = Label(self.master, text='ON TIME:',font='Helvetica 13 bold')
        self.name.grid(row=3,column=1,sticky=E)
        self.Sample= Button(self.master, text='Sample',command=samplepath,bg="blue",fg="white",)
        self.Sample.grid(row=5,column=2,sticky=W)
        self.name1 = Label(self.master, text=' ',font='Helvetica 13 bold')
        self.name1.grid(row=4,column=2)
        self.Actual= Button(self.master, text='Regular',command=self.receviernumber,bg="blue",fg="white",) 
        self.Actual.grid(row=3, column=2,sticky=W)
        self.name1 = Label(self.master, text=' ',font='Helvetica 13 bold')
        self.name1.grid(row=6,column=2)
        self.name2 = Label(self.master, text='SCHEDULE TIME:',font='Helvetica 13 bold')
        self.name2.grid(row=3,column=3,sticky=E)
        self.Sample= Button(self.master, text='Schedule',command=main,bg="blue",fg="white",)
        self.Sample.grid(row=3,column=4,sticky=W)
        self.btn_frm_r = tk.Frame(self.master, background='yellow', width=600, height=50)
        self.btn_frm_r.grid(column=0, row=8 , columnspan= 10)
        self.name1 = Label(self.btn_frm_r, text=quote,font='Helvetica 13 bold')
        self.name1.grid(column=0,row=8,sticky=W)
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
        secondwindow.numberentry= tk.Entry(roots)
        secondwindow.numberentry.grid(row=2, column=1)
        secondwindow.codeentry= tk.Entry(roots)
        secondwindow.codeentry.grid(row=3, column=1)
        self.B1=Button(roots, text=" Start  ",bg="blue",fg="white",command=actualpath
            ).grid(row=5,column=1)
        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        roots.mainloop()

    
class AppThread(threading.Thread):

    def __init__(self, queue,queue1,a,b):
        self.queue = queue
        self.queue1 = queue1
        self.a=a
        self.b=b
        
        threading.Thread.__init__(self,target=self.run)
        self.start()
        #threading.Thread.__init__(self,target=self.run1)
        #self.start()
    def run(self):
        
        num=self.a
        
        self.update_queue(num)
        self.run1()
    def run1(self):
        
        num1=self.b
        self.update_queue1(num1)
    def update_queue(self,num):
        self.queue.put(num)
        self.queue.join()
    def update_queue1(self,num1):
        self.queue1.put(num1)
        self.queue1.join() 
class Sample(tk.Frame,mainwindow):

    def __init__(self,parent):
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
        self.app_thread = None
        self.queue = qu.Queue(QUEUE_SIZE)
        self.queue1 = qu.Queue(QUEUE_SIZE)
        self.k = 600
        self.s = 150 
        self.wk = parent.winfo_screenwidth() 
        self.hw = parent.winfo_screenheight() 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        parent.title("Mail Automation")
        self.frame_head = tk.Frame(parent, width=600, height=50)
        self.frame_head.grid(column=0, row=0 , columnspan= 10)
        self.title = Label(self.frame_head, text='Mail Automation',font='Italic 15 bold',fg="black")
        self.title.grid(row=0, column=1)
        self.subjecth=Label(self.frame_head,text='Subject:') 
        self.subjecth.grid(row=1,column=0,sticky=E)
        self.subject=Label(self.frame_head)
        self.subject.grid(row=1,column=1,sticky=W) 
        self.receviernumber = Label(parent, text='From:')
        self.receviernumber.grid(row=2)
        self.code = Label(parent, text='To:')
        self.code.grid(row=3)
        self.numberentry= tk.Entry(parent)
        self.numberentry.grid(row=2, column=1)
        self.codeentry= tk.Entry(parent)
        self.codeentry.grid(row=3, column=1)
        self.B1=Button(parent, text=" Start  ",bg="blue",fg="white",
            ).grid(row=5,column=1)
        parent.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        #self.multithreading()
        multi = threading.Thread(target=self.multithreading)
        multi.start()
    def multithreading(self):
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
            sub=self.cr[11:]
            self.subject.config(text=str(sub))
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
                        self.start_thread(self.xs[0],self.lg[i])
                        multi = threading.Thread(target=self.queue_polling1)
                        multi.start()
                        time.sleep(1)
                        multi = threading.Thread(target=self.queue_polling2)
                        multi.start()
                        time.sleep(2)
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
                        self.text.insert(END,"Error: MailID {} \n".format(self.xs[0]))
                        self.text.insert(END,"Error: Sent upto {} \n".format(i))
                        logging.error("Unexpected Error Occured")
                        logging.error(str(now))
                        logging.error("Sent upto:%d"%i)
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        roots.mainloop()
                        break
            else:
                logging.debug('Contact Developer...Needs Renovation.')
                tkinter.messagebox.showinfo('Information','Contact Developer...Needs Renovation.')
                
        
    def start_thread(self,a,b):
        
        self.app_thread = AppThread(
            self.queue,self.queue1,a,b)
        #else:
            #if not self.app_thread.isAlive():
        #self.app_thread = AppThread(
        #self.queue,a) 
    def queue_polling1(self):
        
        if self.queue.qsize() :
            try:
                a = self.queue.get()
                #print(a,"2")
                self.numberentry.delete(0,END)
                self.numberentry.insert(0,a)
                self.queue.task_done()
            except qu.Empty: 
                pass
    def queue_polling2(self):
        
        if self.queue1.qsize() :
            try:
                b = self.queue1.get()
                
                self.codeentry.delete(0,END)
                self.codeentry.insert(0,b)
                #time.sleep(2)
                #self.queue.task_done()
            except qu.Empty: 
                pass                      
        #self.after(POLLING_TIME, self.queue_polling)
                 
    def close(self):
        #print("Application-Shutdown")
        self.app_thread.join()
        self.master.destroy()
class AppThread1(threading.Thread):

    def __init__(self, queue,queue1,a,b):
        self.queue = queue
        self.queue1 = queue1
        self.a=a
        self.b=b
        
        threading.Thread.__init__(self,target=self.run)
        self.start()
        #threading.Thread.__init__(self,target=self.run1)
        #self.start()
    def run(self):
        
        num=self.a
        
        self.update_queue(num)
        self.run1()
    def run1(self):
        
        num1=self.b
        self.update_queue1(num1)
    def update_queue(self,num):
        self.queue.put(num)
        self.queue.join()
    def update_queue1(self,num1):
        self.queue1.put(num1)
        self.queue1.join()
class Actual(tk.Frame,mainwindow):

    def __init__(self,parent):
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
        self.app_thread = None
        self.queue = qu.Queue(QUEUE_SIZE)
        self.queue1 = qu.Queue(QUEUE_SIZE)
        self.k = 600
        self.s = 150 
        self.wk = parent.winfo_screenwidth() 
        self.hw = parent.winfo_screenheight() 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        parent.title("Mail Automation") 
        self.frame_head = tk.Frame(parent, width=600, height=50)
        self.frame_head.grid(column=0, row=0 , columnspan= 10)
        self.title = Label(self.frame_head, text='Mail Automation',font='Italic 15 bold',fg="black")
        self.title.grid(row=0, column=1)
        self.subjecth=Label(self.frame_head,text='Subject:') 
        self.subjecth.grid(row=1,column=0,sticky=E)
        self.subject=Label(self.frame_head)
        self.subject.grid(row=1,column=1,sticky=W)
        self.receviernumber = Label(parent, text='From:')
        self.receviernumber.grid(row=2)
        self.code = Label(parent, text='To:')
        self.code.grid(row=3)
        self.numberentry= tk.Entry(parent)
        self.numberentry.grid(row=2, column=1)
        self.codeentry= tk.Entry(parent)
        self.codeentry.grid(row=3, column=1)
        self.B1=Button(parent, text=" Start  ",bg="blue",fg="white",
            ).grid(row=5,column=1)
        parent.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        #self.multithreading()
        multi = threading.Thread(target=self.multithreading1)
        multi.start()
    def multithreading1(self):
        global numberentry
        global codeentry
        global ment
        #ment=StringVar()
        logging.debug('Selected Actual Customers Option')
        j=0
        k=1
        df=secondwindow.codeentry.get()
        self.uo=secondwindow.numberentry.get()
        
        self.uo=int(self.uo)

        
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
            sub=self.cr[11:]
            self.subject.config(text=str(sub))
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
                        server.login(self.xs[j], self.ys[j])  # Sender Mail, Sender Mail Password
                        server.sendmail(self.xs[j], [self.ls[i]], msg_full)
                        self.start_thread(self.xs[j],self.ls[i])
                        multi = threading.Thread(target=self.queue_polling1)
                        multi.start()
                        time.sleep(1)
                        multi = threading.Thread(target=self.queue_polling2)
                        multi.start()
                        time.sleep(2)
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
                        self.text.insert(END,"Error section j={}".format(j))
                        logging.error("Unexpected Error Occured")
                        logging.error(str(now))
                        logging.error("Sent upto: %d"%i)
                        logging.error("Sent with: %d"%j)
                        j=j+1
                        k=0
                        continue
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        roots.mainloop()

            elif i>=500:
                logging.debug('Contact Developer...Needs Renovation.')
                print("Contact Developer.... Needs Renovation.")
    def start_thread(self,a,b):
       
        #if self.app_thread == None:
        #print(a)
        self.app_thread = AppThread1(
            self.queue,self.queue1,a,b)
        #else:
            #if not self.app_thread.isAlive():
        #self.app_thread = AppThread(
        #self.queue,a) 
    def queue_polling1(self):
        
        if self.queue.qsize() :
            try:
                a = self.queue.get()
                #print(a,"2")
                self.numberentry.delete(0,END)
                self.numberentry.insert(0,a)
                self.queue.task_done()
            except qu.Empty: 
                pass
    def queue_polling2(self):
        
        if self.queue1.qsize() :
            try:
                b = self.queue1.get()
                
                self.codeentry.delete(0,END)
                self.codeentry.insert(0,b)
                #time.sleep(2)
                #self.queue.task_done()
            except qu.Empty: 
                pass                      
        #self.after(POLLING_TIME, self.queue_polling)            

def samplepath():
    root = tk.Tk()
    app = Sample(root)
    
    root.mainloop()
def actualpath():
    root = tk.Tk()
    app = Actual(root)
    
    root.mainloop()
class Application(object):
    ls=[] #recevier emailids
    lt=[] #recevier names
    xs=[] #signin emailids
    ys=[] #signin passwords
    lg=[] #sample emailids
    lh=[] #sample names
    vs=[]
    g= open('EnterSampleEmails.txt','r')
    gr=g.read()
    lg = gr.split(",")
    time.sleep(3)
    h=open("EnterSampleNames.txt",'r')
    th=h.read()
    lh=th.split(",")
    time.sleep(3)
    v=open('EnterIDs.txt','r')#inquotes
    vr=v.read()
    vs =vr.split(",")
    x=open('EntersigninEmailID.txt','r')#inquotes
    xr=x.read()
    xs = xr.split(",")
    y=open('EntersigninEmailPassword.txt','r')#inquotes
    yr=y.read()
    ys = yr.split(",")
    s= open('EnterRecevierEmails.txt','r') 
    sr=s.read()
    ls = sr.split(",")
    time.sleep(3)
    t=open("EnterRecevierNames.txt",'r')
    tr=t.read()
    lt=tr.split(",")
    time.sleep(3)
    c= open('Entersubject.txt','r')
    cr=c.read()#inquotes
    a = open('EntertheHTMLPart-I.txt','r')
    ar=a.read()
    im= open('EnterImagePart.txt','r')
    imr=im.read()
    b= open('EntertheHTMLPart-II.txt','r')
    br=b.read()
    def __init__(self,parent):
        self.k = 600
        self.s = 150 
        self.wk = parent.winfo_screenwidth() 
        self.hw = parent.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        parent.title("Mail Automation") 
        tk.Label(parent, text="Welcome to Mail Automation Application",font='Italic 13 bold',fg="black").grid(column=1, row=1, sticky=W)
        self.receviernumber = Label(parent, text='Enter Sending Day In Three Letters:')
        self.receviernumber.grid(row=2)
        self.code = Label(parent, text='Enter Sending Time')
        self.code.grid(row=3)
        Application.numberentry= tk.Entry(parent)
        Application.numberentry.grid(row=2, column=1,sticky=W)
        Application.codeentry= tk.Entry(parent)
        Application.codeentry.grid(row=3, column=1,sticky=W)
        self.text=tk.Label(parent)
        self.text.grid(row=4,column=1)
        self.B1=Button(parent, text=" Start  ",bg="blue",fg="white",command=scd
            ).grid(row=5,column=1,sticky=W)
        parent.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        #self.multithreading()

    def internetcheck(self):
        try:
            ur.urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=aNA8WtaQBayIX7Dop5gGm', timeout=1)
            #urllib.urlopen('https://www.google.co.in/?gfe_rd=cr&dcr=0&ei=aNA8WtaQBayIX7Dop5gGm', timeout=1) #to check internet
            return True
        except URLError as e:
            return False

class AppThread2(threading.Thread):

    def __init__(self, queue,queue1,a,b):
        self.queue = queue
        self.queue1 = queue1
        self.a=a
        self.b=b
        
        threading.Thread.__init__(self,target=self.run)
        self.start()
        #threading.Thread.__init__(self,target=self.run1)
        #self.start()
    def run(self):
        
        num=self.a
        self.update_queue(num)
        self.run1()
    def run1(self):
        
        num1=self.b
        self.update_queue1(num1)
    def update_queue(self,num):
        self.queue.put(num)
        self.queue.join()
    def update_queue1(self,num1):
        self.queue1.put(num1)
        self.queue1.join()
class solve(tk.Frame,Application):

    def __init__(self,parent):
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
        solve.v = StringVar()
        self.app_thread = None
        self.queue = qu.Queue(QUEUE_SIZE)
        self.queue1 = qu.Queue(QUEUE_SIZE)
        self.k = 600
        self.s = 150 
        self.wk = parent.winfo_screenwidth() 
        self.hw = parent.winfo_screenheight() 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        self.frame_head = tk.Frame(parent, width=600, height=50)
        self.frame_head.grid(column=0, row=0 , columnspan= 10)
        self.title = Label(self.frame_head, text='Mail Automation',font='Italic 15 bold',fg="black")
        self.title.grid(row=0, column=1)
        parent.title("Mail Automation")
        self.subjecth=Label(self.frame_head,text='Subject:') 
        self.subjecth.grid(row=1,column=0,sticky=E)
        self.subject=Label(self.frame_head)
        self.subject.grid(row=1,column=1,sticky=W)

        self.receviernumber = Label(parent, text='From:')
        self.receviernumber.grid(row=2,column=0,sticky=E)

        self.code = Label(parent, text='To:')
        self.code.grid(row=3,column=0,sticky=E)
        self.numberentry= tk.Entry(parent)
        self.numberentry.grid(row=2, column=1)
        self.codeentry= tk.Entry(parent)
        self.codeentry.grid(row=3, column=1)
        self.B1=Button(parent, text=" Start  ",bg="blue",fg="white",
            ).grid(row=5,column=1)
        parent.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        #self.multithreading()
        multi = threading.Thread(target=self.multithreading)
        multi.start()
    def multithreading(self):
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
        global tri
        global bac
        logging.debug('Selected Actual Customers Option')
        j=0
        if tri==1:
                i=bac
        for i in range(bac, len(self.ls)):
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
            message['To'] = self.ls[i]
            message['Subject'] =self. cr
            msg_full = message.as_string()
            sub=self.cr[11:]
            self.subject.config(text=str(sub))
            
            if i <= 500:
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
                                    bac=i
                                    tri=1
                                    self.multithreading()
                            else:
                                tkinter.messagebox.showinfo('Information','Awake from sleep, Got connection...')
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                self.multithreading()

                    else:
                        server = smtplib.SMTP('smtp.gmail.com:587')  # setting up service provider name : port number
                        server.starttls()  # asking server to start
                        server.login(self.xs[j], self.ys[j])  # Sender Mail, Sender Mail Password
                        server.sendmail(self.xs[j], [self.ls[i]], msg_full)
                        self.start_thread(self.xs[j],self.ls[i])
                        
                        multi = threading.Thread(target=self.queue_polling1)
                        multi.start()
                        time.sleep(1)
                        multi = threading.Thread(target=self.queue_polling2)
                        multi.start()
                        time.sleep(2)
                        server.quit()  # asking server to quit
                        time.sleep(10)
                        logging.debug('Sending to : %s'%self.lt[i])
                except smtplib.SMTPException:
                    if self.internetcheck() == False:
                        tkinter.messagebox.showwarning('Warning','Network Failure,waiting for connections')
                        logging.error(str(now))
                        logging.error("Internet Connection Not Established")
                        for u in range(0, 1000000):
                            if self.internetcheck() == False:
                                time.sleep(1)
                                tkinter.messagebox.showwarning('Warning',"Sleeping until internet connects...Trying %d times" % u)
                                sys.stdout.flush()
                                if self.internetcheck() == True:
                                    self.multithreading()
                            else:
                                tkinter.messagebox.showinfo('Information','Awake from sleep, Got connection...')
                                sys.stdout.flush()
                                logging.debug(str(now))
                                logging.debug("Internet Connection Established")
                                sys.stdout.flush()
                                self.multithreading()
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
                        self.text.insert(END,"Error section j={}".format(j))
                        logging.error("Unexpected Error Occured")
                        logging.error(str(now))
                        logging.error("Sent upto: %d"%i)
                        logging.error("Sent with: %d"%j)
                        j=j+1
                        k=0
                        continue
                        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
                        roots.mainloop()
            elif i>=500:
                logging.debug('Contact Developer...Needs Renovation.')
                print("Contact Developer.... Needs Renovation.")
    def start_thread(self,a,b):
        
        self.app_thread = AppThread2(
            self.queue,self.queue1,a,b)
        #else:
            #if not self.app_thread.isAlive():
        #self.app_thread = AppThread(
        #self.queue,a) 
    def queue_polling1(self):
        
        if self.queue.qsize() :
            try:
                a = self.queue.get()
                #print(a,"2")
                self.numberentry.delete(0,END)
                self.numberentry.insert(0,a)
                self.queue.task_done()
            except qu.Empty: 
                pass
    def queue_polling2(self):
        
        if self.queue1.qsize() :
            try:
                b = self.queue1.get()
                
                self.codeentry.delete(0,END)
                self.codeentry.insert(0,b)
                #time.sleep(2)
                #self.queue.task_done()
            except qu.Empty: 
                pass                      
        #self.after(POLLING_TIME, self.queue_polling)
def scd():
    global tri
    global bac
    tyme=Application.codeentry.get()
    daye=Application.numberentry.get()
    
    a=tyme
    b=daye
    if b=='sun':
        schedule.every().sunday.at(tyme).do(solvepath)
    elif b=='mon':
        schedule.every().monday.at(tyme).do(solvepath)
    elif b=='tue':
        schedule.every().tuesday.at(tyme).do(solvepath)
    elif b=='wed':
        schedule.every().wednesday.at(tyme).do(solvepath)
    elif b=='thu':
        schedule.every().thursday.at(tyme).do(solvepath)
    elif b=='fri':
        schedule.every().friday.at(tyme).do(solvepath)
    elif b=='sat':
        schedule.every().saturday.at(tyme).do(solvepath)
    while True:
        schedule.run_pending()
        time.sleep(1)
def solvepath():
    root = tk.Tk()
    app = solve(root)
    
    root.mainloop()

def main():
    root = tk.Tk()
    app = Application(root)
    
    root.mainloop()
#--------------------------------------------------------------------------------------------------------#    
def secondmain():#mainwindow
    app_win = tk.Tk()
    app_win.title("Mail Automation")
    
    app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
    
    app = secondwindow(app_win)
     
    app_win.mainloop()

mainwindow()