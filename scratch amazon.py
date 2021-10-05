import requests
from lxml import etree
import re
import xlwt

from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取excel
# import matplotlib.pylab as plt
from xlrd import book

headers = {
    'User-Agent': Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36,
    'Cookie': 'x-wl-uid=1DVw4k4T/jAduWIfwW2jvf029Ha4Bgv/AJGjP/yRfJTdq26dr7oDdeEBdb6zOPUl0ByfsaKJ3GUY=; session-id-time=2082729601l; session-id=457-7649276-4174543; csm-hit=tb:DAHATSQRZZBWHWD4ZXYP+s-T61YJHRDEC6Y6S2VMTVZ|1573355007668&t:1573355007668&adb:adblk_no; ubid-acbcn=459-2457809-1906210; session-token="4sZGQQPKw9CJUOzJFLsTdS3FtlpqIyp0hyvhXL6RMOchbDf7p7YLDEL90YFps2Hl80fBT6uPmzQ00meCLYxsrjuoabX3+kz7OB+CLw8GaAYZB8J9oBBcJLBUsGs6LLm/EHQht5Tm0IpOKR0hz0GGtATgcpJXDfRoEdvNol+CUc3mXOMA5KmEfFWstdV+KwyzSGrGW+DdrAftisgZMl2stffIdhcOLh53B4tJwsR5awKqPrOqZF8uJg=="; lc-acbcn=zh_CN; i18n-prefs=CNY'
} #添加headers模拟浏览器防止被发现
