
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 00:11:39 2020

@author: Aiman
"""
from alicat import FlowController
import tkinter as tk
from tkinter import messagebox
import datetime
from PIL import ImageTk,Image
import time

flow_controller1 = FlowController(port='COM3', address='A')
flow_controller2 = FlowController(port='COM4', address='B')

# #===========================================  POLLING  ===================================================================================   
def MFC_polling_1():
    top_polling_1 = tk.Toplevel()
    top_polling_1.title('MFC A Polling')
    top_polling_1.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
    top_polling_1.geometry('290x250')
    
    data_1 = flow_controller1.get()
    lbl1 = tk.Label(top_polling_1, text= str(time.asctime()), padx=5, pady=5)
    lbl1.grid(row=0,column=0, columnspan=2, padx=5, pady=5, sticky='W')     
    lbl2 = tk.Label(top_polling_1, text="Reading for MFC A", padx=5)
    lbl2.grid(row=1,column=0, columnspan=2, sticky='W')
    
    lbl3 = tk.Label(top_polling_1, text="Absolute Pressure: ", width=20, anchor='w')
    lbl3.grid(row=2, column=0, sticky='W', padx=5)
    lbl4 = tk.Label(top_polling_1, text=data_1['pressure'] , width=10,relief='sunken')
    lbl4.grid(row=2, column=1, sticky='W')
    
    lbl5 = tk.Label(top_polling_1, text="Temperatue: ", width=20, anchor='w')
    lbl5.grid(row=3, column=0, sticky='W', padx=5)
    lbl6 = tk.Label(top_polling_1, text=data_1['temperature'] , width=10,relief='sunken')
    lbl6.grid(row=3, column=1, sticky='W')    
    
    lbl7 = tk.Label(top_polling_1, text="Volumetric Flow: ", width=20, anchor='w')
    lbl7.grid(row=4, column=0, sticky='W', padx=5)
    lbl8 = tk.Label(top_polling_1, text=data_1['volumetric_flow'] , width=10,relief='sunken')
    lbl8.grid(row=4, column=1, sticky='W')    
    
    lbl9 = tk.Label(top_polling_1, text="Mass Flow: ", width=20, anchor='w')
    lbl9.grid(row=5, column=0, sticky='W', padx=5)
    lbl10 = tk.Label(top_polling_1, text=data_1['mass_flow'] , width=10,relief='sunken')
    lbl10.grid(row=5, column=1, sticky='W')    
    
    lbl11 = tk.Label(top_polling_1, text="Set Point: ", width=20, anchor='w')
    lbl11.grid(row=6, column=0, sticky='W', padx=5)
    lbl12 = tk.Label(top_polling_1, text=data_1['setpoint'] , width=10,relief='sunken')
    lbl12.grid(row=6, column=1, sticky='W')    
    
    lbl13 = tk.Label(top_polling_1, text="Gas: ", width=20, anchor='w')
    lbl13.grid(row=7, column=0, sticky='W', padx=5)
    lbl14 = tk.Label(top_polling_1, text=data_1['gas'] , width=10,relief='sunken')
    lbl14.grid(row=7, column=1, sticky='W')

    lbl15 = tk.Label(top_polling_1, text="Control Point: ", width=20, anchor='w')
    lbl15.grid(row=8, column=0, sticky='W', padx=5)
    lbl16 = tk.Label(top_polling_1, text=data_1['control_point'] , width=10,relief='sunken')
    lbl16.grid(row=8, column=1, sticky='W')

def MFC_polling_2():
    top_polling_2 = tk.Toplevel()
    top_polling_2.title('MFC B Polling')
    top_polling_2.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
    top_polling_2.geometry('290x250')
    
    data_2 = flow_controller2.get()
    lbl1 = tk.Label(top_polling_2, text= str(time.asctime()), padx=5, pady=5)
    lbl1.grid(row=0,column=0, columnspan=2, padx=5, pady=5, sticky='W')     
    lbl2 = tk.Label(top_polling_2, text="Reading for MFC B", padx=5)
    lbl2.grid(row=1,column=0, columnspan=2, sticky='W')
    
    lbl3 = tk.Label(top_polling_2, text="Absolute Pressure: ", width=20, anchor='w')
    lbl3.grid(row=2, column=0, sticky='W', padx=5)
    lbl4 = tk.Label(top_polling_2, text=data_2['pressure'] , width=10,relief='sunken')
    lbl4.grid(row=2, column=1, sticky='W')
    
    lbl5 = tk.Label(top_polling_2, text="Temperatue: ", width=20, anchor='w')
    lbl5.grid(row=3, column=0, sticky='W', padx=5)
    lbl6 = tk.Label(top_polling_2, text=data_2['temperature'] , width=10,relief='sunken')
    lbl6.grid(row=3, column=1, sticky='W')    
    
    lbl7 = tk.Label(top_polling_2, text="Volumetric Flow: ", width=20, anchor='w')
    lbl7.grid(row=4, column=0, sticky='W', padx=5)
    lbl8 = tk.Label(top_polling_2, text=data_2['volumetric_flow'] , width=10,relief='sunken')
    lbl8.grid(row=4, column=1, sticky='W')    
    
    lbl9 = tk.Label(top_polling_2, text="Mass Flow: ", width=20, anchor='w')
    lbl9.grid(row=5, column=0, sticky='W', padx=5)
    lbl10 = tk.Label(top_polling_2, text=data_2['mass_flow'] , width=10,relief='sunken')
    lbl10.grid(row=5, column=1, sticky='W')    
    
    lbl11 = tk.Label(top_polling_2, text="Set Point: ", width=20, anchor='w')
    lbl11.grid(row=6, column=0, sticky='W', padx=5)
    lbl12 = tk.Label(top_polling_2, text=data_2['setpoint'] , width=10,relief='sunken')
    lbl12.grid(row=6, column=1, sticky='W')    
    
    lbl13 = tk.Label(top_polling_2, text="Gas: ", width=20, anchor='w')
    lbl13.grid(row=7, column=0, sticky='W', padx=5)
    lbl14 = tk.Label(top_polling_2, text=data_2['gas'] , width=10,relief='sunken')
    lbl14.grid(row=7, column=1, sticky='W')

    lbl15 = tk.Label(top_polling_2, text="Control Point: ", width=20, anchor='w')
    lbl15.grid(row=8, column=0, sticky='W', padx=5)
    lbl16 = tk.Label(top_polling_2, text=data_2['control_point'] , width=10,relief='sunken')
    lbl16.grid(row=8, column=1, sticky='W')
# #============================================================================================================

# #========================================= GAS LIST MODULE ================================================================================
def gas_list_module():
    
    global my_label
    global button_back
    global button_next
    global top_gas_list
    
    top_gas_list = tk.Toplevel()    
    top_gas_list.title('Gas List')
    top_gas_list.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
    
    my_label = tk.Label(top_gas_list, image=my_image1, borderwidth=3)
    my_label.grid(row=0, column=1, pady=10)
    my_label_status = tk.Label(top_gas_list, text='1/2', borderwidth=2, width=10)
    my_label_status.grid (row=1,column=1, pady=5)   
    
    button_back = tk.Button(top_gas_list, text='<<', padx=10, command=lambda: back(1))
    button_next = tk.Button(top_gas_list, text='>>', padx=10, command=lambda: forward(2))

    button_back.grid(row=0, column=0, padx=5, pady=5)
    button_next.grid(row=0, column=2, padx=5, pady=5)
    
def forward(image_number):
    global my_label
    global top_gas_list
    global button_next
    global button_back

    my_label.grid_forget()
    
    my_label = tk.Label(top_gas_list, image=image_list[image_number-1], borderwidth=3)
    my_label_status = tk.Label(top_gas_list, text='2/2', borderwidth=2, width=10)
    
    button_next = tk.Button(top_gas_list, text='>>', padx=10, command=lambda: forward(image_number+1), state='disable')
    button_back = tk.Button(top_gas_list, text='<<', padx=10, command=lambda: back(image_number-1), state='active')

    
    my_label.grid(row=0, column=1, pady=10)
    my_label_status.grid (row=1,column=1, pady=5)
    button_back.grid(row=0, column=0, padx=5, pady=5)
    button_next.grid(row=0, column=2, padx=5, pady=5)
    
            
def back(image_number):
    global my_label
    global button_next
    global button_back
    global top_gas_list

    my_label.grid_forget()
    
    my_label = tk.Label(top_gas_list, image=image_list[image_number-1], borderwidth=3)
    my_label.grid(row=0, column=1, pady=10)
    my_label_status = tk.Label(top_gas_list, text='1/2', borderwidth=2, width=10)
    
    button_next = tk.Button(top_gas_list, text='>>', padx=10, command=lambda: forward(image_number+1), state='active')
    button_back = tk.Button(top_gas_list, text='<<', padx=10, command=lambda: back(image_number-1), state='disable')
    
    my_label.grid(row=0, column=1, pady=10)
    my_label_status.grid (row=1,column=1, pady=5)
    button_back.grid(row=0, column=0, padx=5, pady=5)
    button_next.grid(row=0, column=2, padx=5, pady=5)



#=========================================     Main App      =======================================================================    

class Main_app:
    
    
    def __init__(self, master):
        self.Radiobutton1 = tk.Radiobutton(master, text="MFC A", variable=r, value=1, command= lambda: self.select_MFC(self.frame_1.winfo_children)).grid(row=0, column=0)
        self.Radiobutton2 = tk.Radiobutton(master, text="MFC B", variable=r, value=2, command= lambda: self.select_MFC(self.frame_2.winfo_children)).grid(row=0, column=1)
        
        self.frame_1 = tk.LabelFrame(master, text="Mass Flowrate A", padx=70, pady=20)
        self.frame_1.grid(row=1, column=0, padx=10, pady=10)
        
        oMenuWidth = len(max(user_decision_options, key=len))
        
        self.drop_1 = tk.OptionMenu(self.frame_1, menu_select_1, *user_decision_options)
        self.drop_1.grid(row=0, column=0)
        self.drop_1.config(width=oMenuWidth, relief="sunken", bg="white")
        self.button1 = tk.Button(self.frame_1, text="Proceed", command=lambda : self.user_decision_1(master), width=10).grid(row=1, column=0)
        self.top_streaming_1 = None
        
        self.frame_2 = tk.LabelFrame(master, text="Mass Flowrate B", padx=70, pady=20)
        self.frame_2.grid(row=1, column=1, padx=10, pady=10)
        
        self.drop_2 = tk.OptionMenu(self.frame_2, menu_select_2, *user_decision_options)
        self.drop_2.grid(row=0, column=0,)
        self.drop_2.config(width=oMenuWidth, relief="sunken", bg="white")
        self.button2 = tk.Button(self.frame_2, text="Proceed", command=lambda : self.user_decision_2(master), width=10).grid(row=1, column=0)
        self.top_streaming_2 = None

        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
        for child in self.frame_1.winfo_children():
            child.configure(state='disable', bg="white")
        for child in self.frame_2.winfo_children():
            child.configure(state='disable', bg="white")
            
    def select_MFC(self,winfo_children):
        r.get()
        
        if r.get()==1:
            for child in self.frame_1.winfo_children():
                child.configure(state='active',bg="white")
            for child in self.frame_2.winfo_children():
                child.configure(state='disable',bg="white")
        else:
            for child in self.frame_2.winfo_children():
                child.configure(state='active',bg="white") 
            for child in self.frame_1.winfo_children():
                child.configure(state='disable',bg="white")

    
    def user_decision_1(self, master):
        global top_streaming_1
            
        menu_select_1.get()
        if menu_select_1.get() == 'Poll':
            MFC_polling_1()                
        elif menu_select_1.get() == 'Stream':                
            self.New_interval_1(master)        
        elif menu_select_1.get() == 'Set Flowrate':
            self.New_flowrate_1(master)                            
        else:
            self.New_pressure_1(master)
        

    def user_decision_2(self,master):
         
        menu_select_2.get()
        if menu_select_2.get() == 'Poll':
            MFC_polling_2()    
        elif menu_select_2.get() == 'Stream':
            self.New_interval_2(master)
        elif menu_select_2.get() == 'Set Flowrate':
            self.New_flowrate_2(master)              
        else:
            self.New_pressure_2(master)        

#==========================================================================================================================================

#====================================================  NEW INTERVAL MFC A & B   ===================================================================


    def New_interval_1(self, master):
        
        if self.top_streaming_1 is None:
            self.top_interval_1 = tk.Toplevel(master)
    
            self.top_interval_1.title('Interval for MFC A')
            self.top_interval_1.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
            self.top_interval_1.geometry('300x110')
        
            self.set_lbl1 = tk.Label(self.top_interval_1, text='Mass Flowrate A', padx=5, pady=5).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='W')
            self.set_lbl2 = tk.Label(self.top_interval_1, text='Interval (in second):', padx=5, pady=5).grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky='W')
            self.entry_interval_1= tk.Entry(self.top_interval_1, textvariable=interval_1_var, width=10, borderwidth=3)
            self.entry_interval_1.grid(row=1, column=1)    
            
            self.label = tk.Label(self.top_interval_1, text='', width=13).grid(row=1, column=2)
            self.set_button = tk.Button(self.top_interval_1, text='Enter', command=lambda : self.Set_interval_1(master), width=5)
            self.set_button.grid(row=2,column=2, stick='E')
        else:
            self.message = tk.messagebox.showerror('Error',' Please close the current stream')
              
    
    def Set_interval_1(self,master):
        global interval_1
        try:
            if float(self.entry_interval_1.get()) <= 0:
                self.message = messagebox.showerror('User Input Error', 'Error!! Please enter a number greater than 0')
                return
            else:
                interval_1 = self.entry_interval_1.get()
                interval_1 = float(interval_1) * 1000
            
                self.entry_interval_1.delete(0, tk.END)
                pass
            
            self.openwindow_1(master)
            self.top_interval_1.destroy()
            return
        except ValueError:
            self.message = tk.messagebox.showerror('User Input Error', 'Error!! Please enter float number')


    def New_interval_2(self, master):
        
        if self.top_streaming_2 is None:
            self.top_interval_2 = tk.Toplevel(master)
    
            self.top_interval_2.title('Interval for MFC B')
            self.top_interval_2.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
            self.top_interval_2.geometry('300x110')
        
            self.set_lbl1 = tk.Label(self.top_interval_2, text='Mass Flowrate B', padx=5, pady=5).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='W')
            self.set_lbl2 = tk.Label(self.top_interval_2, text='Interval (in second):', padx=5, pady=5).grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky='W')
            self.entry_interval_2= tk.Entry(self.top_interval_2, textvariable=interval_2_var, width=10, borderwidth=3)
            self.entry_interval_2.grid(row=1, column=1)    
            
            self.label = tk.Label(self.top_interval_2, text='', width=13).grid(row=1, column=2)
            self.set_button = tk.Button(self.top_interval_2, text='Enter', command=lambda: self.Set_interval_2(master), width=5)
            self.set_button.grid(row=2,column=2, stick='E')
        
        else:
            self.message = tk.messagebox.showerror('Error',' Please close the current stream')
               
    
    def Set_interval_2(self,master):
        global interval_2
        try:
            if float(self.entry_interval_2.get()) <= 0:
                self.message = messagebox.showerror('User Input Error', 'Error!! Please enter a number greater than 0')
                return
            else:
                interval_2 = self.entry_interval_2.get()
                interval_2 = float(interval_2) * 1000
            
                self.entry_interval_2.delete(0, tk.END)
                pass
            
            self.openwindow_2(master)
            self.top_interval_2.destroy()
            return
        except ValueError:
            self.message = tk.messagebox.showerror('User Input Error', 'Error!! Please enter float number')

#====================================================  STREAMING MFC A  ===================================================================


    def streaming_history_1(self,master):
        
        self.top_history_1 = tk.Toplevel(master)
        
        self.top_history_1.title('MFC A Streaming History')
        self.top_history_1.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
        self.top_history_1.geometry('900x200')
        
        self.scrollbar_1 = tk.Scrollbar(self.top_history_1)
        self.scrollbar_1.pack(side='right', fill='y')
        
        self.listbox_1 = tk.Listbox(self.top_history_1, yscrollcommand=self.scrollbar_1.set)
        self.listbox_1.pack(side='left', fill='both', expand=True)
        
        self.scrollbar_1.config(command=self.listbox_1.yview)
        
        self.top_history_1.withdraw()
        
        self.top_history_1.protocol('WM_DELETE_WINDOW', self.top_history_1.withdraw)
    

    def loop_1(self):    
        self.data_1 = flow_controller1.get()
        
        self.streaming_lbl1 = tk.Label(self.top_streaming_1, text=str(time.asctime()), padx=5, pady=5).grid(row=0,column=0, columnspan=2, padx=5, pady=5, sticky='W') 
        self.lbl4 = tk.Label(self.top_streaming_1, text=self.data_1['pressure'] , width=10,relief='sunken')
        self.lbl4.grid(row=2, column=1, sticky='W')
        self.lbl6 = tk.Label(self.top_streaming_1, text=self.data_1['temperature'] , width=10,relief='sunken')
        self.lbl6.grid(row=3, column=1, sticky='W')
        self.lbl8 = tk.Label(self.top_streaming_1, text=self.data_1['volumetric_flow'] , width=10,relief='sunken')
        self.lbl8.grid(row=4, column=1, sticky='W') 
        self.lbl10 = tk.Label(self.top_streaming_1, text=self.data_1['mass_flow'] , width=10,relief='sunken')
        self.lbl10.grid(row=5, column=1, sticky='W') 
        self.lbl12 = tk.Label(self.top_streaming_1, text=self.data_1['setpoint'] , width=10,relief='sunken')
        self.lbl12.grid(row=6, column=1, sticky='W') 
        self.lbl14 = tk.Label(self.top_streaming_1, text=self.data_1['gas'] , width=10,relief='sunken')
        self.lbl14.grid(row=7, column=1, sticky='W')
        self.lbl16 = tk.Label(self.top_streaming_1, text=self.data_1['control_point'] , width=10,relief='sunken')
        self.lbl16.grid(row=8, column=1, sticky='W')
        
        self.listbox_1.insert('end', time.strftime("%H:%M:%S: ") + ' MFC A Data Flowrate: ' + str(flow_controller1.get()))   
    
        self.file_1.write(str(self.listbox_1.get('end')) + '\n' )
        
        self.loop = self.top_streaming_1.after(int(interval_1), self.loop_1)


    def openwindow_1(self, master):

        self.top_streaming_1 = tk.Toplevel(master)
         
        
        self.top_streaming_1.title('MFC A Streaming')
        self.top_streaming_1.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
        self.top_streaming_1.geometry('350x270')
          
        self.lbl2 = tk.Label(self.top_streaming_1, text="Live Reading for MFC A", padx=5)
        self.lbl2.grid(row=1,column=0, columnspan=2, sticky='W')
        
        self.lbl3 = tk.Label(self.top_streaming_1, text="Absolute Pressure: ", width=20, anchor='w')
        self.lbl3.grid(row=2, column=0, sticky='W', padx=5)
        
        self.lbl5 = tk.Label(self.top_streaming_1, text="Temperatue: ", width=20, anchor='w')
        self.lbl5.grid(row=3, column=0, sticky='W', padx=5)

        self.lbl7 = tk.Label(self.top_streaming_1, text="Volumetric Flow: ", width=20, anchor='w')
        self.lbl7.grid(row=4, column=0, sticky='W', padx=5)

        self.lbl9 = tk.Label(self.top_streaming_1, text="Mass Flow: ", width=20, anchor='w')
        self.lbl9.grid(row=5, column=0, sticky='W', padx=5)
       
        self.lbl11 = tk.Label(self.top_streaming_1, text="Set Point: ", width=20, anchor='w')
        self.lbl11.grid(row=6, column=0, sticky='W', padx=5)
       
        self.lbl13 = tk.Label(self.top_streaming_1, text="Gas: ", width=20, anchor='w')
        self.lbl13.grid(row=7, column=0, sticky='W', padx=5)
    
        self.lbl15 = tk.Label(self.top_streaming_1, text="Control Point: ", width=20, anchor='w')
        self.lbl15.grid(row=8, column=0, sticky='W', padx=5)

        
        self.streaming_lbl6 = tk.Label(self.top_streaming_1, text='Start streaming at '+ str(time.asctime()), padx=5).grid(row=9, column=0, columnspan=2, sticky='W')
        self.streaming_lbl5 = tk.Label(self.top_streaming_1, text='Interval: '+ str(interval_1/1000) + ' seconds', padx=5).grid(row=10, column=0, columnspan=2, sticky='W')
         
        self.label = tk.Label(self.top_streaming_1, text='', width=3).grid(row=10, column=2)         
        self.set_button = tk.Button(self.top_streaming_1, text='See History', command=lambda: self.top_history_1.deiconify())
        self.set_button.grid(row=10,column=3, stick='E')
        
        self.streaming_history_1(master)

        x = datetime.datetime.now()
        self.file_1 = open("MFC_A_" + x.strftime("%B_%d_(%I%M%p)") + ".txt","a")
        self.file_1.write(str(time.asctime()) + '\n' )         
        self.loop_1()

        self.top_streaming_1.protocol('WM_DELETE_WINDOW', self.removewindow_1)
            

#==========================================================================================================================================

#====================================================  STREAMING MFC B  ===================================================================

    def streaming_history_2(self,master):
        
        self.top_history_2 = tk.Toplevel(master)
        
        self.top_history_2.title('MFC B Streaming History')
        self.top_history_2.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
        self.top_history_2.geometry('900x200')
        
        self.scrollbar_2 = tk.Scrollbar(self.top_history_2)
        self.scrollbar_2.pack(side='right', fill='y')
        
        self.listbox_2 = tk.Listbox(self.top_history_2, yscrollcommand=self.scrollbar_2.set)
        self.listbox_2.pack(side='left', fill='both', expand=True)
        
        self.scrollbar_2.config(command=self.listbox_2.yview)
        
        self.top_history_2.withdraw()
        
        self.top_history_2.protocol('WM_DELETE_WINDOW', self.top_history_2.withdraw)


    def loop_2(self):    
        self.data_2 = flow_controller2.get()
        
        self.streaming_lbl1 = tk.Label(self.top_streaming_2, text=str(time.asctime()), padx=5, pady=5).grid(row=0,column=0, columnspan=2, padx=5, pady=5, sticky='W') 
        self.lbl4 = tk.Label(self.top_streaming_2, text=self.data_2['pressure'] , width=10,relief='sunken')
        self.lbl4.grid(row=2, column=1, sticky='W')
        self.lbl6 = tk.Label(self.top_streaming_2, text=self.data_2['temperature'] , width=10,relief='sunken')
        self.lbl6.grid(row=3, column=1, sticky='W')
        self.lbl8 = tk.Label(self.top_streaming_2, text=self.data_2['volumetric_flow'] , width=10,relief='sunken')
        self.lbl8.grid(row=4, column=1, sticky='W') 
        self.lbl10 = tk.Label(self.top_streaming_2, text=self.data_2['mass_flow'] , width=10,relief='sunken')
        self.lbl10.grid(row=5, column=1, sticky='W') 
        self.lbl12 = tk.Label(self.top_streaming_2, text=self.data_2['setpoint'] , width=10,relief='sunken')
        self.lbl12.grid(row=6, column=1, sticky='W') 
        self.lbl14 = tk.Label(self.top_streaming_2, text=self.data_2['gas'] , width=10,relief='sunken')
        self.lbl14.grid(row=7, column=1, sticky='W')
        self.lbl16 = tk.Label(self.top_streaming_2, text=self.data_2['control_point'] , width=10,relief='sunken')
        self.lbl16.grid(row=8, column=1, sticky='W')
        
        self.listbox_2.insert('end', time.strftime("%H:%M:%S: ") + ' MFC B Data Flowrate: ' + str(flow_controller2.get())) 
    
        self.file_2.write(str(self.listbox_2.get('end')) + '\n' )
        
        self.loop = self.top_streaming_2.after(int(interval_2), self.loop_2)

    def openwindow_2(self, master):

        self.top_streaming_2 = tk.Toplevel(master)
         
        self.top_streaming_2.title('MFC B Streaming')
        self.top_streaming_2.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
        self.top_streaming_2.geometry('350x270')
        
        self.lbl2 = tk.Label(self.top_streaming_2, text="Live Reading for MFC B", padx=5)
        self.lbl2.grid(row=1,column=0, columnspan=2, sticky='W')
        
        self.lbl3 = tk.Label(self.top_streaming_2, text="Absolute Pressure: ", width=20, anchor='w')
        self.lbl3.grid(row=2, column=0, sticky='W', padx=5)
        
        self.lbl5 = tk.Label(self.top_streaming_2, text="Temperatue: ", width=20, anchor='w')
        self.lbl5.grid(row=3, column=0, sticky='W', padx=5)

        self.lbl7 = tk.Label(self.top_streaming_2, text="Volumetric Flow: ", width=20, anchor='w')
        self.lbl7.grid(row=4, column=0, sticky='W', padx=5)

        self.lbl9 = tk.Label(self.top_streaming_2, text="Mass Flow: ", width=20, anchor='w')
        self.lbl9.grid(row=5, column=0, sticky='W', padx=5)
       
        self.lbl11 = tk.Label(self.top_streaming_2, text="Set Point: ", width=20, anchor='w')
        self.lbl11.grid(row=6, column=0, sticky='W', padx=5)
       
        self.lbl13 = tk.Label(self.top_streaming_2, text="Gas: ", width=20, anchor='w')
        self.lbl13.grid(row=7, column=0, sticky='W', padx=5)
    
        self.lbl15 = tk.Label(self.top_streaming_2, text="Control Point: ", width=20, anchor='w')
        self.lbl15.grid(row=8, column=0, sticky='W', padx=5)

        
        self.streaming_lbl6 = tk.Label(self.top_streaming_2, text='Start streaming at '+ str(time.asctime()), padx=5).grid(row=9, column=0, columnspan=2, sticky='W')
        self.streaming_lbl5 = tk.Label(self.top_streaming_2, text='Interval: '+ str(interval_2/1000) + ' seconds', padx=5).grid(row=10, column=0, columnspan=2, sticky='W')
         
        self.label = tk.Label(self.top_streaming_2, text='', width=3).grid(row=10, column=2)         
        self.set_button = tk.Button(self.top_streaming_2, text='See History', command=lambda: self.top_history_2.deiconify())
        self.set_button.grid(row=10,column=3, stick='E')
        
        self.streaming_history_2(master)

        x = datetime.datetime.now()
        self.file_2 = open("MFC_B_" + x.strftime("%B_%d_(%I%M%p)") + ".txt","a")
        self.file_2.write(str(time.asctime()) + '\n' )        
        self.loop_2()

        self.top_streaming_2.protocol('WM_DELETE_WINDOW', self.removewindow_2)
                         
#==========================================================================================================================================

#====================================================  Flowrate MFC A & B   ===================================================================
    def New_flowrate_1(self, master):
        global entry_flowrate_1
        global entry_gas_1
        self.top_New_flowrate_1 = tk.Toplevel(master)    
        self.top_New_flowrate_1.title('MFC A Configuration')
        self.top_New_flowrate_1.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
        self.top_New_flowrate_1.geometry('310x150')
        
        self.set_lbl1 = tk.Label(self.top_New_flowrate_1, text='Mass Flowrate A', padx=5, pady=5)
        self.set_lbl1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='W')
        
        self.set_lbl2 = tk.Label(self.top_New_flowrate_1, text='Flowrate:', padx=5, pady=5)
        self.set_lbl2.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky='W')
        self.entry_flowrate_1 = tk.Entry(self.top_New_flowrate_1, textvariable=flow_rate_1_var, width=10, borderwidth=3)
        self.entry_flowrate_1.grid(row=1, column=1)
        
        self.set_lbl3 = tk.Label(self.top_New_flowrate_1, text='Gas:', padx=5, pady=5)
        self.set_lbl3.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky='W')
        self.entry_gas_1 = tk.Entry(self.top_New_flowrate_1, textvariable=gas_1_var, width=10, borderwidth=3)
        self.entry_gas_1.grid(row=2, column=1)
    
        self.set_button = tk.Button(self.top_New_flowrate_1, text='See Gas List', command=gas_list_module, width=10)
        self.set_button.grid(row=2,column=3, stick='E')
    
    
        self.label = tk.Label(self.top_New_flowrate_1, text='', padx=40)
        self.label.grid(row=1, column=2)
        self.set_button = tk.Button(self.top_New_flowrate_1, text='Enter', command=self.Set_flowrate_1, width=10)
        self.set_button.grid(row=3,column=3, stick='E')
    
    def Set_flowrate_1(self):
        global flow_rate_1
        global gas_1
        
        if self.entry_flowrate_1.get() == '' or self.entry_gas_1.get() == '':
            self.message = messagebox.showerror('User Input Error', 'Error!! Please enter value for both FLOWRATE and TYPE OF GAS')
            return
        else:
            try:
    
                if float(self.entry_flowrate_1.get()) < 0 or float(self.entry_flowrate_1.get()) > 200:
                    self.message = messagebox.showerror('User Input Error', 'Error!! Please enter float number (0 sccm - 200 sccm)')
    
                    return
                else:
                    flow_rate_1 = self.entry_flowrate_1.get()
                    flow_rate_1 = float(flow_rate_1)
                    flow_controller1._set_control_point("flow")
                    flow_controller1.set_flow_rate(flow_rate_1)                    
                    pass
                
                if self.entry_gas_1.get() in Gas_list:
                    gas_1 = self.entry_gas_1.get()
                    flow_controller1.set_gas(gas_1)
                    pass
                else:
                  self.meesage = messagebox.showerror('User Input Error', 'Error!! Please select gas from the list')
                  return
                
            except ValueError:
                self.message = messagebox.showerror('User Input Error', 'Error!! Please enter float number (0 sccm - 200 sccm)')
                return
            
            self.entry_flowrate_1.delete(0, tk.END)
            self.entry_gas_1.delete(0, tk.END)
            
            self.top_New_flowrate_1.destroy()

    def New_flowrate_2(self,master):
        
        global entry_flowrate_2
        global entry_gas_2

        self.top_New_flowrate_2 = tk.Toplevel(master)    
        self.top_New_flowrate_2.title('MFC B Configuration')
        self.top_New_flowrate_2.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
        self.top_New_flowrate_2.geometry('310x150')
        
        self.set_lbl1 = tk.Label(self.top_New_flowrate_2, text='Mass Flowrate B', padx=5, pady=5)
        self.set_lbl1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='W')
        
        self.set_lbl2 = tk.Label(self.top_New_flowrate_2, text='Flowrate:', padx=5, pady=5)
        self.set_lbl2.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky='W')
        self.entry_flowrate_2 = tk.Entry(self.top_New_flowrate_2, textvariable=flow_rate_2_var, width=10, borderwidth=3)
        self.entry_flowrate_2.grid(row=1, column=1)
        
        self.set_lbl3 = tk.Label(self.top_New_flowrate_2, text='Gas:', padx=5, pady=5)
        self.set_lbl3.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky='W')
        self.entry_gas_2 = tk.Entry(self.top_New_flowrate_2, textvariable=gas_2_var, width=10, borderwidth=3)
        self.entry_gas_2.grid(row=2, column=1)
        
        self.set_button = tk.Button(self.top_New_flowrate_2, text='See Gas List', command=gas_list_module, width=10)
        self.set_button.grid(row=2,column=3, stick='E')
            
        self.label = tk.Label(self.top_New_flowrate_2, text='', padx=40).grid(row=1, column=2)
        self.set_button = tk.Button(self.top_New_flowrate_2, text='Enter', command=self.Set_flowrate_2, width=10)
        self.set_button.grid(row=3,column=3, stick='E')
            
    def Set_flowrate_2(self):
        global flow_rate_2
        global gas_2
        
        if self.entry_flowrate_2.get()== '' or self.entry_gas_2.get()== '':
            self.message = messagebox.showerror('User Input Error', 'Error!! Please enter value for both FLOWRATE and TYPE OF GAS')
            return
        else:
            try:               
            
                if float(self.entry_flowrate_2.get()) < 0 or float(self.entry_flowrate_2.get()) > 200:
                    self.message = messagebox.showerror('User Input Error', 'Error!! Please enter float number (0 sccm - 200 sccm)')
                    return
                else:
                    flow_rate_2 = self.entry_flowrate_2.get()
                    flow_rate_2 = float(flow_rate_2)
                    flow_controller2._set_control_point("flow")
                    flow_controller2.set_flow_rate(flow_rate_2)
                    pass
                
                if self.entry_gas_2.get() in Gas_list:
                    gas_2 = self.entry_gas_2.get()
                    flow_controller2.set_gas(gas_2)
                    pass
                else:
                  messagebox.showerror('User Input Error', 'Error!! Please select gas from the list' )
                  return
                
            except ValueError:
                messagebox.showerror('User Input Error', 'Error!! Please enter float number (0 sccm - 200 sccm)')
                return
            
            self.entry_flowrate_2.delete(0, tk.END)
            self.entry_gas_2.delete(0, tk.END)
            
            self.top_New_flowrate_2.destroy()
    
#==========================================================================================================================================

#====================================================  Pressure MFC A & B   ===================================================================    

    def New_pressure_1(self,master):
        
        global entry_pressure_1
        global entry_gas_1
        
        self.top_New_pressure_1 = tk.Toplevel(master)    
        self.top_New_pressure_1.title('MFC A Configuration')
        self.top_New_pressure_1.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
        self.top_New_pressure_1.geometry('310x150')
        
        self.set_lbl1 = tk.Label(self.top_New_pressure_1, text='Mass Flowrate A', padx=5, pady=5)
        self.set_lbl1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='W')
        
        self.set_lbl2 = tk.Label(self.top_New_pressure_1, text='Pressure:', padx=5, pady=5)
        self.set_lbl2.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky='W')
        self.entry_pressure_1 = tk.Entry(self.top_New_pressure_1, textvariable=pressure_1_var, width=10, borderwidth=3)
        self.entry_pressure_1.grid(row=1, column=1)
            
        self.set_lbl3 = tk.Label(self.top_New_pressure_1, text='Gas:', padx=5, pady=5)
        self.set_lbl3.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky='W')
        self.entry_gas_1 = tk.Entry(self.top_New_pressure_1, textvariable=gas_1_var, width=10, borderwidth=3)
        self.entry_gas_1.grid(row=2, column=1)
    
        self.set_button = tk.Button(self.top_New_pressure_1, text='See Gas List', command=gas_list_module, width=10)
        self.set_button.grid(row=2,column=3, stick='E')
    
    
        self.label = tk.Label(self.top_New_pressure_1, text='', padx=40).grid(row=1, column=2)
        self.set_button = tk.Button(self.top_New_pressure_1, text='Enter', command=self.Set_pressure_1, width=10)
        self.set_button.grid(row=3,column=3, stick='E')
    
    def Set_pressure_1(self):
        global pressure_1
        global gas_1
        
        if self.entry_pressure_1.get() == '' or self.entry_gas_1.get()== '':
            self.message = messagebox.showerror('User Input Error', 'Error!! Please enter value for both PRESSURE and TYPE OF GAS')
            return
        else:
            try:
            
                if float(self.entry_pressure_1.get()) > 160:
                    self.message = messagebox.showerror('User Input Error', 'Error!! Please enter pressure (max = 160 psia)')
                    return
                else:
                    pressure_1 = self.entry_pressure_1.get()
                    pressure_1 = float(pressure_1)
                    flow_controller1._set_control_point("pressure")
                    flow_controller1.set_pressure(pressure_1)
                    pass
                
                if self.entry_gas_1.get() in Gas_list:
                    gas_1 = self.entry_gas_1.get()
                    flow_controller1.set_gas(gas_1)
                    pass
                else:
                  self.message = messagebox.showerror('User Input Error', 'Error!! Please select gas from the list')
                  return
                
            except ValueError:
                self.message = messagebox.showerror('User Input Error', 'Error!! Please enter pressure (max = 160 psia)')
                return
            
            self.entry_pressure_1.delete(0, tk.END)
            self.entry_gas_1.delete(0, tk.END)
            
            self.top_New_pressure_1.destroy()

    def New_pressure_2(self,master):
        
        global entry_pressure_2
        global entry_gas_2
        
        self.top_New_pressure_2 = tk.Toplevel(master)    
        self.top_New_pressure_2.title('MFC B Configuration')
        self.top_New_pressure_2.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')
        self.top_New_pressure_2.geometry('310x150')
        
        self.set_lbl1 = tk.Label(self.top_New_pressure_2, text='Mass Flowrate B', padx=5, pady=5)
        self.set_lbl1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='W')
        
        self.set_lbl2 = tk.Label(self.top_New_pressure_2, text='Pressure:', padx=5, pady=5)
        self.set_lbl2.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky='W')
        self.entry_pressure_2 = tk.Entry(self.top_New_pressure_2, textvariable=pressure_2_var, width=10, borderwidth=3)
        self.entry_pressure_2.grid(row=1, column=1)
            
        self.set_lbl3 = tk.Label(self.top_New_pressure_2, text='Gas:', padx=5, pady=5)
        self.set_lbl3.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky='W')
        self.entry_gas_2 = tk.Entry(self.top_New_pressure_2, textvariable=gas_2_var, width=10, borderwidth=3)
        self.entry_gas_2.grid(row=2, column=1)
    
        self.set_button = tk.Button(self.top_New_pressure_2, text='See Gas List', command=gas_list_module, width=10)
        self.set_button.grid(row=2,column=3, stick='E')
    
    
        self.label = tk.Label(self.top_New_pressure_2, text='', padx=40).grid(row=1, column=2)
        self.set_button = tk.Button(self.top_New_pressure_2, text='Enter', command=self.Set_pressure_2, width=10)
        self.set_button.grid(row=3,column=3, stick='E')
    
    def Set_pressure_2(self):
        global pressure_2
        global gas_2
        
        if self.entry_pressure_2.get() == '' or self.entry_gas_2.get()== '':
            self.message = messagebox.showerror('User Input Error', 'Error!! Please enter value for both PRESSURE and TYPE OF GAS')
            return
        else:
            try:
            
                if float(self.entry_pressure_2.get()) > 160:
                    self.message = messagebox.showerror('User Input Error', 'Error!! Please enter pressure (max = 160 psia)')
                    return
                else:
                    pressure_2 = self.entry_pressure_2.get()
                    pressure_2 = float(pressure_2)
                    flow_controller2._set_control_point("pressure")
                    flow_controller2.set_pressure(pressure_2)
                    pass
                
                if self.entry_gas_2.get() in Gas_list:
                    gas_2 = self.entry_gas_2.get()
                    flow_controller2.set_gas(gas_2)
                    pass
                else:
                  self.message = messagebox.showerror('User Input Error', 'Error!! Please select gas from the list')
                  return
                
            except ValueError:
                self.message = messagebox.showerror('User Input Error', 'Error!! Please enter pressure (max = 160 psia)')
                return
            
            self.entry_pressure_2.delete(0, tk.END)
            self.entry_gas_2.delete(0, tk.END)
            
            self.top_New_pressure_2.destroy()


#==========================================================================================================================================

#====================================================  CLOSE WINDOWS  ===================================================================
    
    def removewindow_1(self):
        self.top_streaming_1.destroy()
        self.top_history_1.destroy()
        self.file_1.close()
        self.top_streaming_1 = None
         
    def removewindow_2(self):
        self.top_streaming_2.destroy()
        self.top_history_2.destroy()
        self.file_1.close()
        self.top_streaming_2 = None

    def on_closing(self):
        if self.top_streaming_1 is not None or self.top_streaming_2 is not None:
            self.message = messagebox.showerror('Warning', 'Please close the running streams before exiting')
        else:
           if messagebox.askyesno("Quit", "Do you want to quit?"):  
               root.destroy()

#==========================================================================================================================================


root = tk.Tk()
root.title('Alicat Mass Flowrate Controller Program')
root.iconbitmap('C:/Users/SyaminAimanSalleh/anaconda3/envs/AlicatMFC/ANU.ico')


flow_rate_1_var= tk.IntVar()
pressure_1_var = tk.IntVar()
gas_1_var = tk.StringVar()


flow_rate_2_var = tk.IntVar()
pressure_2_var = tk.IntVar()
gas_2_var = tk.StringVar()

interval_1_var=tk.IntVar()
interval_2_var=tk.IntVar()

flow_rate_1 = 0
pressure_1 = 0
gas_1 = 'Air'

flow_rate_2 = 0
pressure_2 = 0
gas_2 = 'CH4'

interval_1 = 1000
interval_2 = 1000


Gas_list = ["Air","Ar","CH4","CO","CO2","C2H6","H2","He","N2","N20","Ne","O2","C3H8","nC4H10","C2H2","C2H4","iC4H10","Kr","Xe","SF6",
            "C-25","C-10","C-8","C-2","C-75","He-25","He-75","A1025","Star29","P-5","NO","NF3","NH3","Cl2","H2S","SO2","C3H6","1Buten",
            "cButen","iButen","COS","DME","SiH4","R-11","R-115","R-116","R-124","R-125","R-134A","R-14","R-142b","R-143a","R-152a",
            "R-22","R-23","R-32","R-318","R-404A","R-407C","R-410A","R-507A","C-15","C-20","C-50","He-50","He-90","Bio5M","Bio10M",
            "Bio15M","Bio20M","Bio25M","Bio30M","Bio35M","Bio40M","Bio45M","Bio50M","Bio55M","Bio60M","Bio65M","Bio70M","Bio75M","Bio80M",
            "Bio85M","Bio90M","Bio95M","EAN-32","EAN","EAN-40","HeOx20","HeOx21","HeOx30","HeOx40","HeOx50","HeOx60","HeOx80","HeOx99",
            "EA-40","EA-60","EA-80","Metab","LG-4.5","LG-6","LG-7","LG-9","HeNe-9","LG-9.4","SynG-1","SynG-2","SynG-3","SynG-4","NatG-1",
            "NatG-2","NatG-3","CoalG","Endo","HHO","HD-5","HD-10","OCG-89","OCG-93","OCG-95","FG-1","FG-2","FG-3","FG-4","FG-5","FG-6","P-10","D-2"]


my_image1 = ImageTk.PhotoImage(Image.open("Gas_1.png"))
my_image2 = ImageTk.PhotoImage(Image.open("Gas_2.png"))
    
image_list = [my_image1, my_image2]

user_decision_options = ["Poll", "Stream", "Set Flowrate", "Set Pressure"]

r = tk.IntVar()

menu_select_1 = tk.StringVar()
menu_select_1.set(user_decision_options[0])
menu_select_2 = tk.StringVar()
menu_select_2.set(user_decision_options[0])

Main = Main_app(root)

root.mainloop()