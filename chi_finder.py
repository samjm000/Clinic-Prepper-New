# chi_finder
import pandas as pd  # Excel file handler
from datetime import datetime
from collections import OrderedDict


# function to return a dicitonary of times and chi numbers from excel sheet
def get_chi_numbers(excelFile):
    print(f"Running Excel import from {excelFile}")
    clinic_file = pd.ExcelFile(excelFile)

    # Read in sheet 1 CHI numbers and time from appropriately named columns "Time and CHI"
    clinic_sheet = clinic_file.parse("Sheet1", converters={"Time": str, "CHI": str})

    # Drop the rows where 'CHI' is NaN
    clinic_sheet = clinic_sheet.dropna(subset=["CHI"])

    # save data from sheet as series
    appt_time = clinic_sheet["Time"]
    chi_number = clinic_sheet["CHI"]

    # remove '(b)' from time string
    appt_time = appt_time.str.replace("(B)", ":00")

    # Convert the Series to a list
    chi_numbers = list(chi_number)
    appt_times = list(appt_time)

    # combine the lists together into a time/chi paired dictionary
    time_and_chi_dict = dict(zip(chi_numbers, appt_times))
    print(time_and_chi_dict)

    return time_and_chi_dict


# test the program
if __name__ == "__main__":
    get_chi_numbers(r"clinics\Clinic Prepper\Clinic List Monday 150424.xls")
