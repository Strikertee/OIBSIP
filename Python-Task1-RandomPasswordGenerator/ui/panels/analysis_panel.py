import customtkinter as ctk

from ui.widgets import Card, Subtitle
from ui.styles import *


class AnalysisPanel(Card):

    def __init__(self, master):

        super().__init__(master)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        Subtitle(
            self,
            "🛡 Password Analysis"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20,10)
        )

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

        self.strength = ctk.CTkLabel(
            self.scroll,
            text="Strength: -",
            font=("Segoe UI",18,"bold")
        )

        self.strength.grid(
            row=0,
            column=0,
            sticky="w",
            pady=5
        )

        self.progress = ctk.CTkProgressBar(
            self.scroll,
            height=18
        )

        self.progress.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(10,20)
        )

        self.progress.set(0)

        self.entropy = ctk.CTkLabel(
            self.scroll,
            text="Entropy: -"
        )

        self.entropy.grid(
            row=2,
            column=0,
            sticky="w",
            pady=6
        )

        self.crack = ctk.CTkLabel(
            self.scroll,
            text="Estimated Crack Time: -"
        )

        self.crack.grid(
            row=3,
            column=0,
            sticky="w",
            pady=6
        )

        self.feedback = ctk.CTkLabel(
            self.scroll,
            text="Suggestion: Generate or type a password.",
            wraplength=320,
            justify="left"
        )

        self.feedback.grid(
            row=4,
            column=0,
            sticky="w",
            pady=(15,5)
        )

    def update_analysis(
        self,
        strength,
        progress,
        entropy,
        crack_time
    ):

        self.strength.configure(
            text=f"Strength: {strength}"
        )

        self.progress.set(progress)

        self.entropy.configure(
            text=f"Entropy: {entropy} bits"
        )

        self.crack.configure(
            text=f"Estimated Crack Time: {crack_time}"
        )

        if strength == "Weak":

            msg = "Consider increasing the length and including numbers, uppercase letters, and symbols."

        elif strength == "Medium":

            msg = "A good password, but adding more unique characters will improve security."

        elif strength == "Strong":

            msg = "This password is strong. A few extra characters can make it even stronger."

        else:

            msg = "Excellent! This password provides a high level of security."

        self.feedback.configure(text=msg)

    def reset(self):

        self.update_analysis(
            "-",
            0,
            0,
            "-"
        )

        self.feedback.configure(
            text="Suggestion: Generate or type a password."
        )