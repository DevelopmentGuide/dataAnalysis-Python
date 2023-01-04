import xlwt
from xlwt import Workbook
from datetime import datetime

now = datetime.now()

time = now.strftime("%H:%M:%S")
today = now.strftime("%D")
footerMsg = "Sent at: " + time + '\n' + "Dated: " + today

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

# style = xlwt.easyxf('none;')
# sheet1.write(1, 0, footerMsg, style)

sheet1.write(0, 0, footerMsg)
sheet1.write(1, 0, footerMsg)
sheet1.write(2, 0, footerMsg)
sheet1.write(3, 0, footerMsg)
sheet1.write(4, 0, footerMsg)

wb.save('example.xls')
print("done!")
