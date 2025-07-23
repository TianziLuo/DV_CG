import tkinter as tk

class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        if message.strip() == "":
            return  # Skip empty messages

        # Get the insertion start index
        start_index = self.text_widget.index(tk.END + "-1c")

        # Insert the message and scroll to the end
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)

        # Get the index after insertion
        end_index = self.text_widget.index(tk.END)

        # Schedule deletion of this message after 3 seconds (3000 ms)
        self.text_widget.after(3000, lambda: self._delete_range(start_index, end_index))

    def _delete_range(self, start, end):
        try:
            # Safely delete the message range
            self.text_widget.delete(start, end)
        except tk.TclError:
            pass  # Ignore errors if already deleted

    def flush(self):
        pass  # Required to support sys.stdout/sys.stderr redirection
