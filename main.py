
import PyPDF2
import os

class Patient:
    def __init__(self, name, mrn, dob, underlying_conditions, procedure_name, procedure_location):
        self.name = name
        self.mrn = mrn
        self.dob = dob
        self.underlying_conditions = underlying_conditions
        self.procedure_name = procedure_name
        self.procedure_location = procedure_location

def extract_patient_info(pdf_file):
    patient_info = []
    pdf = PyPDF2.PdfReader(open(pdf_file, 'rb'))
    
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        page_text = page.extract_text()
        
        # Example: Assuming the text contains labels for patient information
        labels = {
            'Name': 'name',
            'MRN': 'mrn',
            'Date of Birth': 'dob',
            'Underlying Conditions': 'underlying_conditions',
            'Procedure Name': 'procedure_name',
            'Procedure Location': 'procedure_location'
        }
        
        patient_data = {}
        for label, attr in labels.items():
            start_index = page_text.find(label)
            if start_index != -1:
                end_index = page_text.find('\n', start_index)
                if end_index != -1:
                    data = page_text[start_index + len(label):end_index].strip()
                    patient_data[attr] = data
        
        if patient_data:
            patient = Patient(**patient_data)
            patient_info.append(patient)
    
    return patient_info

def display_patient_info(patient_info):
    for idx, patient in enumerate(patient_info, start=1):
        print(f"Patient {idx}:")
        print(f"Name: {patient.name}")
        print(f"MRN: {patient.mrn}")
        print(f"Date of Birth: {patient.dob}")
        print(f"Underlying Conditions: {patient.underlying_conditions}")
        print(f"Procedure Name: {patient.procedure_name}")
        print(f"Procedure Location: {patient.procedure_location}")
        print()

if __name__ == "__main__":
    pdf_file = "Surgical_Notes.pdf"  # Replace with the path to your PDF file
    patient_info = extract_patient_info(pdf_file)
    
    if patient_info:
        display_patient_info(patient_info)
    else:
        print("No patient information found in the PDF.")