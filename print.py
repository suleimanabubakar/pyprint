import win32print
import locale
import ghostscript


# pdf = render_to_pdf('print/slip.html', context)
# temp1 = tempfile.mktemp('.pdf')
# f1 = open(temp1, 'ab')
# f1.write(pdf)
# f1.close()
pdftest = "C:\\Users\Lewa\Dev\pyprint\pdftest.pdf"

args = [
        "-dPrinted", "-dBATCH", "-dNOSAFER", "-dNOPAUSE", "-dNOPROMPT"
        "-q",
        "-dNoCancel",
        "-dNumCopies#2",
        "-sDEVICE#mswinpr2",
        f'-sOutputFile#"%printer%{win32print.GetDefaultPrinter()}"',
        f'"{pdftest}"'
    ]

encoding = locale.getpreferredencoding()
args = [a.encode(encoding) for a in args]
ghostscript.Ghostscript(*args)