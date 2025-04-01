from fpdf import FPDF

# setting  the page
pdf=FPDF(orientation="P",unit="mm",format="A4")

# generating exercise book
for i in range(1, 31):
    pdf.add_page()

    for y in range(20,298,10):
        pdf.line(2,y,209,y)
        pdf.line(15, 20, 15, 297)



pdf.output("output1.pdf")