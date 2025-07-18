import tkinter as tk
from tkinter import messagebox
from tasks_config import TASKS
from task_runner import run_task 
from transfer import stock_transfer

def get_task_category(task):
    name = task.get("name", "")
    prefix = task.get("output_prefix", "")
    if "入库" in name or prefix.startswith("入库"):
        return "in"
    if "出库" in name or prefix.startswith("出库"):
        return "out"
    return "other"

# === Callback for execution button ===
def execute_task(task):
    success = run_task(task)
    if success:
        messagebox.showinfo("Completed", f"✅ Done: {task['name']}")
    else:
        messagebox.showerror("Error", f"❌ Failed: {task['name']}, check error code")

def create_gui():
    win = tk.Tk()
    win.title("🐶 DV Doggo - cg Edition")
    win.geometry("420x580")
    win.resizable(False, False)
    win.configure(bg="#FFF8E7")  

    # ---- Top label ----
    tk.Label(
        win,
        text="🐾 cg Delivery Center 🐕💨",
        font=("Segoe UI", 20, "bold"),
        fg="#834D17",       # Paw orange
        bg="#FFF8E7"
    ).pack(pady=(16, 8))

    # ---- Frame: Inbound tasks ----
    in_frame = tk.LabelFrame(win, text="📥 Inbound Task", padx=10, pady=8,
                             bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    in_frame.pack(fill="x", padx=20, pady=(6, 10))

    # ---- Frame: Outbound tasks ----
    out_frame = tk.LabelFrame(win, text="📤 Outbound Tasks", padx=10, pady=8,
                              bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    out_frame.pack(fill="x", padx=20, pady=(0, 12))

    # ---- Create buttons ----
    def on_enter(e): e.widget.config(bg="#EFCB9A")  # Hover color
    def on_leave(e): e.widget.config(bg="#F4D6A0")  # Normal color

    for task in TASKS:
        cat = get_task_category(task)
        parent = in_frame if cat == "in" else out_frame
        btn = tk.Button(
            parent,
            text="🐾 " + task["name"],
            width=20,
            font=('Segoe UI', 12, 'bold'),
            bg="#FFD993",       # Button color
            fg="#4B3B2A",
            relief="raised",
            bd=2,
            command=lambda t=task: execute_task(t)
        )
        btn.pack(pady=4)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

# ---- Frame: Tools (for Transfer Task) ----
    tool_frame = tk.LabelFrame(win, text="📤 Transfer Task", padx=10, pady=8,
                               bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    tool_frame.pack(fill="x", padx=20, pady=(0, 12))

    transfer_btn = tk.Button(
        tool_frame,
        text="📋 Paste & Export",
        width=24,
        font=('Segoe UI', 12, 'bold'),
        bg="#FFD993",
        fg="#4B3B2A",
        relief="raised",
        bd=2,
        command=stock_transfer  
    )
    transfer_btn.pack(pady=4)
    transfer_btn.bind("<Enter>", on_enter)
    transfer_btn.bind("<Leave>", on_leave)

    # ---- Exit button ----
    exit_btn = tk.Button(
        win,
        text="🐶 Exit Program",
        width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#E57373",       
        fg="#fff",
        command=win.quit
    )
    exit_btn.pack(pady=(10, 20))

    win.mainloop()

