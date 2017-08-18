from urllib.request import urlopen
import requests
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = 'http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt'
COMMENT_CHARS = '#:'
r = requests.get(URL)
text = r.text#生成文本
data = []

with open('C:/Users/C.U.Weir/Documents/GitHub/Draw_A_Nice_Picture/test.txt', 'w') as x:
    x.write(text)
try:
    f = open('C:/Users/C.U.Weir/Documents/GitHub/Draw_A_Nice_Picture/test.txt', 'r')
    for line in f.readlines():  # readlines():讀取並返回一個包含行的列表
        if not line.isspace() and not line[0] in COMMENT_CHARS:  # isspace():檢測字符串是否只由空格產生，是返回True
            data.append([str(n) for n in line.split()])  # split():對字符串進行切片
finally:
    if f:
        f.close()

drawing = Drawing(400, 200)


pred = [float(row[2]) for row in data]
high = [float(row[3]) for row in data]
low = [float(row[4]) for row in data]
times = [float(row[0]) + float(row[1])/12.0 for row in data]

lp = LinePlot()
lp.x = 50#x和y值是圖表左下角的坐標
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times, pred)), list(zip(times, high)), list(zip(times, low))]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize=14, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')

with open('C:/Users/C.U.Weir/Documents/GitHub/Draw_A_Nice_Picture/test.txt', 'w') as x:
    x.truncate()