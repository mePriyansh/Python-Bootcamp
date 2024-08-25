import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Get the list of file paths
filepaths = glob.glob("Project 5- Excel to pdf invoice\\Invoice\\*.xlsx")

for filepath in filepaths:
    df=pd.read_excel(filepath,sheet_name='Sheet 1')

    pdf=FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    filename=Path(filepath).stem
    invoice_nr,date=filename.split('-')
    #date=filename.split('-')[1]
    
    pdf.set_font(family="Times",size=16,style='B')
    pdf.cell( w=50,h=8,txt=f"Invoice nr. {invoice_nr}")

    pdf.set_font(family="Times",size=16,style='B')
    pdf.cell( w=50,h=8,txt=f"Date {invoice_nr}")
    
    
    pdf.output(f"Project 5- Excel to pdf invoice\\PDFs\\{filename}.pdf")
