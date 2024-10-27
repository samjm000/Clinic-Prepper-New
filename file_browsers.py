from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os


def get_excel_file(self):
    filetypes = [("Excel files", "*.xls"), ("Excel 2007 files", "*.xlsx")]
    filepathforinfo = filedialog.askopenfilename(
        title="Open an Excel file", initialdir=os.getcwd(), filetypes=filetypes
    )

    # Import clinic list from Excel sheet
    self.input_excel_file = filepathforinfo
    self.upload_label.config(
        text=f"Selected input: .../{os.path.basename(self.input_excel_file)}"
    )
    print(f"Selected Clinic List: {os.path.basename(self.input_excel_file)}")


def get_source_folder(self):
    folder_path = askdirectory()
    if folder_path:
        self.selected_folder_label.config(
            text=f"Selected folder: .../{os.path.basename(folder_path)}"
        )
        self.input_folder = folder_path
        print(f"Selected Source Folder: {os.path.basename(folder_path)}")


def get_destination_folder(self):
    folder_path = askdirectory()
    if folder_path:
        self.destination_folder_label.config(
            text=f"Selected folder: .../{os.path.basename(folder_path)}"
        )
        self.output_folder = folder_path
        print(f"Selected Destination Folder: {os.path.basename(folder_path)}")
