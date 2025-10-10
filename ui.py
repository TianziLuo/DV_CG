import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as st
import sys

from tasks_config import TASKS
from task_runner import run_task
from utils_func.transfer import stock_transfer
from WFS.WFS_up import WFS_upload
from WFS.WFS_out import WFS_out
from inventory_check import inventory_check
from packing_detail import packing_detail
from error_code_process import text_errorcode
from console_redirector import ConsoleRedirector
from task_cate import get_task_category, on_enter, on_leave


def create_gui():
    win = tk.Tk()
    win.title("🐶 DV Doggo - cg Edition")
    win.geometry("820x600")
    win.resizable(False, False)
    win.configure(bg="#FFF8E7")

    # --- Title ---
    tk.Label(
        win, text="🎨 cg Delivery Center 🐕💨",
        font=("Segoe UI", 20, "bold"),
        fg="#834D17", bg="#FFF8E7"
    ).pack(pady=(16, 8))

    # --- Main container (2 columns) ---
    main_frame = tk.Frame(win, bg="#FFF8E7")
    main_frame.pack(fill="both", expand=True, padx=20, pady=10)

    left_col = tk.Frame(main_frame, bg="#FFF8E7")
    left_col.pack(side="left", fill="both", expand=True, padx=(0, 10))

    right_col = tk.Frame(main_frame, bg="#FFF8E7")
    right_col.pack(side="right", fill="both", expand=True, padx=(10, 0))

    # --- Inbound / Outbound Frames (Left) ---
    in_frame = tk.LabelFrame(left_col, text="📥 Inbound Task", padx=10, pady=8,
                             bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    in_frame.pack(fill="x", pady=(0, 12))

    out_frame = tk.LabelFrame(left_col, text="📤 Outbound Tasks", padx=10, pady=8,
                              bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    out_frame.pack(fill="x", pady=(0, 12))

    # --- Walmart / Others (Right) ---
    walmart_frame = tk.LabelFrame(right_col, text="🛒 Walmart", padx=10, pady=8,
                                  bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    walmart_frame.pack(fill="x", pady=(0, 12))

    others_frame = tk.LabelFrame(right_col, text="🔁 Other Tools", padx=10, pady=8,
                                 bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    others_frame.pack(fill="x", pady=(0, 12))

    # --- Debug Button ---
    tk.Button(
    right_col,
    text="🐶 Fix Error",
    width=20,
    font=('Segoe UI', 12, 'bold'),
    bg="#E57373",
    fg="#e0d9d9",
    command=text_errorcode
    ).pack(pady=(20, 10))

    # --- Task Execution Helper ---
    def execute_task(task):
        try:
            print(f"[RUN] Executing task: {task['name']} ...")
            success = run_task(task)
            if success:
                print(f"[SUCCESS] Task completed: {task['name']} ✅")
            else:
                print(f"[FAIL] Task failed: {task['name']} ❌")
                messagebox.showerror("Error", f"❌ Failed: {task['name']}")
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
            messagebox.showerror("Error", f"❌ Exception: {e}")

    # --- Create TASK Buttons ---
    for task in TASKS:
        cat = get_task_category(task)
        parent = in_frame if cat == "in" else out_frame
        btn = tk.Button(
            parent,
            text="🐾 " + task["name"],
            width=20,
            font=('Segoe UI', 12, 'bold'),
            bg="#FFD993", fg="#4B3B2A",
            relief="raised", bd=2,
            command=lambda t=task: execute_task(t)
        )
        btn.pack(pady=4)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # --- Walmart Buttons ---
    tk.Button(
        walmart_frame,
        text="💾 WFS Upload", width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#FFD993", fg="#4B3B2A",
        relief="raised", bd=2,
        command=WFS_upload
    ).pack(pady=4)

    tk.Button(
        walmart_frame,
        text="💾 WFS Outbound", width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#FFD993", fg="#4B3B2A",
        relief="raised", bd=2,
        command=WFS_out
    ).pack(pady=4)

    # --- Others Buttons ---
    tk.Button(
        others_frame,
        text="📋 Stock Transfer", width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#FFD993", fg="#4B3B2A",
        relief="raised", bd=2,
        command=stock_transfer
    ).pack(pady=4)

    tk.Button(
        others_frame,
        text="📋 Inventory Check", width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#FFD993", fg="#4B3B2A",
        relief="raised", bd=2,
        command=inventory_check
    ).pack(pady=4)

    tk.Button(
        others_frame,
        text="📋 Packing Details", width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#FFD993", fg="#4B3B2A",
        relief="raised", bd=2,
        command=packing_detail
    ).pack(pady=4)

     # --- Console Log ---
    tk.Label(
        win, text="📋 Console Log:",
        font=("Segoe UI", 10, "bold"),
        bg="#FFF8E7", fg="#4B3B2A",
        anchor="w"
    ).pack(fill="x", padx=20, pady=(2, 0))

    console = st.ScrolledText(
        win, height=10,
        font=("Consolas", 10),
        bg="#F7F4E9", fg="#333",
        relief="sunken"
    )
    console.pack(fill="both", expand=False, padx=20, pady=(0, 12))

    # Console Redirection
    sys.stdout = ConsoleRedirector(console)
    sys.stderr = ConsoleRedirector(console)

    win.mainloop()
