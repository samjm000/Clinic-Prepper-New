import os
import sys
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import ttkbootstrap
from tkinter.scrolledtext import ScrolledText
from date_finder import next_monday
import program_logic
from file_browsers import get_excel_file
from file_browsers import get_source_folder
from file_browsers import get_destination_folder


class CPApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.output_name = tk.StringVar(value="Clinic " + next_monday())
        self.input_excel_file = ""
        self.input_folder = ""
        self.output_folder = ""

        # GUI SETTINGS
        self.geometry("300x600")
        self.title("Clinic Prepper")

        # Style
        style = ttkbootstrap.Style()
        style.theme_use("lumen")

        # Welcome label
        welcome = ttk.Label(
            self, text="Welcome to Clinic Prepper", font=("Verdana", 12, "bold")
        )
        welcome.pack(padx=10, pady=5)

        # Create the "Select Source Folder" button & label
        select_source_button = ttk.Button(
            self,
            text="Select Source Document Folder",
            command=lambda: get_source_folder(self),
        )
        select_source_button.pack(padx=10, pady=5)
        self.selected_folder_label = ttk.Label(self, text="...")
        self.selected_folder_label.pack(padx=10, pady=5)

        # Create the "Select Destination Folder" button & label
        select_destination_button = ttk.Button(
            self,
            text="Select Destination Document Folder",
            command=lambda: get_destination_folder(self),
        )
        select_destination_button.pack(padx=10, pady=5)
        self.destination_folder_label = ttk.Label(self, text="...")
        self.destination_folder_label.pack(padx=10, pady=5)

        # Create the "Upload Clinic List  button & label
        upload_clinic_button = ttk.Button(
            self,
            text="Upload Clinic List From Template",
            command=lambda: get_excel_file(self),
        )
        upload_clinic_button.pack(padx=10, pady=5)
        self.upload_label = ttk.Label(self, text="...")
        self.upload_label.pack(padx=10, pady=5)

        # Input filename
        input_filename_button = ttk.Button(
            self,
            text="Enter File Name For Output Below",
            command=lambda: print("Please type filename in Box Provided."),
        )
        input_filename_button.pack(padx=10, pady=5)
        # label = ttk.Label(self, text="Enter file name for output:")
        # label.pack(padx=10, pady=5)

        self.output_box = ttk.Entry(self)
        self.output_box.insert(0, self.output_name.get())
        self.output_box.pack(padx=10, pady=10)

        # Run Program Button
        run_button = ttk.Button(self, text="Run", command=self.run_prepper)
        run_button.pack(padx=10, pady=10)

        # Create a Text widget for the system log
        self.log_text = ScrolledText(self, wrap=tk.WORD, height=10)
        self.log_text.pack(padx=10, pady=5)

        # Redirect stdout to the Text widget
        sys.stdout = self

        # Exit Program Button
        # exit_button = ttk.Button(self, text="Exit", command=self.quit)
        # exit_button.pack(padx=10, pady=10)

    def write(self, text):
        """Custom write method to redirect stdout to the Text widget."""
        self.log_text.insert(tk.END, text)  # Insert text at the end
        self.log_text.see(tk.END)  # Scroll to the end

    def run_prepper(self):
        print("Running now Clinic Prepper...")
        excel_file = self.input_excel_file
        output_filename = self.output_box.get()
        source_folder = self.input_folder
        destination_folder = self.output_folder

        # check for excel file
        if not excel_file:
            messagebox.showerror("Error", "No input Excel file selected")
            return

        # check for source folder
        if not source_folder:
            messagebox.showerror("Error", "No input folder selected")
            return

        # check filename
        if not output_filename.endswith(".docx"):
            output_filename += ".docx"
        # print(f"Running program with {self.input_excel_file, output_filename, source_folder}")
        result = program_logic.clinic_prepper(
            self.input_excel_file, output_filename, source_folder, destination_folder
        )
        messagebox.showinfo("Complete", f" Created file : {output_filename}")


if __name__ == "__main__":
    app = CPApp()
    app.mainloop()
