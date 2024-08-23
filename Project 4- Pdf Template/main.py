from fpdf import FPDF
import pandas as pd

df=pd.read_csv(r"Project 4- Pdf Template\topics.csv")

pdf=FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Times", size = 24, style='B')
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],
            ln=1,align='L')
    #for line throughot page
    for y in range(20,278,10):
        pdf.line(10,y,200,y)
    #pdf.line(10,21,200,21)

    pdf.ln(260)
    pdf.set_font("Times", size = 8, style='I')
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row['Topic'],align="R",)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font("Times", size = 8, style='I')
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row['Topic'],align="R",)
            #for line throughot page
        for y in range(20,278,10):
            pdf.line(10,y,200,y)
pdf.output(r"Project 4- Pdf Template\output_line.pdf")