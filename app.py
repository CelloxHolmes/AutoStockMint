import tkinter as tk
from tkinter import messagebox

PRIMARY_COLOR = "#2e3f4f"
ACCENT_COLOR = "#00bcd4"
BG_COLOR = "#f7f7f7"
FONT_HEADER = ("Segoe UI", 20, "bold")
FONT_BUTTON = ("Segoe UI", 12)

class AutoStockMintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoStockMint")
        self.root.geometry("420x420")
        self.root.configure(bg=BG_COLOR)

        self.build_ui()

    def build_ui(self):
        tk.Label(
            self.root,
            text="🎨 AutoStockMint",
            bg=BG_COLOR,
            fg=PRIMARY_COLOR,
            font=FONT_HEADER
        ).pack(pady=(30, 20))

        buttons = [
            ("1. Generate AI Prompt", self.generate_prompt),
            ("2. Generate Image with Midjourney", self.generate_image),
            ("3. Add Metadata & Tags", self.add_metadata),
            ("4. Upload to Adobe Stock", self.upload),
            ("Exit", self.root.quit),
        ]

        for text, command in buttons:
            btn = tk.Button(
                self.root,
                text=text,
                font=FONT_BUTTON,
                width=30,
                height=2,
                bg=ACCENT_COLOR,
                fg="white",
                bd=0,
                activebackground="#0097a7",
                command=command
            )
            btn.pack(pady=8)

    def generate_prompt(self):
        messagebox.showinfo("Prompt", "ยังไม่เชื่อม GPT")

    def generate_image(self):
        messagebox.showinfo("Midjourney", "ยังไม่เชื่อม Discord bot")

    def add_metadata(self):
        messagebox.showinfo("Metadata", "ยังไม่เชื่อม AI keyword")

    def upload(self):
        messagebox.showinfo("Upload", "ยังไม่เชื่อม Adobe Stock")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoStockMintApp(root)
    root.mainloop()
