from fpdf import FPDF

pdf=FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()
pdf.set_font("Times", size = 12, style='B')
pdf.cell(w=0,h=12,txt="Hello World",
         ln=1,align='L')
pdf.set_font("Times", size = 10)
pdf.cell(w=0,h=12,txt="Hi World",
         ln=1,align='L')
pdf.output('output.pdf')