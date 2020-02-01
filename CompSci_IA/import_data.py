import csv
import xlrd #importing library
import pprint as p #importing library
csvfile = open('/users/2020jkapasi/documents/book1.xlsx', "r")
reader = csv.DictReader(csvfile)

def get_data(file, sheet): #defining function to take in the file and the excel sheet
    book = xlrd.open_workbook(file) #function from xlrd
    sheet = book.sheet_by_name(sheet) #opening the sheet, and then storing it as sheet
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]#for the rows and columns within the sheeet, it is getting the value at every single row and column
    return data #return data

sheet = 'Sheet1' #name of sheet
file = r'/users/2020jkapasi/documents/book1.xlsx' #file path to get to sheet
p.pprint(get_data(file, sheet)) #print it
