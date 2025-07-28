from pathlib import Path

TASKS = [
    # ----- Out -----
    {
        "name": "DV OUT",
        "source_path": Path(r"C:\Frank\2.1_易仓管理.xlsx"),
        "sheet_name": "小票_店小秘非BW",
        "col_range": (28, 31),             
        "template_path": Path(r"C:\Template\出库.xlsx"),
        "template_sheet": "Worksheet 1",
        "output_prefix": "出库_DV",
    },
    {
        "name": "RAW OUT",
        "source_path": Path(r"C:\Frank\2.1_易仓管理.xlsx"),
        "sheet_name": "RAW扫码出库",
        "col_range": (5, 8),                # E‑H
        "template_path": Path(r"C:\Template\出库.xlsx"),
        "template_sheet": "Worksheet 1",
        "output_prefix": "出库_RAW",
    },
    {
        "name": "FBA OUT",
        "source_path": Path(r"C:\Frank\3.1_FBA.xlsx"),
        "sheet_name": "FBA扣减库存",
        "col_range": (7, 10),             
        "template_path": Path(r"C:\Template\出库.xlsx"),
        "template_sheet": "Worksheet 1",
        "output_prefix": "出库_FBA",
    },
    {
        "name": "FBA OUT 2",
        "source_path": Path(r"C:\Frank\3.1_FBA.xlsx"),
        "sheet_name": "FBA扣减库存",
        "col_range": (19, 22),              
        "template_path": Path(r"C:\Template\出库.xlsx"),
        "template_sheet": "Worksheet 1",
        "output_prefix": "出库_FBA_2",
    },

    # ----- In -----
    {
        "name": "Return IN",
        "source_path": Path(r"C:\Frank\2.1_易仓管理.xlsx"),
        "sheet_name": "Return",
        "col_range": (7, 10),               # G‑I 
        "template_path": Path(r"C:\Template\入库.xlsx"),
        "template_sheet": "Worksheet 1",
        "output_prefix": "入库_return",
    },
]
