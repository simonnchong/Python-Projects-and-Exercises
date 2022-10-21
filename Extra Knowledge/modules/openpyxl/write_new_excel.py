from openpyxl import Workbook
#creates a new workbook
wb = Workbook()
#Gets the first active worksheet
ws = wb.active
#creating new worksheets by using the create_sheet method

ws1 = wb.create_sheet("sheet1", 0) #inserts at first position
ws2 = wb.create_sheet("sheet2") #inserts at last position
ws3 = wb.create_sheet("sheet3", -1) #inserts at penultimate position
ws4 = wb.create_sheet() 
ws5 = wb.create_sheet() 

#Renaming the sheet
ws5.title = "Example"

#save the workbook
wb.save(filename = "example.xlsx")