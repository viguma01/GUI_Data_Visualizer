import wx
import json
import csv
import random
from faker import Faker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class IoTDataGenerator(wx.Frame):
    def __init__(self, parent, title):
        super(IoTDataGenerator, self).__init__(parent, title=title, size=(800, 600))
        self.fake = Faker()
        self.data = []

        # Setup Menu
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        stats_menu = wx.Menu()

        file_menu.Append(wx.ID_NEW, "&Generate IoT")
        file_menu.Append(wx.ID_SAVE, "&Save JSON")
        file_menu.Append(wx.ID_SAVEAS, "Save &CSV")

        stats_menu.Append(1, "&Descriptive")
        stats_menu.Append(2, "Plot &A")
        stats_menu.Append(3, "Plot &B")
        stats_menu.Append(4, "Plot &C")

        menubar.Append(file_menu, "&File")
        menubar.Append(stats_menu, "&Statistics")
        self.SetMenuBar(menubar)

        # Event Bindings
        self.Bind(wx.EVT_MENU, self.generate_iot_data, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.save_json, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.save_csv, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU, self.show_statistics, id=1)
        self.Bind(wx.EVT_MENU, self.plot_A, id=2)
        self.Bind(wx.EVT_MENU, self.plot_B, id=3)
        self.Bind(wx.EVT_MENU, self.plot_C, id=4)

        # Status Bar
        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText('Ready')
        self.Show(True)

    def generate_iot_data(self, event):
        self.statusbar.SetStatusText('Generating IoT Data...')
        try:
            for _ in range(10):  # Generate multiple records
                self.data.append({
                    "Firstname": self.fake.first_name(),
                    "Lastname": self.fake.last_name(),
                    "Age": self.fake.random_int(min=18, max=90),
                    "Gender": self.fake.random_element(elements=("Male", "Female", "Non-binary")),
                    "Username": self.fake.user_name(),
                    "Address": self.fake.address(),
                    "Email": self.fake.email(),
                    "Date": self.fake.date_this_decade(),
                    "Time": self.fake.time(),
                    "Outside Temperature (°C)": round(random.uniform(-10, 40), 2),
                    "Outside Humidity (%)": round(random.uniform(0, 100), 2),
                    "Room Temperature (°C)": round(random.uniform(15, 30), 2),
                    "Room Humidity (%)": round(random.uniform(20, 60), 2),
                })
        except Exception as e:
            wx.MessageBox(f"Error generating data: {e}", "Error", wx.OK | wx.ICON_ERROR)
        self.statusbar.SetStatusText('Ready')

    def save_json(self, event):
        if not self.data:
            wx.MessageBox("No data to save as JSON.", "Error", wx.OK | wx.ICON_ERROR)
            return

        file_dialog = wx.FileDialog(self, "Save JSON file", wildcard="JSON files (*.json)|*.json",
                                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if file_dialog.ShowModal() == wx.ID_CANCEL:
            return  # User cancelled the save operation

        path = file_dialog.GetPath()
        try:
            with open(path, 'w') as file:
                json.dump(self.data, file, indent=4)
            wx.MessageBox(f"Data successfully saved to {path}.", "Success", wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox(f"Failed to save file: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)

    def save_csv(self, event):
        if not self.data:
            wx.MessageBox("No data to save as CSV.", "Error", wx.OK | wx.ICON_ERROR)
            return

        file_dialog = wx.FileDialog(self, "Save CSV file", wildcard="CSV files (*.csv)|*.csv",
                                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if file_dialog.ShowModal() == wx.ID_CANCEL:
            return  # User cancelled the save operation

        path = file_dialog.GetPath()
        try:
            with open(path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            wx.MessageBox(f"Data successfully saved to {path}.", "Success", wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox(f"Failed to save file: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)


    def show_statistics(self, event):
        if self.data:
            data_df = pd.DataFrame(self.data)
            self.display_dataframe(data_df, "Generated IoT Data")
        else:
            wx.MessageBox("No data to display.", "Error", wx.OK | wx.ICON_ERROR)

    def display_dataframe(self, df, title):
        dialog = wx.Dialog(self, title=title, size=(800, 600))
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Using a TextCtrl to display data
        text_ctrl = wx.TextCtrl(dialog, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        # Formatting DataFrame as a string for display
        df_string = df.to_string(index=False)
        text_ctrl.SetValue(df_string)

        sizer.Add(text_ctrl, 1, wx.EXPAND)
        dialog.SetSizer(sizer)
        dialog.ShowModal()
        dialog.Destroy()

    def plot_A(self, event):
        if self.data:
            outside_temperature_data = [d['Outside Temperature (°C)'] for d in self.data]
            self.create_histogram(outside_temperature_data, 'Outside Temperature (°C)', 'Frequency', 'Histogram of Outside Temperature')
        else:
            wx.MessageBox("No data to plot.", "Error", wx.OK | wx.ICON_ERROR)

    def plot_B(self, event):
        if self.data:
            room_temperature_data = [d["Room Temperature (°C)"] for d in self.data]
            time_data = [d["Time"] for d in self.data]
            self.create_line_plot(time_data, room_temperature_data, 'Time', 'Room Temperature (°C)', 'Room Temperature Over Time')
        else:
            wx.MessageBox("No data to plot.", "Error", wx.OK | wx.ICON_ERROR)

    def plot_C(self, event):
        if self.data:
            outside_temperature_data = [d["Outside Temperature (°C)"] for d in self.data]
            outside_humidity_data = [d["Outside Humidity (%)"] for d in self.data]
            self.create_scatter_plot(outside_temperature_data, outside_humidity_data, 'Outside Temperature (°C)', 'Outside Humidity (%)', 'Scatter Plot of Outside Temperature vs. Outside Humidity')
        else:
            wx.MessageBox("No data to plot.", "Error", wx.OK | wx.ICON_ERROR)

    # Additional methods for plotting
    def create_histogram(self, data, x_label, y_label, title):
        plt.hist(data, bins=10, color='blue', edgecolor='black')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    def create_line_plot(self, x_data, y_data, x_label, y_label, title):
        plt.plot(x_data, y_data, marker='o', color='green', linestyle='-')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def create_scatter_plot(self, x_data, y_data, x_label, y_label, title):
        plt.scatter(x_data, y_data, color='red', marker='o')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = IoTDataGenerator(None, "IoT Data Generator")
    app.MainLoop()
