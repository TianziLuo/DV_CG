from utils_func.user_input_utils import process_excel_data

def WFS_out():
    process_excel_data(
        prompt_title="WFS Outbound",
        prompt_message="Please paste the data:\n(Use Tab to separate columns)",
        template_path=r"C:\Template\WFS\实际装箱出货.xlsx",
        output_prefix="WFS_OUT",
        column_mapping={
            1: 0,     # A列 <- 输入第14列 (0-based index)
            2: 1,      # B列 <- 输入第2列
            3: "DVP"   # C列 <- 默认填充 DVP
        },
        required_columns=2
    )

'''
if __name__ == "__main__":
    WFS_out()
'''