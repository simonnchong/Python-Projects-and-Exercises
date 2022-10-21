import openpyxl

wb = openpyxl.load_workbook("example.xlsx")

#getting all sheets names
print(wb.sheetnames)

#getting a particular sheet
selected_sheet = wb["sheet2"]
print(selected_sheet)

#getting sheet title
print(selected_sheet.title)

#Getting the active sheet
sheetactive = wb.active
print(sheetactive)