import customtkinter as ctk

from ui.styles import *


class ButtonPanel(ctk.CTkFrame):

    def __init__(
        self,
        master,
        generate_callback,
        copy_callback,
        export_callback
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure((0, 1, 2), weight=1)

        # ---------------------------------------
        # Generate Button
        # ---------------------------------------

        self.generate_btn = ctk.CTkButton(
            self,
            text="🔐 Generate Password",
            command=generate_callback,
            height=50,
            corner_radius=12,
            font=BUTTON_FONT,
            fg_color=PRIMARY,
            hover_color=PRIMARY_HOVER
        )

        self.generate_btn.grid(
            row=0,
            column=0,
            padx=10,
            sticky="ew"
        )

        # ---------------------------------------
        # Copy Button
        # ---------------------------------------

        self.copy_btn = ctk.CTkButton(
            self,
            text="📋 Copy",
            command=copy_callback,
            height=50,
            corner_radius=12,
            font=BUTTON_FONT,
            fg_color=SUCCESS,
            hover_color="#16A34A"
        )

        self.copy_btn.grid(
            row=0,
            column=1,
            padx=10,
            sticky="ew"
        )

        # ---------------------------------------
        # Export Button
        # ---------------------------------------

        self.export_btn = ctk.CTkButton(
            self,
            text="💾 Export",
            command=export_callback,
            height=50,
            corner_radius=12,
            font=BUTTON_FONT,
            fg_color="#7C3AED",
            hover_color="#6D28D9"
        )

        self.export_btn.grid(
            row=0,
            column=2,
            padx=10,
            sticky="ew"
        )

    # ===================================================

    def enable(self):

        self.generate_btn.configure(state="normal")
        self.copy_btn.configure(state="normal")
        self.export_btn.configure(state="normal")

    # ===================================================

    def disable(self):

        self.generate_btn.configure(state="disabled")
        self.copy_btn.configure(state="disabled")
        self.export_btn.configure(state="disabled")