import tkinter as tk
from tkinter import ttk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy tính")
        self.root.geometry("360x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.expression = ""

        self.display_var = tk.StringVar(value="0")

        display_frame = ttk.Frame(root, padding=(10, 10, 10, 8))
        display_frame.pack(fill="x")

        self.display = ttk.Entry(
            display_frame,
            textvariable=self.display_var,
            justify="right",
            font=("Segoe UI", 22),
            state="readonly"
        )
        self.display.pack(fill="x", ipady=8)

        buttons = [
            ("C", "clear"),
            ("⌫", "back"),
            ("%", "percent"),
            ("/", "operator"),
            ("7", "num"),
            ("8", "num"),
            ("9", "num"),
            ("*", "operator"),
            ("4", "num"),
            ("5", "num"),
            ("6", "num"),
            ("-", "operator"),
            ("1", "num"),
            ("2", "num"),
            ("3", "num"),
            ("+", "operator"),
            ("0", "num"),
            (".", "dot"),
            ("=", "equal"),
        ]

        button_frame = ttk.Frame(root, padding=(10, 0, 10, 10))
        button_frame.pack(fill="both", expand=True)

        for i, (text, kind) in enumerate(buttons):
            row = i // 4
            col = i % 4
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Segoe UI", 18),
                width=6,
                height=2,
                bd=0,
                cursor="hand2",
                bg=self.get_button_color(kind),
                fg="#ffffff" if kind in ("operator", "equal") else "#222222",
                command=lambda t=text, k=kind: self.handle_click(t, k),
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

        for r in range(5):
            button_frame.rowconfigure(r, weight=1)
        for c in range(4):
            button_frame.columnconfigure(c, weight=1)

        root.bind("<KeyPress>", self.on_key_press)

    def get_button_color(self, kind):
        colors = {
            "operator": "#f39c12",
            "equal": "#2ecc71",
            "clear": "#e74c3c",
            "back": "#95a5a6",
            "percent": "#95a5a6",
            "dot": "#f7f7f7",
            "num": "#ffffff",
        }
        return colors.get(kind, "#ffffff")

    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key in ".+-*/%":
            self.handle_click(key, "num" if key.isdigit() or key == "." else ("operator" if key != "%" else "percent"))
        elif event.keysym == "Return":
            self.handle_click("=", "equal")
        elif event.keysym == "BackSpace":
            self.handle_click("⌫", "back")
        elif event.keysym == "Escape":
            self.handle_click("C", "clear")

    def handle_click(self, value, kind):
        if kind == "num" or kind == "dot":
            if value == "." and "." in self.expression.split("[")[-1].split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]:
                return
            self.expression += value
            self.display_var.set(self.expression)
        elif kind == "operator":
            if self.expression and self.expression[-1] not in "+-*/":
                self.expression += value
                self.display_var.set(self.expression)
        elif kind == "percent":
            try:
                result = eval(self.expression, {"__builtins__": None}, {}) if self.expression else 0
                self.expression = str(result / 100)
                self.display_var.set(self.expression)
            except Exception:
                self.display_var.set("Error")
        elif kind == "back":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif kind == "clear":
            self.expression = ""
            self.display_var.set("0")
        elif kind == "equal":
            self.evaluate()

    def evaluate(self):
        try:
            # Giới hạn chỉ cho phép các toán tử an toàn
            allowed = {"__builtins__": None}
            result = eval(self.expression, allowed, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self.display_var.set(self.expression)
        except Exception:
            self.display_var.set("Error")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
