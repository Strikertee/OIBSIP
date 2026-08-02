from tkinter import filedialog, messagebox
from datetime import datetime


def export(passwords):

    if not passwords:

        messagebox.showwarning(
            "Nothing to Export",
            "There are no passwords in the history."
        )

        return

    filename = filedialog.asksaveasfilename(
        title="Export Password History",
        initialfile=f"password_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not filename:
        return

    try:

        with open(filename, "w", encoding="utf-8") as file:

            file.write("PASSWORD HISTORY\n")
            file.write("=" * 60 + "\n\n")

            file.write(
                f"Exported: {datetime.now().strftime('%d %B %Y %H:%M:%S')}\n\n"
            )

            for i, password in enumerate(passwords, start=1):

                file.write(f"{i}. {password}\n")

        messagebox.showinfo(
            "Export Successful",
            f"Password history saved successfully.\n\n{filename}"
        )

    except Exception as e:

        messagebox.showerror(
            "Export Failed",
            str(e)
        )