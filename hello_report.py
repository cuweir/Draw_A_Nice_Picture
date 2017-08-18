from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello, world!', textAnchor='middle')#x和y的坐標以及要顯示的文本，textAnchor字符應放在指定坐標処

d.add(s)

renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')