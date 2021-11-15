import openpyxl
from openpyxl import Workbook
wb = openpyxl.load_workbook('F:F:\程序学习\Python/1.xlsx')
ws = wb['2016']
ws.cell(30,15,'我是武玟睿')
wb.save('F:\程序学习\Python/1.xlsx')
input()