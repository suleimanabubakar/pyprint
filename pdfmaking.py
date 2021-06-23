import pdfkit

def makePdf():
    options = {
    'margin-top': '0',
    'margin-left': '0',
        }
    pdfkit.from_url('http://127.0.0.1:8000/orderprintauto/30', 'D:/pds/px31.pdf', options=options)
