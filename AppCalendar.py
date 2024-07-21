import tkinter as tk
import calendar
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkFont,set_default_color_theme,CTkToplevel
from hPyT import *
from pywinstyles import apply_style
from datetime import datetime
from typing import Optional, Callable
from os import path
class new_toplevel(CTkToplevel):
    def __init__(self,all_hide : any = False,topmost : bool = False):
        super().__init__()
        set_default_color_theme(path.join(path.dirname(path.realpath(__file__)), 'extreme.json'))
        self.configure(takefocus=False)
        if topmost:
            new_toplevel.attributes("-topmost", True)
        if all_hide is not None:
            if all_hide:
                all_stuffs.hide(self)
            else:
                maximize_minimize_button.hide(self)
        else:
            title_bar.hide(self)
        try:
            apply_style(self,"acrylic")
        except Exception as e:
            print(f"{e}\n\nMaybe you can try this>\npip install pywinstyles")

        #print(self.winfo_name())
class CalendarApp(new_toplevel):
    def __init__(self, all_hide : Optional[bool] = None, topmost : bool = False, print : bool = False, command: Optional[Callable] = None, current_day_color : str="#1050d0", current_day_color_hover : str="#0c2f60",day_color : str="#090909", day_color_hover : str="#333333"):
        super().__init__(all_hide=all_hide,topmost=topmost)
        self.title("Calendar")
        self.geometry("210x250")
        self.now = datetime.now()
        self.current_year = self.now.year
        self.current_month = self.now.month
        self.current_day = self.now.day

        self.print=print
        self.command=command
        self.all_hide=all_hide
        self.current_day_color=current_day_color
        self.current_day_color_hover=current_day_color_hover
        self.day_color=day_color
        self.day_color_hover=day_color_hover
        # Frame for the day names
        self.day_names_frame = CTkFrame(self, bg_color="#000000")
        self.day_names_frame.pack(pady=(10 if all_hide is None else 0,0))
        # Main frame for the calendar
        self.frame = CTkFrame(self, bg_color="#000000")
        self.frame.pack(expand=True, fill="both")
        
        self.day_font = CTkFont(size=9)
        self.header_frame = CTkFrame(self, bg_color="#000000")
        self.header_frame.pack(pady=(0,10))
        
        self.prev_button = CTkButton(self.header_frame, width=30, text="<", command=self.prev_month, bg_color="#000000")
        self.prev_button.grid(row=0, column=0)
        
        self.date_label = CTkLabel(self.header_frame, width=100, text="", bg_color="#000000")
        self.date_label.grid(row=0, column=1, padx=20)
        
        self.next_button = CTkButton(self.header_frame, width=30, text=">", command=self.next_month, bg_color="#000000")
        self.next_button.grid(row=0, column=2)
        
        self.update_timer = None  # Timer for delaying the update
        self.update_delay = 100  # Delay in milliseconds
        
        self.setup_day_names()
        self.update_calendar()

    def setup_day_names(self):
        day_names = calendar.weekheader(2).split()
        for j, day_name in enumerate(day_names):
            day_name_label = CTkLabel(self.day_names_frame, width=28,anchor="w", height=8,corner_radius=0, text=day_name, bg_color="#000000")
            day_name_label.grid(row=0, column=j, padx=1, pady=1)

    def update_calendar(self):
        # Update the month and year label immediately
        self.date_label.configure(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

        # Schedule the calendar grid update with a delay
        if self.update_timer is not None:
            self.after_cancel(self.update_timer)
        self.update_timer = self.after(self.update_delay, self.update_calendar_grid)

    def update_calendar_grid(self):
        self.clear_frame()
        cal = calendar.monthcalendar(self.current_year, self.current_month)
        for i, week in enumerate(cal):
            for j, day in enumerate(week):
                if day != 0:
                    button_text = str(day)
                    color = self.current_day_color if day == self.current_day and self.current_month == self.now.month and self.current_year == self.now.year else self.day_color
                    hover_color = self.current_day_color_hover if day == self.current_day and self.current_month == self.now.month and self.current_year == self.now.year else self.day_color_hover
                    button = CTkButton(self.frame, text=button_text, corner_radius=4, bg_color="#000000",hover_color=hover_color, font=self.day_font, fg_color=color, width=28, height=28, command=lambda d=day: self.day_click(d))
                    button.grid(row=i + 1, column=j, padx=1, pady=1)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def prev_month(self):
        if self.update_timer is not None:
            self.after_cancel(self.update_timer)
        self.current_month = self.current_month - 1 if self.current_month > 1 else 12
        self.current_year -= 1 if self.current_month == 12 else 0
        self.schedule_update()

    def next_month(self):
        if self.update_timer is not None:
            self.after_cancel(self.update_timer)
        self.current_month = self.current_month + 1 if self.current_month < 12 else 1
        self.current_year += 1 if self.current_month == 1 else 0
        self.schedule_update()

    def schedule_update(self):
        self.update_timer = self.after(self.update_delay, self.update_calendar)

    def day_click(self, day):
        if self.print:
            print(f"{day} {calendar.month_name[self.current_month]} {self.current_year} clicked!")
        self.selection = {"Day": day, "Month": calendar.month_name[self.current_month], "Year": self.current_year}
        if self.command is not None:
            self.command(self.selection)
        if self.all_hide is None:
            self.destroy()


if __name__ == "__main__":
    app = CalendarApp()
    app.mainloop()
