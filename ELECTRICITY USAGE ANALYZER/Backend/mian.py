from csv2pdf import convert
import os
import time

def makingpdf():
    # ----------------- CONVERTING THE CSV FILE TO PDF FORMAT -------------------------
    pdffile = 'Output.pdf'
    location = 'C:/Users/sunil/OneDrive/Desktop/green computing web app/'
    pdfpath = os.path.join(location, pdffile)
    if os.path.exists(pdfpath):
        os.remove(pdfpath)

        time.sleep(2)

        convert('CalculatedData.csv', 'output.pdf')

    # ---------------------------------------------------------------------------------


if __name__ == '__main__':
    makingpdf()
