# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:11:07 2021

@author: HgCNO2
"""
# Import Modules
from tkinter import Tk, Button, Label
from tkcalendar import Calendar
from datetime import datetime
from re import search

def date_pycker(cal_name='Date Picker', size='500x600'):
    
    if not search(r'\d*x\d*', size):
        raise ValueError('The size dimensons need to match {dimension}x{dimension} (eg: 500x600).')
    
    # Define function to get the date from the calendar
    def sel_date():
        global _date
        _date = cal.selection_get()
        window.destroy()
    
    # Create Window
    window = Tk()
    window.title(cal_name)
    window.geometry(size)
    
    # Label Calendar
    Label(window,
          text=cal_name,
          font='bold').pack(expand=True)
    
    # Create Calendar
    cal = Calendar(window, selectMode='day',
                   year=datetime.today().year,
                   month=datetime.today().month,
                   day=datetime.today().day,
                   date_pattern='mm/dd/y',
                   firstweekday='sunday')
    cal.pack(pady=20, padx=20, fill='both', expand=True)
    
    Button(window,
           text='Select Date',
           command=sel_date).pack(pady=20, expand=True)
    
    window.mainloop()
    return _date

if __name__ == '__main__':
    start = date_pycker('Report Start Date')
    end = date_pycker('Report End Date', 'try for error')