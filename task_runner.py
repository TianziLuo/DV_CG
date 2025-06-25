from datetime import datetime
from pathlib import Path
import warnings
import os
import traceback

from tasks_config import TASKS
from excel_utils import (
    verify_file_fresh,
    load_worksheet,
    find_last_data_row,
    copy_range_to_ws,
    save_as_xls,
)

# -------- CONFIG --------
DOWNLOADS = Path.home() / "Downloads"
max_life_age = 30  


def run_task(task: dict) -> bool:
    # Ignore warnings
    warnings.filterwarnings("ignore")  
    print(f"\n🚀 Starting task: {task['name']}")

    try:
        source_path = task["source_path"]
        sheet_name = task["sheet_name"]
        col_range = task["col_range"]
        template_path = task["template_path"]
        template_sheet = task.get("template_sheet", "Worksheet 1")
        output_prefix = task["output_prefix"]

        # Check if the source file is fresh
        verify_file_fresh(source_path, task.get("max_life_age", max_life_age))

        # Load source and template worksheets
        _, src_ws = load_worksheet(source_path, sheet_name)
        tpl_wb, tpl_ws = load_worksheet(template_path, template_sheet)

        # Find last row with data
        start_row = 3
        last_row = find_last_data_row(src_ws, col_range, start_row)
        row_range = (start_row, last_row + 1)

        # Map source columns to target columns
        col_map = [
            (src_col, idx + 1)
            for idx, src_col in enumerate(range(col_range[0], col_range[1] + 1))
        ]

        # Copy data to template worksheet
        copy_range_to_ws(src_ws, tpl_ws, row_range, col_map)

        # Prepare output file names
        today = datetime.now().strftime("%Y%m%d")
        base_name = f"{output_prefix}_{today}"
        xlsx_path = DOWNLOADS / f"{base_name}.xlsx"
        xls_path = DOWNLOADS / f"{base_name}.xls"

        # Ensure output folder exists
        DOWNLOADS.mkdir(parents=True, exist_ok=True)

        # Save .xlsx file
        if task.get("export_xlsx", True):
            tpl_wb.save(xlsx_path)
            print(f"✅ Saved .xlsx: {xlsx_path}")

        # Convert to .xls 
        if task.get("export_xls", True):
            save_as_xls(xlsx_path, xls_path)
            print(f"✅ Saved .xls: {xls_path}")

        # Delete the intermediate .xlsx 
        if task.get("delete_xlsx_after", True):
            try:
                os.remove(xlsx_path)
                print(f"🗑️ Deleted intermediate file: {xlsx_path.name}")
            except Exception as e:
                print(f"⚠️ Failed to delete .xlsx file: {e}")

        return True

    except Exception as e:
        print(f"❌ Task failed: {task['name']} - Error: {e}")
        traceback.print_exc()
        return False


def main():
    print("📦 Running batch Excel export tasks")
    for task in TASKS:
        run_task(task)
    print("\n✅ All tasks completed!")


# Uncomment to run directly
# if __name__ == "__main__":
#     main()
