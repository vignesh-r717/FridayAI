import customtkinter as ctk
import math

class AIOrb(ctk.CTkCanvas):

    def __init__(self, master, size=180):

        super().__init__(
            master,
            width=size,
            height=size,
            bg="#1a1a1a",
            highlightthickness=0
        )

        self.size = size
        self.angle = 0

        self.after(30, self.animate)

    def animate(self):

        self.delete("all")

        r = 55 + 8 * math.sin(self.angle)

        glow = 70 + 10 * math.sin(self.angle)

        cx = self.size / 2
        cy = self.size / 2

        self.create_oval(
            cx-glow,
            cy-glow,
            cx+glow,
            cy+glow,
            fill="#163c73",
            outline=""
        )

        self.create_oval(
            cx-r,
            cy-r,
            cx+r,
            cy+r,
            fill="#00bfff",
            outline=""
        )

        self.angle += 0.12

        self.after(30, self.animate)
        