#!/usr/bin/python3
"""Module to manage patient information in a hospital setting."""

class Patient:
    """
    Class representing a patient.
    """

    def __init__(self, id, name, age, gender, admission_date, condition):
        """
        Initialize a new patient with the given details.
        """
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition

    def get_details(self):
        """Return a summary of the patient's information as a string.

        Returns:
            str: A formatted string containing the patient's details.
        """
        return (f"ID: {self.id}, Name: {self.name}, Age: {self.age}, "
                f"Gender: {self.gender}, Admission Date: {self.admission_date}, "
                f"Condition: {self.condition}")

def count_patients(patient_list):
    """Return the total number of patients in the patient list.

    Args:
        patient_list (list): A list of Patient objects.

    Returns:
        int: The total number of patients in the list.
    """
    return len(patient_list)

def list_patient_names(patient_list):
    """Return a list of names of all patients in the patient list.

    Args:
        patient_list (list): A list of Patient objects.

    Returns:
        list: A list containing the names of the patients.
    """
    return [patient.name for patient in patient_list]

def print_patient_by_id(patient_list):
    """Prompt for a patient ID and print the patient's details if found.

    Args:
        patient_list (list): A list of Patient objects.
    """
    try:
        patient_id = int(input("Enter patient ID: "))
        for patient in patient_list:
            if patient.id == patient_id:
                print(patient.get_details())
                return
        print("Patient not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")

if __name__ == "__main__":
    # Create instances of the Patient class
    patient1 = Patient(1, "Alice Mutoni", 30, "Female", "2023-01-10", "Flu")
    patient2 = Patient(2, "Sugira Johnson", 45, "Male", "2023-01-12", "Broken Arm")
    patient3 = Patient(3, "Berwa Julio", 28, "Male", "2023-01-15", "Anxiety")

    # Store patients in a list
    patients = [patient1, patient2, patient3]

    # Count and print the number of patients
    print(f"Total number of patients: {count_patients(patients)}")

    # List and print all patient names
    print("Patient Names:", list_patient_names(patients))

    # Optional: Print patient details by ID
    print_patient_by_id(patients)
