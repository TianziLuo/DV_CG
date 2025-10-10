import pandas as pd
import re
import xlwt
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def text_errorcode():
    # === 1. User input text ===
    root = tk.Tk()
    root.withdraw()  # hide main window
    text = simpledialog.askstring("Stock Update", "Enter shortage text:")
    if not text:
        messagebox.showinfo("Info", "No text entered. Exit.")
        return

    # === 2. Extract SKU and quantity ===
    pattern = r'产品“(.*?)“的库存不足，可用(\d+)个'
    stock_dict = {k: int(v) for k, v in re.findall(pattern, text)}

    if not stock_dict:
        messagebox.showinfo("Info", "No valid SKU found. Exit.")
        return

    # === 3. Choose Excel file ===
    file_path = filedialog.askopenfilename(title="Select Excel file", 
                                           filetypes=[("Excel files", "*.xls;*.xlsx")])
    if not file_path:
        messagebox.showinfo("Info", "No file selected. Exit.")
        return

    # === 4. Read Excel ===
    try:
        df = pd.read_excel(file_path, engine='xlrd')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read Excel:\n{e}")
        return

    # === 5. Find columns ===
    sku_col = None
    qty_col = None
    for col in df.columns:
        if 'sku' in str(col).lower() or '产品' in str(col):
            sku_col = col
        if '数量' in str(col):
            qty_col = col
    if not sku_col or not qty_col:
        messagebox.showerror("Error", "SKU or Quantity column not found.")
        return

    # === 6. Update quantities ===
    for i in range(len(df)):
        sku = str(df.at[i, sku_col]).strip()
        if sku in stock_dict:
            df.at[i, qty_col] = stock_dict[sku]

    # === 7. Remove zero quantities ===
    df = df[df[qty_col] != 0]

    # Fill empty cells
    df = df.fillna("")

    # === 8. Save as .xls ===
    new_path = file_path.replace(".xls", "_updated.xls").replace(".xlsx", "_updated.xls")
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Sheet1")

    # Write header
    for col_idx, col_name in enumerate(df.columns):
        ws.write(0, col_idx, col_name)

    # Write data
    for row_idx, row in enumerate(df.itertuples(index=False), start=1):
        for col_idx, value in enumerate(row):
            ws.write(row_idx, col_idx, str(value))

    wb.save(new_path)
    messagebox.showinfo("Done", f"Stock updated.\nSaved as:\n{new_path}")

'''
if __name__ == "__main__":
    update_stock_from_text()
'''