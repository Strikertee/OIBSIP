import customtkinter as ctk

from ui.widgets import Card, Subtitle
from ui.styles import *


class HistoryPanel(Card):

    def __init__(self, master):

        super().__init__(master)

        self.passwords = []

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # -----------------------------------
        # Header
        # -----------------------------------

        Subtitle(
            self,
            "📜 Password History"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20, 15)
        )

        # -----------------------------------
        # Scrollable Area
        # -----------------------------------

        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.scroll_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.scroll_frame.grid_columnconfigure(0, weight=1)

    # =====================================================

    def add_password(self, password, strength="Unknown"):

        self.passwords.append(password)

        colors = {
            "Weak": DANGER,
            "Medium": WARNING,
            "Strong": PRIMARY,
            "Very Strong": SUCCESS
        }

        color = colors.get(strength, SUBTEXT)

        row = len(self.passwords)

        item = ctk.CTkFrame(
            self.scroll_frame,
            fg_color=ENTRY,
            corner_radius=10
        )

        item.grid(
            row=row,
            column=0,
            sticky="ew",
            pady=5
        )

        item.grid_columnconfigure(0, weight=1)

        # Mask the password except the first and last 2 characters
        if len(password) > 6:
            masked = (
                password[:2]
                + "*" * (len(password) - 4)
                + password[-2:]
            )
        else:
            masked = "*" * len(password)

        password_label = ctk.CTkLabel(
            item,
            text=masked,
            font=("Consolas", 14)
        )

        password_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=10
        )

        badge = ctk.CTkLabel(
            item,
            text=strength,
            text_color=color,
            font=("Segoe UI", 13, "bold")
        )

        badge.grid(
            row=0,
            column=1,
            padx=15
        )

        copy_btn = ctk.CTkButton(
            item,
            text="📋",
            width=40,
            command=lambda p=password: self.copy_password(p)
        )

        copy_btn.grid(
            row=0,
            column=2,
            padx=(0, 10)
        )

    # =====================================================

    def copy_password(self, password):

        self.clipboard_clear()

        self.clipboard_append(password)

    # =====================================================

    def clear(self):

        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        self.passwords.clear()