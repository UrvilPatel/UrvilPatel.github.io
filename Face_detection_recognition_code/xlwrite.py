import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlutils.copy import copy
from pathlib import Path

def make_sheet(filename, sheet,num, name, present):
    #get the location of the excel sheet
    FileLoc = Path('C:/Users/Admin/Desktop/attedance_sheet/'+filename+str(datetime.now().date())+'.xls');

    if FileLoc.is_file():
        # exists file
        #go to the original source file by using open_workbook
        open_file = open_workbook('C:/Users/Admin/Desktop/attedance_sheet/'+filename+str(datetime.now().date())+'.xls');

        #copy into the new workbook
        new_book = copy(open_file);

        #get the sheet information and also edit the sheet
        f_sheet = new_book.get_sheet(0)

    else:
        #create a blank spreadsheet file or workbook
        new_book = xlwt.Workbook()

        #create a sheet within the file
        #we can add sheets to our workbook by using add_sheet
        f_sheet = new_book.add_sheet(sheet)

    font_style = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')
    date_style = xlwt.easyxf(num_format_str='D-MMM-YY')

    #add date in the particular cells in the sheet
    f_sheet.write(0,0,datetime.now().date(),date_style);

    column1_name = 'Name'
    column2_name = 'Present'

    f_sheet.write(1,0,column1_name,font_style);
    f_sheet.write(1, 1, column2_name,font_style);

    f_sheet.write(num+1,0,name);
    f_sheet.write(num+1, 1, present);

    fullname=filename+str(datetime.now().date())+'.xls';

    #save the excel sheet with current date
    new_book.save('C:/Users/Admin/Desktop/attedance_sheet/'+fullname)
    return fullname;