import pyodbc 
from fpdf import FPDF

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MSAHALQASIM;'
                      'Database=Demo;'
                      'Trusted_Connection=yes;'
                      'uid=sa;pwd=Optiplex@242244')

cursor = conn.cursor()
cursor.execute('SELECT * FROM EMP')

for i in cursor:
    print(i.Name)
    fpdf = FPDF()
    # add page
    fpdf.add_page()
    # Insert image
    fpdf.image("1.png",50,50,w=120)
    # Set font
    fpdf.set_font("Arial",size=10)
    # Add text
    fpdf.text(60,90,txt=i.Name)
    fpdf.output(i.Name+".pdf")


