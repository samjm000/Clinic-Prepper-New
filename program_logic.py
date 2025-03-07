# program_logic.py

import document_converter
import excel_processor
import document_organiser
import patient_details_finder
import document_builder


# Create parent clinic List
def clinic_prepper(input_excel_file, file_name, source_folder, destination_folder):

    # Importing Excel file details
    # print(f"Reading in File : {input_excel_file}")
    CHI_time_List = excel_processor.get_chi_numbers(input_excel_file)
    print(f"Generated time and CHI dictionary: {CHI_time_List}\\n")

    # organise and get list of previous documents (Not dealt with .doc files yet)
    sorted_document_list = document_organiser.get_documents_in_order(source_folder)

    # get new document list converting .doc to .docx
    # all_documents_docx = document_converter.process_documents(sorted_document_list)
    all_documents_docx = sorted_document_list

    # import patient clinic list details
    patient_clinic_list = patient_details_finder.patient_details_finder(
        CHI_time_List, all_documents_docx
    )

    # build the word document with the patient clinic list
    completion_details = document_builder.create_word_document(
        patient_clinic_list, file_name, destination_folder
    )

    # Output the results in a word document
    return completion_details


if __name__ == "__main__":
    print("Running Program")
