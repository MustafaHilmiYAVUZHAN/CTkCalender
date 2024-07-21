"""
CTkCalendar - A custom Tkinter calendar widget

This module provides a CalendarApp class, which creates a customizable calendar widget using the CTk and tkinter libraries. The widget displays a calendar for the current month with navigation controls to switch between months. It also allows you to customize the appearance of the current day and handle day-click events.

Features:
- Displays a calendar with day names and day buttons
- Allows navigation between months
- Highlights the current day with customizable colors
- Provides an option to execute a callback function when a day is clicked
- Supports hiding or showing window elements

Dependencies:
- tkinter
- customtkinter
- hPyT
- pywinstyles
- datetime

Installation:
To install the dependencies, run:
    pip install customtkinter hPyT pywinstyles

Usage:
To use the CalendarApp class, instantiate it and call the `mainloop` method:

    from CTkCalendar import CalendarApp

    def on_day_click(selection):
        print(f"Selected date: {selection}")

    app = CalendarApp(command=on_day_click)
    app.mainloop()

For detailed documentation, visit the GitHub repository: https://github.com/MustafaHilmiYAVUZHAN

License:
This module is licensed under the [Your License] license. See LICENSE file for more details.

Contact:
For any questions or issues, please contact [your email or GitHub issues page].
"""

from .AppCalendar import CalendarApp
