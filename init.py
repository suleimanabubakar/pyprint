import win32print
import win32api 
GHOSTSCRIPT_PATH = "C:\\Users\lewa\Desktop\py print\ghostscript\bin\gswin32.exe"
GSPRINT_PATH = "C:\\Users\lewa\Desktop\py print\gsprint\gsprint.exe"

# printername = "Kyocera KM-2560 KX (Copy 1)"
# currentprinter = win32print.SetDefaultPrinter(printername)
defaultprinter = win32print.GetDefaultPrinter()

pdftest = "C:\\Users\Lewa\Dev\pyprint\pdftest.pdf"



# print(defaultprinter)

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+defaultprinter+'" "'+pdftest+'"', '.', 0)
