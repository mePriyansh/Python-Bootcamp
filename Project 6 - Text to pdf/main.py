from fpdf import FPDF
from pathlib import Path
import glob

filepath=glob.glob("Project 6 - Text to pdf\\Text Files\\*.txt")

pdf=FPDF(orientation='P', unit='mm', format='A4')

for file in filepath:

    pdf.add_page()
    filename=Path(file).stem
    name=filename.title()
    pdf.set_font(family="Times",size=16,style='B')
    pdf.cell( w=50,h=8,txt=name,ln=1)

pdf.output(f"Project 6 - Text to pdf\\PDFs\\output.pdf")



