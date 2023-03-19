import os.path

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer

from reportlab.lib.styles import  getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import  A4
from reportlab.lib import colors

class MineParagraphStyle(ParagraphStyle):
    def __int__(self):
        super().__int__(self,fontSize=18,
                        font= "Helvetica",
                        textColor= "Blue")

style_sheet = getSampleStyleSheet()

op = []

header = style_sheet["Heading4"]
header.pageBreakBefore = 1
header.keepWithNext = 0
header.backColor = colors.paleturquoise

paragarph = Paragraph("Docs header", header)
op.append(paragarph)

chainText = """Texto de contido de parafo que imos repetir unhas cantas veces. """
sampleText = style_sheet['BodyText']
paragarph2= Paragraph(chainText * 500, sampleText)
op.append(paragarph2)
op.append(Spacer(0,20))

image_file = "C:\\Users\Interno\Pictures\Screenshots\DI.png"
image = Image(os.path.relpath(image_file))
op.append(image)

paragarph3 = Paragraph(chainText * 5, MineParagraphStyle())
op.append()

doc = SimpleDocTemplate("Platypus.pdf", pagesize = A4, showBoundary=1)
doc.build(op)
