class Patient:
    """Class to represent and indicate patient's information in the healthcare system."""
    
    def __init__(self, id, name, age, gender, admission_date, condition):
        """Initialize a patient with their details."""
        self.id = id                
        self.name = name            
        self.age = age            
        self.gender = gender.capitalize()  # Standardize gender format        
        self.admission_date = admission_date  
        self.condition = condition
    
    def get_details(self):  
        """Get the information of the patient as string."""
        return (f"ID: {self.id}, Name: {self.name}, Age: {self.age}, "
                f"Gender: {self.gender}, Admission Date: {self.admission_date}, "
                f"Condition: {self.condition}")

def count_patients(patient_list):
    """Count number of patients available."""
    return len(patient_list)

def list_patient_names(patient_list):
    """Return a list of all patient names."""
    return [patient.name for patient in patient_list]

def print_patient_by_id(patient_list):
    """Print patient details by their ID."""
    try:
        patient_id = int(input("Enter patient ID: "))
        for patient in patient_list:
            if patient.id == patient_id:
                print(patient.get_details())
                return
        print("Patient not found.")
    except ValueError:
        print("Please enter a valid numeric ID.")

def main():
    # Create multiple patient objects
    patients = [
        Patient(1, "Ineza Tania", 20, "Female", "2024-10-15", "stomache"),
        Patient(2, "Destin Manzi", 22, "Male", "2024-10-20", "backbone"),
        Patient(3, "Claudia Adeline", 18, "Female", "2024-10-10", "headache"),
    ]
    
    # Show the total number of patients at the center
    print("Total number of patients:", count_patients(patients))
    
    # List patients' names
    print("Patient names:", list_patient_names(patients))
    
    # Show patient details by ID
    print_patient_by_id(patients)

if __name__ == "__main__":
    main()
