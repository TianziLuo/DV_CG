from ui import create_gui
from verify import verify_license
from tkinter import messagebox
import sys

if __name__ == "__main__":
    ok, msg = verify_license()
    if not ok:
        messagebox.showerror("License fail", msg)
        sys.exit()


    create_gui()
