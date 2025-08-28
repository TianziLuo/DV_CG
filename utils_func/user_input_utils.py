import openpyxl
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
from utils_func.excel_utils import save_as_xls  # Your existing XLS conversion utility
import os

def process_excel_data(
    prompt_title: str,
    prompt_message: str,
    template_path: str,
    output_prefix: str,
    column_mapping: dict,
    required_columns: int,
    output_dir: str = r"C:\Users\monica\Downloads"
):
    """
    Generic Excel data processing function.

    Parameters:
    - prompt_title: Title of the popup input dialog
    - prompt_message: Prompt message for user input
    - template_path: Path to the Excel template file (.xlsx)
    - output_prefix: Prefix for the saved file name
    - column_mapping: Dict mapping target Excel columns to source data indexes (starting from 0), e.g. {1: 13, 2: 1}
    - required_columns: Minimum number of columns required in the pasted data
    - output_dir: Output folder path for saving the file
    """
    # Get multiline user input from popup
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring(prompt_title, prompt_message)

    if not user_input:
        messagebox.showerror("Error", "No input detected.")
        return

    # Parse tab-separated input data
    data = []
    for line in user_input.strip().splitlines():
        row = line.strip().split("\t")
        if len(row) >= required_columns:
            mapped_row = []
            for col_index in column_mapping.values():
                if isinstance(col_index, int):
                    try:
                        mapped_row.append(row[col_index])
                    except IndexError:
                        mapped_row.append("")  # 
                else:
                    # input
                    mapped_row.append(col_index)
            data.append(mapped_row)

    if not data:
        messagebox.showerror("Error", "Parsed data is empty or invalid.")
        return

    # Load Excel template
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active

    # Write data to worksheet starting from row 2
    start_row = 2
    for i, row_data in enumerate(data, start=start_row):
        for target_col, value in enumerate(row_data, start=1):
            ws.cell(row=i, column=target_col).value = value

    # Save as .xlsx
    today_str = datetime.today().strftime("%Y%m%d")
    file_name_xlsx = f"{output_prefix}_{today_str}.xlsx"
    output_path_xlsx = os.path.join(output_dir, file_name_xlsx)
    wb.save(output_path_xlsx)

    # Convert .xlsx to .xls
    file_name_xls = f"{output_prefix}_{today_str}.xls"
    output_path_xls = os.path.join(output_dir, file_name_xls)
    save_as_xls(output_path_xlsx, output_path_xls)

    # Delete temporary .xlsx file
    try:
        os.remove(output_path_xlsx)
    except Exception as e:
        messagebox.showwarning("Warning", f"Failed to delete xlsx file: {e}")

    # Notify success
    messagebox.showinfo("Success", f"✅ Data has been successfully saved as:\n{output_path_xls}")
