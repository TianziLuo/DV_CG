def get_task_category(task):
    name = task.get("name", "")
    prefix = task.get("output_prefix", "")
    if "入库" in name or prefix.startswith("入库"):
        return "in"
    if "出库" in name or prefix.startswith("出库"):
        return "out"
    return "other"

def on_enter(e):
    e.widget.config(bg="#EFCB9A")

def on_leave(e):
    e.widget.config(bg="#F4D6A0")
