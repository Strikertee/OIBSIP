import customtkinter as ctk

from ui.styles import *


class Card(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=CARD,
            corner_radius=CORNER_RADIUS,
            border_width=1,
            border_color=BORDER
        )


class Title(ctk.CTkLabel):

    def __init__(self, master, text):

        super().__init__(
            master,
            text=text,
            font=TITLE_FONT,
            text_color=TEXT
        )


class Subtitle(ctk.CTkLabel):

    def __init__(self, master, text):

        super().__init__(
            master,
            text=text,
            font=HEADER_FONT,
            text_color=TEXT
        )


class Caption(ctk.CTkLabel):

    def __init__(self, master, text):

        super().__init__(
            master,
            text=text,
            font=SMALL_FONT,
            text_color=SUBTEXT
        )


class PrimaryButton(ctk.CTkButton):

    def __init__(self, master, text, command):

        super().__init__(
            master,
            text=text,
            command=command,
            height=46,
            corner_radius=12,
            font=BUTTON_FONT,
            fg_color=PRIMARY,
            hover_color=PRIMARY_HOVER
        )