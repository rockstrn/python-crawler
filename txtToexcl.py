import xlwt
import codecs
from Openweb import getInfo
input_txt = '11.22.txt'
output_excel = '11.22.xls'
sheetName = 'Sheet1'
start_row = 1
start_col = 0

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet(sheetName)

ws.write(0, 0, 'task_id')
ws.write(0, 1, 'meeting_id')
ws.write(0, 2, 'meeting_code')
ws.write(0, 3, 'reason1')
ws.write(0, 4, 'reason2')
ws.write(0, 5, 'filestate')
ws.write(0, 6, 'recordState')

reason1 = ''

f = open(input_txt, encoding='utf-8')

row_excel = start_row
for line in f:
    # print(len(line))
    line = line.strip(" ,\n:：")
    if len(line) <= 1 or line[0] == '[':
        continue
    line = line.split(":")

    # print(line)
    print(len(line))

    col_excel = start_col
    len_line = len(line)
    if len_line > 1 and len(line[1]) > 1:
        # row_excel += 1
        print(line)
        line[0] = line[0].strip(" ,\n:：")
        line[1] = line[1].strip(" ,\n:：")
        print(line)
        if line[0] == "原因":
            ws.write(row_excel-1, 4, line[1])
        elif line[0] == "meeting_id":
            # ws.write(row_excel, 1, line[1])
            continue
        elif line[0] == "启动耗时大于8s的任务详情":
            reason1 = line[0].strip(' ')
            ws.write(row_excel, 0, line[1])
            # meetingId, meetingCode, recordState, filestate = getInfo(line[1])
            # ws.write(row_excel, 1, meetingId)
            # ws.write(row_excel, 2, meetingCode)
            ws.write(row_excel, 3, reason1)
            # ws.write(row_excel, 5, filestate)
            # ws.write(row_excel, 6, recordState)
            row_excel += 1
        elif line[0] == "task_id":
            ws.write(row_excel, 0, line[1])
            # meetingId, meetingCode, recordState, filestate = getInfo(line[1])
            # ws.write(row_excel, 1, meetingId)
            # ws.write(row_excel, 2, meetingCode)
            # ws.write(row_excel, 5, filestate)
            # ws.write(row_excel, 6, recordState)
            ws.write(row_excel, 3, reason1)
            row_excel += 1
        else :
            ws.write(row_excel, 0, line[0])
            # meetingId, meetingCode, recordState, filestate = getInfo(line[0])
            # ws.write(row_excel, 1, meetingId)
            # ws.write(row_excel, 2, meetingCode)
            # ws.write(row_excel, 5, filestate)
            # ws.write(row_excel, 6, recordState)
            ws.write(row_excel, 4, line[1])
            ws.write(row_excel, 3, reason1)
            row_excel += 1
        wb.save(output_excel)
    else:
        line[0] = line[0].strip(" ,\n:：")
        print(line)
        if ( line[0][0] >= '0' and line[0][0] <= '9' ) or (line[0][0] >= 'a' and line[0][0] <= 'z') :
            # ws.write(row_excel, col_excel, line[0])
            # meetingId, meetingCode, recordState, filestate = getInfo(line[0])
            # ws.write(row_excel, 1, meetingId)
            # ws.write(row_excel, 2, meetingCode)
            # ws.write(row_excel, 5, filestate)
            # ws.write(row_excel, 6, recordState)
            ws.write(row_excel, 0, line[0])
            ws.write(row_excel, 3, reason1)
            row_excel += 1
        else :
            reason1 = line[0]
        wb.save(output_excel)

wb.save(output_excel)
f.close
