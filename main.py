from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

pdf = FPDF(orientation="P", unit="mm", format="A3")
pdf.set_auto_page_break(auto=False, margin=0)

filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A3")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDF/{filename}.pdf")





