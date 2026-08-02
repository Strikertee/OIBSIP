import customtkinter as ctk

from ui.widgets import Card, Subtitle
from ui.styles import *


class PasswordPanel(Card):

    def __init__(self, master):

        super().__init__(master)

        self.change_callback = None
        self.password_visible = False

        self.grid_columnconfigure(0, weight=1)

        # -----------------------------
        # Header
        # -----------------------------

        Subtitle(
            self,
            "🔑 Password"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20, 10)
        )

        # -----------------------------
        # Password Variable
        # -----------------------------

        self.password_var = ctk.StringVar()

        self.password_var.trace_add(
            "write",
            self._password_changed
        )

        # -----------------------------
        # Password Frame
        # -----------------------------

        entry_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        entry_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 20)
        )

        entry_frame.grid_columnconfigure(0, weight=1)

        # -----------------------------
        # Entry
        # -----------------------------

        self.entry = ctk.CTkEntry(
            entry_frame,
            textvariable=self.password_var,
            height=50,
            font=("Consolas", 18),
            corner_radius=12,
            fg_color=ENTRY,
            border_color=BORDER,
            border_width=1,
            show="•"
        )

        self.entry.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        # -----------------------------
        # Show / Hide Button
        # -----------------------------

        self.eye_button = ctk.CTkButton(
            entry_frame,
            text="👁",
            width=45,
            height=50,
            corner_radius=12,
            fg_color=PRIMARY,
            hover_color=PRIMARY_HOVER,
            command=self.toggle_visibility
        )

        self.eye_button.grid(
            row=0,
            column=1,
            padx=(10, 0)
        )

    # ==================================
    # Public Methods
    # ==================================

    def get_password(self):

        return self.password_var.get()

    def set_password(self, password):

        self.password_var.set(password)

    def clear(self):

        self.password_var.set("")

    def focus(self):

        self.entry.focus()

    # ==================================
    # Visibility
    # ==================================

    def toggle_visibility(self):

        self.password_visible = not self.password_visible

        if self.password_visible:

            self.entry.configure(show="")

            self.eye_button.configure(
                text="🙈"
            )

        else:

            self.entry.configure(show="•")

            self.eye_button.configure(
                text="👁"
            )

    # ==================================
    # Callback Registration
    # ==================================

    def set_change_callback(
        self,
        callback
    ):

        self.change_callback = callback

    # ==================================
    # Internal
    # ==================================

    def _password_changed(
        self,
        *args
    ):

        if self.change_callback:

            self.change_callback(
                self.password_var.get()
            )