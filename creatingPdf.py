import fpdf
from fpdf import FPDF
import pandas as pd
#reading csv file
df=pd.read_csv("topics.csv")

# generating pdf file
pdf=FPDF(orientation="P", unit="mm",format="A4")

# iterating over the rows
for index, row in df.iterrows():

    pdf.add_page()
    pdf.set_font(family="Times",size=24, style="B")
    pdf.cell(w=0,h=12, txt=row["Topic"],ln=1,border=0)
    pdf.set_text_color(100,100,100)
    pdf.line(10,21,200,21)

pdf.output("output.pdf")