from reportlab.pdfgen import canvas

aux = canvas.Canvas ("documento.pdf")

aux.drawString(0,0, "Posicion orixe (X,Y) = (0,0)")
aux.drawImage(50,100, "Posicion (X,Y) = (50,100)")
aux.drawString(150, 500, "Posicion (X,Y) = (150,500)")

aux.drawImage ("C:\Users\Interno\Documents\foto.png",200,200,225,225)

aux.showPage()
aux.save()