import tkinter as tk
from tkinter import filedialog, messagebox
import os
import win32com.client
from pathlib import Path

def WFS():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Please select the Excel file to save as .xls",
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if not file_path:
        print("❌ No file selected. Operation cancelled.")
        messagebox.showwarning("No File Selected", "You did not select any file.")
        return

    downloads_dir = str(Path.home() / "Downloads")
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_xls_path = os.path.join(downloads_dir, f"Walmart_{base_name}.xls")

    print(f"Selected file: {file_path}")
    print(f"Saving as: {output_xls_path}")

    try:
        excel = win32com.client.Dispatch("Excel.Application")
        wb = excel.Workbooks.Open(file_path)
        wb.SaveAs(output_xls_path, FileFormat=56)  # 56 = .xls
        wb.Close(SaveChanges=False)
        excel.Quit()
    except Exception as e:
        print(f"❌ Error during save: {e}")
        messagebox.showerror("Save Failed", f"Error saving as .xls:\n{e}")
        return

    print(f"✅ Successfully saved to: {output_xls_path}")
    messagebox.showinfo("Success", f"✅The file was successfully saved as .xls:\n{output_xls_path}")

'''
if __name__ == "__main__":
    WFS()
'''