import xlrd
import xlwt
from xlwt import Workbook

wb = xlrd.open_workbook('example.xls')
sheets = wb.sheets()

a = 0

row = sheets[0].row_values(0)
column = sheets[0].col_values(0)
cell = sheets[0].cell_value(a, 0)

# print(row)
# print(column)
# print(cell)

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

# style = xlwt.easyxf('none;')
# sheet1.write(1, 0, footerMsg, style)

# while cell != "":
#     a += 1
#     cell = sheets[0].cell_value(a, 0)
#     print(a)
#     print(cell)
#     if IndexError:
#         sheet1.write(a, 0, "aa")
#         wb.save('example.xls')
#         print("i8")
#         break

sheet1.write(5, 0, "aa")
wb.save('example.xls')

print("done!")
