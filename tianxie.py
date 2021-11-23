import xlrd
import xlwt
from Openweb import getInfo
from xlutils.copy import copy

input_file_name = '11.22.xls'


def read_excel(input_file_name):
    """
    从xls文件中读取数据
    """
    workbook = xlrd.open_workbook(input_file_name)
    new = copy(workbook)
    news = new.get_sheet(0)
    print(workbook)
    # 可以使用workbook对象的sheet_names()方法获取到excel文件中哪些表有数据
    print(workbook.sheet_names())
    # 可以通过sheet_by_index()方法或sheet_by_name()方法获取到一张表，返回一个对象
    # table = workbook.sheet_by_index(0)
    # print(table)
    table = workbook.sheet_by_name('Sheet1')
    print(table)
    # 通过nrows和ncols获取到表格中数据的行数和列数
    rows = table.nrows-1
    cols = table.ncols
    # 也可以根据单元格获取每一个单元格的数据
    for row in range(rows):
        data = table.cell(row+1, 0).value
        meetingId, meetingCode, recordState, filestate = getInfo(data)
        news.write(row+1, 1, meetingId)
        news.write(row+1, 2, meetingCode)
        news.write(row+1, 5, filestate)
        news.write(row+1, 6, recordState)
        # news.write(row+1, 3, reason1)
        new.save("11.22.xls")


read_excel(input_file_name)