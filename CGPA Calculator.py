import tkinter as tk
from tkinter import messagebox

def calculate_cgpa():
    total_credit_hours = 0
    total_weighted_grade_points = 0
    
    try:
        num_subjects = int(num_subjects_entry.get())
        
        for i in range(num_subjects):
            grade = grade_entries[i].get().upper()
            credit_hours = float(credit_hour_entries[i].get())
            
            if grade in grade_points:
                grade_point = grade_points[grade]
                weighted_grade_point = grade_point * credit_hours
                
                total_credit_hours += credit_hours
                total_weighted_grade_points += weighted_grade_point
            else:
                messagebox.showerror("Error", "Invalid grade entered.")
                return
        
        cgpa = total_weighted_grade_points / total_credit_hours
        cgpa_label.config(text=f"CGPA: {cgpa:.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

grade_points = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0,
}

root = tk.Tk()
root.title("CGPA Calculator")

num_subjects_label = tk.Label(root, text="Enter the number of subjects:")
num_subjects_label.pack()

num_subjects_entry = tk.Entry(root)
num_subjects_entry.pack()

submit_button = tk.Button(root, text="Submit", command=calculate_cgpa)
submit_button.pack()

grade_entries = []
credit_hour_entries = []

for i in range(7): 
    grade_label = tk.Label(root, text=f"Enter grade for Subject {i+1}:")
    grade_label.pack()
    
    grade_entry = tk.Entry(root)
    grade_entry.pack()
    grade_entries.append(grade_entry)
    
    credit_hour_label = tk.Label(root, text=f"Enter credit hours for Subject {i+1}:")
    credit_hour_label.pack()
    
    credit_hour_entry = tk.Entry(root)
    credit_hour_entry.pack()
    credit_hour_entries.append(credit_hour_entry)

cgpa_label = tk.Label(root, text="")
cgpa_label.pack()

root.mainloop()
