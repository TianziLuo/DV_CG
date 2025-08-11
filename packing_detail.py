from utils_func.user_input_utils import process_excel_data

def packing_detail():
    process_excel_data(
        prompt_title="Packing Detail Input",
        prompt_message="Please paste the data:\n(Use Tab to separate columns)",
        template_path=r"C:\Template\Packing_details.xlsx",
        output_prefix="packing",
        column_mapping={1: 13, 2: 1, 3: 3},  # Column A <- 14th, B <- 2nd, C <- 4th
        required_columns=14
    )