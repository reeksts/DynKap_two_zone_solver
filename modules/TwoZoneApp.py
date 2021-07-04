import tkinter as tk
from tkinter import ttk
from modules.TwoZoneSolver import TwoZoneSolver

class TwoZoneApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Two Zone Solver')

        # Adding main frame:
        self.main_frame = ttk.Frame(self, padding=10)
        self.main_frame.pack(side='top', fill='both', expand=True)

        # Adding variable frame
        self.variable_frame = tk.Frame(self.main_frame)
        self.variable_frame.pack(side='left')

        # Adding figure frame
        self.figure_frame = ttk.Frame(self.main_frame)
        self.figure_frame.pack(side='left')

        # Variables
        self.ri_var = tk.StringVar(value='0.036')
        self.ro_var = tk.StringVar(value='0.3')
        self.kdry_var = tk.StringVar(value='0.3052')
        self.kmoist_var = tk.StringVar(value='1.3')
        self.Ti_var = tk.StringVar(value='80')
        self.To_var = tk.StringVar(value='10')
        self.power_var = tk.StringVar(value='270')

        # Adding parameters with entry cells:
        self.ri_label = tk.Label(self.variable_frame, text='ri')
        self.ri_label.grid(row=0, column=0, padx=(0, 10), pady=(5, 0))
        self.ri_entry = tk.Entry(self.variable_frame, textvariable=self.ri_var)
        self.ri_entry.grid(row=0, column=1, padx=(0, 10), pady=(5, 0))

        self.ro_label = tk.Label(self.variable_frame, text='ro')
        self.ro_label.grid(row=1, column=0, padx=(0, 10), pady=(5, 0))
        self.ro_entry = tk.Entry(self.variable_frame, textvariable=self.ro_var)
        self.ro_entry.grid(row=1, column=1, padx=(0, 10), pady=(5, 0))

        self.kdry_label = tk.Label(self.variable_frame, text='k dry')
        self.kdry_label.grid(row=2, column=0, padx=(0, 10), pady=(5, 0))
        self.kdry_entry = tk.Entry(self.variable_frame, textvariable=self.kdry_var)
        self.kdry_entry.grid(row=2, column=1, padx=(0, 10), pady=(5, 0))

        self.kmoist_label = tk.Label(self.variable_frame, text='k moist')
        self.kmoist_label.grid(row=3, column=0, padx=(0, 10), pady=(5, 0))
        self.kmoist_entry = tk.Entry(self.variable_frame, textvariable=self.kmoist_var)
        self.kmoist_entry.grid(row=3, column=1, padx=(0, 10), pady=(5, 0))

        self.Ti_label = tk.Label(self.variable_frame, text='Ti')
        self.Ti_label.grid(row=4, column=0, padx=(0, 10), pady=(5, 0))
        self.Ti_entry = tk.Entry(self.variable_frame, textvariable=self.Ti_var)
        self.Ti_entry.grid(row=4, column=1, padx=(0, 10), pady=(5, 0))

        self.To_label = tk.Label(self.variable_frame, text='To')
        self.To_label.grid(row=5, column=0, padx=(0, 10), pady=(5, 0))
        self.To_entry = tk.Entry(self.variable_frame, textvariable=self.To_var)
        self.To_entry.grid(row=5, column=1, padx=(0, 10), pady=(5, 0))

        self.power_label = tk.Label(self.variable_frame, text='power')
        self.power_label.grid(row=6, column=0, padx=(0, 10), pady=(5, 0))
        self.power_entry = tk.Entry(self.variable_frame, textvariable=self.power_var)
        self.power_entry.grid(row=6, column=1, padx=(0, 10), pady=(5, 0))

        # Calculation button
        self.calculate_button = tk.Button(
            self.variable_frame,
            text='Calculate',
            command=self.calculate_zones)
        self.calculate_button.grid(row=7, column=0, pady=(20, 0))

        # Solver initialization
        self.solver = TwoZoneSolver(
            self.ri_var,
            self.ro_var,
            self.kdry_var,
            self.kmoist_var,
            self.Ti_var,
            self.To_var,
            self.power_var)

    def calculate_zones(self):
        self.solver.setter(
            self.ri_var.get(),
            self.ro_var.get(),
            self.kdry_var.get(),
            self.kmoist_var.get(),
            self.Ti_var.get(),
            self.To_var.get(),
            self.power_var.get())

        temps_min = self.solver.calculate_min_temp()
        temps_max = self.solver.calculate_max_temp()

        print(temps_min)
        print(temps_max)