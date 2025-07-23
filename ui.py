import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as st
import sys

from tasks_config import TASKS
from task_runner import run_task
from transfer import stock_transfer
from walmart import WFS
from console_redirector import ConsoleRedirector
from utils import get_task_category, on_enter, on_leave

def create_gui():
    win = tk.Tk()
    win.title("🐶 DV Doggo - cg Edition")
    win.geometry("460x720")
    win.resizable(False, False)
    win.configure(bg="#FFF8E7")

    # --- Title ---
    tk.Label(
        win, text="🎨 cg Delivery Center 🐕💨",
        font=("Segoe UI", 20, "bold"),
        fg="#834D17", bg="#FFF8E7"
    ).pack(pady=(16, 8))

    # --- Inbound / Outbound Frames ---
    in_frame = tk.LabelFrame(win, text="📥 Inbound Task", padx=10, pady=8,
                             bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    in_frame.pack(fill="x", padx=20, pady=(6, 10))

    out_frame = tk.LabelFrame(win, text="📤 Outbound Tasks", padx=10, pady=8,
                              bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    out_frame.pack(fill="x", padx=20, pady=(0, 12))

    # --- Task Buttons ---
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

    # --- Transfer Frame ---
    transfer_frame = tk.LabelFrame(win, text="🔁 Transfer Task", padx=10, pady=8,
                                   bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    transfer_frame.pack(fill="x", padx=20, pady=(0, 12))

    tk.Button(
        transfer_frame,
        text="📋 Paste & Export", width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#FFD993", fg="#4B3B2A",
        relief="raised", bd=2,
        command=stock_transfer
    ).pack(pady=4)

    # --- Walmart Frame ---
    walmart_frame = tk.LabelFrame(win, text="🛒 Walmart", padx=10, pady=8,
                                  bg="#FAF3DD", fg="#4B3B2A", font=("Segoe UI", 10, "bold"))
    walmart_frame.pack(fill="x", padx=20, pady=(0, 12))

    tk.Button(
        walmart_frame,
        text="💾 Save As", width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#FFD993", fg="#4B3B2A",
        relief="raised", bd=2,
        command=WFS
    ).pack(pady=4)

    # --- Exit Button ---
    tk.Button(
        win,
        text="🐶 Exit Program", width=20,
        font=('Segoe UI', 12, 'bold'),
        bg="#E57373", fg="#fff",
        command=win.quit
    ).pack(pady=(10, 10))

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
