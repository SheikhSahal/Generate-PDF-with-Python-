from fpdf import FPDF

fpdf = FPDF()
fpdf.add_page()
fpdf.set_font("Arial",size=70)
fpdf.text(50,50,txt="hellow world")
fpdf.image("1.png",50,50,w=120)
fpdf.set_font("Arial",size=10)
fpdf.text(60,90,txt="hellow world")
fpdf.output("output.pdf")