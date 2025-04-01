import fpdf
from fpdf import FPDF
import pandas as pd
#reading csv file
df=pd.read_csv("topics.csv")

# generating pdf file
pdf=FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False)

# iterating over the rows
for index, row in df.iterrows():

    pdf.add_page()
    # set a header
    pdf.set_font(family="Times",size=24, style="B")
    pdf.cell(w=0,h=12, txt=row["Topic"],ln=1,border=0,align="L")
    pdf.set_text_color(100,100,100)
    pdf.line(10,21,200,21)


    # adding lines
    for y in range(20,298,10):
        pdf.line(10,y,200,y)

        # set a footer
    pdf.ln(265)
    pdf.set_font(family="Times", size=12, style="I")
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, border=0, align="R")
    pdf.set_text_color(180, 180, 180)



    # adding pages
    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(275)
        pdf.set_font(family="Times", size=12, style="I")
        pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, border=0, align="R")
        pdf.set_text_color(180, 180, 180)
        # adding lines
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)


pdf.output("output.pdf")