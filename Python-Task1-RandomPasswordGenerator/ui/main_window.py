import customtkinter as ctk

from generator.password_generator import PasswordGenerator
from generator.strength import PasswordStrength

from utils.clipboard import copy
from utils.exporter import export

from ui.styles import *

from ui.panels.password_panel import PasswordPanel
from ui.panels.settings_panel import SettingsPanel
from ui.panels.analysis_panel import AnalysisPanel
from ui.panels.history_panel import HistoryPanel
from ui.panels.button_panel import ButtonPanel


class PasswordGeneratorApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        # -----------------------------
        # Window
        # -----------------------------

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.title("Random Password Generator")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.minsize(MIN_WIDTH, MIN_HEIGHT)

        self.configure(
            fg_color=BACKGROUND
        )

        # -----------------------------
        # Grid
        # -----------------------------

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(1, weight=1)

        # -----------------------------
        # Header
        # -----------------------------

        self.header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20,10)
        )

        title = ctk.CTkLabel(
            self.header,
            text="🔐 Random Password Generator",
            font=TITLE_FONT
        )

        title.pack()

        subtitle = ctk.CTkLabel(
            self.header,
            text="Generate Strong, Secure & Unique Passwords",
            font=SUBTITLE_FONT,
            text_color=SUBTEXT
        )

        subtitle.pack()

        # -----------------------------
        # Main Dashboard
        # -----------------------------

        self.dashboard = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.dashboard.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10
        )

        self.dashboard.grid_columnconfigure(0, weight=3)
        self.dashboard.grid_columnconfigure(1, weight=2)

        self.dashboard.grid_rowconfigure(0, weight=1)
        self.dashboard.grid_rowconfigure(1, weight=1)
        self.dashboard.grid_rowconfigure(2, weight=0)

        # -----------------------------
        # Panels
        # -----------------------------

        self.password_panel = PasswordPanel(
            self.dashboard
        )

        self.password_panel.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.analysis_panel = AnalysisPanel(
            self.dashboard
        )

        self.analysis_panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.settings_panel = SettingsPanel(
            self.dashboard
        )

        self.settings_panel.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.history_panel = HistoryPanel(
            self.dashboard
        )

        self.history_panel.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.button_panel = ButtonPanel(
            self.dashboard,
            self.generate_password,
            self.copy_password,
            self.export_passwords
        )

        self.button_panel.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=(10,20)
        )

        # -----------------------------
        # Live Analysis
        # -----------------------------

        self.password_panel.set_change_callback(
            self.analyze_password
        )

        # -----------------------------
        # Keyboard Shortcuts
        # -----------------------------

        self.bind("<Control-g>", lambda e: self.generate_password())
        self.bind("<Control-c>", lambda e: self.copy_password())
        self.bind("<Control-e>", lambda e: self.export_passwords())

    # ==================================================

    def generate_password(self):

        settings = self.settings_panel.get_settings()

        password = PasswordGenerator.generate(
            length=settings["length"],
            uppercase=settings["uppercase"],
            lowercase=settings["lowercase"],
            numbers=settings["numbers"],
            symbols=settings["symbols"],
            exclude_similar=settings["exclude_similar"]
        )

        self.password_panel.set_password(password)
        result = PasswordStrength.analyze(password)

        self.history_panel.add_password(
            password,
            result["strength"]
)

    # ==================================================

    def analyze_password(self, password):

        if not password:

            self.analysis_panel.reset()

            return

        result = PasswordStrength.analyze(password)

        self.analysis_panel.update_analysis(
            result["strength"],
            result["progress"],
            result["entropy"],
            result["crack_time"]
        )

    # ==================================================

    def copy_password(self):

        password = self.password_panel.get_password()

        if password:

            copy(password)

    # ==================================================

    def export_passwords(self):

        export(self.history_panel.passwords)