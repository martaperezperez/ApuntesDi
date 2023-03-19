from reportlab.graphics.shapes import Image,Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

op =[]

img = Image(250,0,400,400,"C:\\Users\Interno\Pictures\Screenshots\DI.png")

draw = Drawing(30,30)
draw.add(img)
draw.translate(0,400)

op.append(draw)

draw2 = Drawing(30,30)
draw2.add(img)
draw2.rotate(30)
draw2.scale(0.5,0.5)
op.append(draw2)

draw3 = Drawing(A4[0],A4[1])
for img in op:
    draw3.add(img)

renderPDF.drawToFile(draw3,"Draw(Marta).pdf")
