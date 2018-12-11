# coding:utf-8

# 可以在原来的文件上直接修改
from datetime import date

from xlutils.copy import copy
import os
import xlrd
import xlwt

rb = xlrd.open_workbook(os.path.abspath('user.xls'))
# 获取sheet名称
print rb.sheet_names()
# 通过索引获得sheet，也可通过name
sheet0 = rb.sheet_by_index(0)
# 检查某个sheet是否导入完毕
sl = rb.sheet_loaded(0)
print sl
# 获取指定单元格的值
print sheet0.cell(0, 0).value.encode('utf-8')
# ctype类型 : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print sheet0.cell(0, 0).ctype
# 获取表格中的日期 ，先判断是否为日期，不然会报错
if sheet0.cell(0, 3).ctype == 3:
    date_value = xlrd.xldate_as_tuple(sheet0.cell_value(0, 3), rb.datemode)
    print type(date_value)
    print u'日期=>', date(*date_value[:3])
    print u'格式化日期=>:', date(*date_value[:3]).strftime('%Y/%m/%d')

    dates = xlrd.xldate_as_datetime(sheet0.cell_value(0, 3), rb.datemode)
    print type(dates), dates.date()
# 获取一行的值
print sheet0.row_values(0)
# 获取一列的值
print sheet0.col_values(0)
# 有效行数
print sheet0.nrows
print sheet0.ncols
# 第一行
print sheet0.row(0)
# 第一列 #返回由该列中所有的单元格对象组成的列表
print sheet0.col(0)
# 返回由该列中所有的单元格对象组成的列表
print sheet0.col_slice(0)
# 返回由该列中所有单元格的数据组成的列表
print sheet0.col_values(0)
# 返回由该列中所有单元格的数据类型组成的列表
print sheet0.col_types(0)

# 获取合并单元格的内容
# 合并只有的第一个单元格可以获取到值，其他为空
print sheet0.cell(1, 3).value
print sheet0.cell(2, 3).value  # 值为空
print sheet0.cell(3, 3).value
print u'1行', sheet0.row_values(0)
print u'2行', sheet0.row_values(1)
"""可以利用merged_cells方法进行处理，处理的方法是只能获取合并单元格的第一个cell的行列索引，才能读到值，读错了就是空值。即合并行单元格读取
行的第一个索引，合并列单元格读取列的第一个索引。这里，需要在读取文件的时候添加个参数，将formatting_info参数设置为True，默认是False，否
则可能调用merged_cells方法获取到的是空值。

merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),其中[row,row_range)包括row,不包括row_range,col也是一样，下标从0开始。
"""
workbook = xlrd.open_workbook(os.path.abspath('user.xls'), formatting_info=True)
sheet2 = workbook.sheet_by_name('Sheet1')
print sheet2.merged_cells  # [(0, 2, 4, 6), (3, 5, 4, 5)] 取1，3位（即低位的索引值）
# 获取合并单元格的值
merg = []
for lrow, lrow_range, rcol, rcol_range in sheet2.merged_cells:
    merg.append([lrow, rcol])
    print sheet2.cell_value(lrow, rcol)

print sheet2.cell_value(merg[0][0], merg[0][1])
print sheet2.cell_value(merg[1][0], merg[1][1])

