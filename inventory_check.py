from utils_func.user_input_utils import process_excel_data

def inventory_check():
    process_excel_data(
        prompt_title="Inventory Check Input",
        prompt_message="Please paste the data:\n(Use Tab to separate columns)",
        template_path=r"C:\Template\盘点.xlsx",
        output_prefix="inventory",
        column_mapping={1: 0, 2: 1},  # Column A <- 2nd input column, Column B <- 1st input column
        required_columns=2
    )


'''
if __name__ == "__main__":
    inventory_check()
'''