# import win32print
# import win32api
import tempfile
import os   
filename = tempfile.mktemp (".txt")
open (filename, "w").write ("This is a test")
# win32api.ShellExecute (
#   0,
#   "printto",
#   filename,
#   '"%s"' % win32print.GetDefaultPrinter (),
#   ".",
#   0
# )
os.system('C:\\Users\Lewa\Dev\pyprint\pdftest.pdf')