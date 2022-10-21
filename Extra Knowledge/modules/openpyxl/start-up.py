from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = 42

# Rows can also be appended
ws.append([10, 2, 3, 4, 6, 7, 4, 5])

# Python types will automatically be converted
import datetime
ws['A3'] = datetime.datetime.now()

import random
for _ in range(20):
    ws.append([random.randint(100, 1000)])

# Save the file
wb.save("sample.xlsx")