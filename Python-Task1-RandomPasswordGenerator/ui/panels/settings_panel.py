import customtkinter as ctk

from ui.widgets import Card, Subtitle
from ui.styles import *


class SettingsPanel(Card):

    def __init__(self, master):

        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        Subtitle(
            self,
            "⚙ Password Settings"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20,10)
        )

        # -----------------------------
        # Scrollable Content
        # -----------------------------

        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.scroll.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=15,
            pady=(0,15)
        )

        self.scroll.grid_columnconfigure(0, weight=1)

        # --------------------------------

        self.length_var = ctk.IntVar(value=16)

        ctk.CTkLabel(
            self.scroll,
            text="Password Length",
            font=HEADER_FONT
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=(5,0)
        )

        self.length_label = ctk.CTkLabel(
            self.scroll,
            text="16",
            font=("Segoe UI",18,"bold"),
            text_color=PRIMARY
        )

        self.length_label.grid(
            row=0,
            column=1,
            padx=10
        )

        self.slider = ctk.CTkSlider(
            self.scroll,
            from_=6,
            to=64,
            variable=self.length_var,
            command=self.update_length
        )

        self.slider.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(5,20)
        )

        self.upper_var = ctk.BooleanVar(value=True)
        self.lower_var = ctk.BooleanVar(value=True)
        self.number_var = ctk.BooleanVar(value=True)
        self.symbol_var = ctk.BooleanVar(value=True)
        self.exclude_var = ctk.BooleanVar(value=False)

        options = [

            ("Include Uppercase (A-Z)", self.upper_var),

            ("Include Lowercase (a-z)", self.lower_var),

            ("Include Numbers (0-9)", self.number_var),

            ("Include Symbols (!@#$)", self.symbol_var),

            ("Exclude Similar Characters", self.exclude_var),

        ]

        for i, (text, var) in enumerate(options, start=2):

            ctk.CTkCheckBox(
                self.scroll,
                text=text,
                variable=var
            ).grid(
                row=i,
                column=0,
                sticky="w",
                pady=6
            )

    def update_length(self, value):

        self.length_label.configure(
            text=str(int(value))
        )

    def get_settings(self):

        return {

            "length": self.length_var.get(),

            "uppercase": self.upper_var.get(),

            "lowercase": self.lower_var.get(),

            "numbers": self.number_var.get(),

            "symbols": self.symbol_var.get(),

            "exclude_similar": self.exclude_var.get()

        }