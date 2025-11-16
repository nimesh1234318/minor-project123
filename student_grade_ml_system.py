import json
import os
import numpy as np
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

class Student:
    def __init__(self, student_id, name, email, phone):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.grades = {}
        self.gpa = 0.0
        self.attendance = {}
        self.performance_risk = "Low"
    
    def add_grade(self, subject, marks):
        self.grades[subject] = marks
        self.calculate_gpa()
        self.update_performance_prediction()
    
    def add_attendance(self, subject, percentage):
        self.attendance[subject] = percentage
        self.update_performance_prediction()
    
    def calculate_gpa(self):
        if not self.grades:
            self.gpa = 0.0
            return
        
        total_marks = sum(self.grades.values())
        total_subjects = len(self.grades)
        average_marks = total_marks / total_subjects
        self.gpa = round((average_marks / 10), 2)
    
    def update_performance_prediction(self):
        if len(self.grades) < 2:
            self.performance_risk = "Low"
            return
        
        current_avg = np.mean(list(self.grades.values()))
        attendance_avg = np.mean(list(self.attendance.values())) if self.attendance else 85
        
        if current_avg < 40 or (attendance_avg < 75 and current_avg < 50):
            self.performance_risk = "High"
        elif current_avg < 60:
            self.performance_risk = "Medium"
        else:
            self.performance_risk = "Low"
    
    def get_grade_letter(self, marks):
        if marks >= 90:
            return 'A+'
        elif marks >= 80:
            return 'A'
        elif marks >= 70:
            return 'B'
        elif marks >= 60:
            return 'C'
        elif marks >= 50:
            return 'D'
        else:
            return 'F'
    
    def get_ml_recommendations(self):
        recommendations = []
        
        if self.performance_risk == "High":
            recommendations.append("⚠️  Needs immediate attention - High failure risk")
            recommendations.append("📚 Suggest extra classes and mentoring")
        elif self.performance_risk == "Medium":
            recommendations.append("🔶 Moderate risk - Regular monitoring needed")
            recommendations.append("💡 Focus on weak subjects")
        
        for subject, marks in self.grades.items():
            if marks < 60:
                recommendations.append(f"🎯 Improve {subject} (Current: {marks})")
        
        return recommendations
    
    def display_info(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"GPA: {self.gpa}")
        print(f"🎯 ML Performance Risk: {self.performance_risk}")
        
        recommendations = self.get_ml_recommendations()
        if recommendations:
            print("\n🤖 ML Recommendations:")
            for rec in recommendations:
                print(f"   • {rec}")
        
        if self.grades:
            print("\nGrades:")
            print("-" * 40)
            for subject, marks in self.grades.items():
                grade_letter = self.get_grade_letter(marks)
                attendance = self.attendance.get(subject, "N/A")
                print(f"{subject}: {marks} ({grade_letter}) | Attendance: {attendance}%")
        print("-" * 40)


class MLAnalyzer:
    def __init__(self):
        self.model = LinearRegression()
    
    def predict_final_score(self, current_grades, attendance):
        if len(current_grades) < 2:
            return "Need more data for prediction"
        
        X = np.array(list(range(len(current_grades)))).reshape(-1, 1)
        y = np.array(list(current_grades.values()))
        
        try:
            self.model.fit(X, y)
            future_score = self.model.predict([[len(current_grades)]])[0]
            future_score = max(0, min(100, future_score))
            
            if future_score >= 60:
                return f"Predicted Final: {future_score:.1f}% ✅ (Good)"
            elif future_score >= 40:
                return f"Predicted Final: {future_score:.1f}% ⚠️ (Needs Improvement)"
            else:
                return f"Predicted Final: {future_score:.1f}% ❌ (At Risk)"
        except:
            return "Prediction unavailable"
    
    def analyze_class_performance(self, students):
        if not students:
            return "No data available"
        
        grades_data = []
        for student in students:
            if student.grades:
                grades_data.extend(student.grades.values())
        
        if not grades_data:
            return "No grade data available"
        
        avg_grade = np.mean(grades_data)
        std_grade = np.std(grades_data)
        pass_rate = (sum(1 for g in grades_data if g >= 40) / len(grades_data)) * 100
        
        analysis = {
            "average_score": round(avg_grade, 2),
            "standard_deviation": round(std_grade, 2),
            "pass_rate": round(pass_rate, 2),
            "total_students_analyzed": len([s for s in students if s.grades])
        }
        
        return analysis


class Database:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.ml_analyzer = MLAnalyzer()
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    for student_id, student_data in data.items():
                        student = Student(
                            student_data['student_id'],
                            student_data['name'],
                            student_data['email'],
                            student_data['phone']
                        )
                        student.grades = student_data.get('grades', {})
                        student.gpa = student_data.get('gpa', 0.0)
                        student.attendance = student_data.get('attendance', {})
                        student.performance_risk = student_data.get('performance_risk', 'Low')
                        self.students[student_id] = student
            except Exception as e:
                print(f"Error loading data: {e}")
    
    def save_data(self):
        try:
            data = {}
            for student_id, student in self.students.items():
                data[student_id] = {
                    'student_id': student.student_id,
                    'name': student.name,
                    'email': student.email,
                    'phone': student.phone,
                    'grades': student.grades,
                    'gpa': student.gpa,
                    'attendance': student.attendance,
                    'performance_risk': student.performance_risk
                }
            
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_student(self, student):
        self.students[student.student_id] = student
        self.save_data()
    
    def get_student(self, student_id):
        return self.students.get(student_id)
    
    def get_all_students(self):
        return list(self.students.values())
    
    def update_student(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            self.save_data()
            return True
        return False
    
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            return True
        return False
    
    def student_exists(self, student_id):
        return student_id in self.students
    
    def get_ml_analysis(self):
        return self.ml_analyzer.analyze_class_performance(self.get_all_students())


class StudentGradeManager:
    def __init__(self):
        self.db = Database()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        print("\n" + "="*60)
        print("           🤖 STUDENT GRADE MANAGEMENT SYSTEM + ML")
        print("="*60)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Grades")
        print("7. Add Attendance")
        print("8. ML Analysis & Predictions")
        print("9. Generate Report")
        print("10. Exit")
        print("="*60)
    
    def display_students_table(self, students):
        if not students:
            print("\nNo students found!")
            return
        
        print("\n" + "-" * 120)
        print(f"{'Student ID':<12} {'Name':<20} {'Email':<25} {'GPA':<6} {'Risk':<10} {'Subjects':<8}")
        print("-" * 120)
        
        for student in students:
            risk_icon = "🔴" if student.performance_risk == "High" else "🟡" if student.performance_risk == "Medium" else "🟢"
            print(f"{student.student_id:<12} {student.name:<20} {student.email:<25} {student.gpa:<6} {risk_icon} {student.performance_risk:<8} {len(student.grades):<8}")
        
        print("-" * 120)
    
    def add_student(self):
        print("\n--- ADD NEW STUDENT ---")
        
        student_id = input("Enter Student ID: ").strip()
        if self.db.student_exists(student_id):
            print("Error: Student ID already exists!")
            return
        
        name = input("Enter Full Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone Number: ").strip()
        
        if not all([student_id, name, email, phone]):
            print("Error: All fields are required!")
            return
        
        student = Student(student_id, name, email, phone)
        self.db.add_student(student)
        print(f"\nStudent {name} added successfully!")
    
    def view_all_students(self):
        students = self.db.get_all_students()
        self.display_students_table(students)
    
    def search_student(self):
        student_id = input("\nEnter Student ID to search: ").strip()
        student = self.db.get_student(student_id)
        
        if student:
            student.display_info()
            
            if student.grades:
                prediction = self.db.ml_analyzer.predict_final_score(student.grades, student.attendance)
                print(f"\n🧠 ML Prediction: {prediction}")
        else:
            print("Student not found!")
    
    def update_student(self):
        student_id = input("\nEnter Student ID to update: ").strip()
        student = self.db.get_student(student_id)
        
        if not student:
            print("Student not found!")
            return
        
        print("\nCurrent Information:")
        student.display_info()
        
        print("\nEnter new information (leave blank to keep current):")
        name = input(f"Name [{student.name}]: ").strip()
        email = input(f"Email [{student.email}]: ").strip()
        phone = input(f"Phone [{student.phone}]: ").strip()
        
        if name:
            student.name = name
        if email:
            student.email = email
        if phone:
            student.phone = phone
        
        self.db.update_student(student_id, student)
        print("Student information updated successfully!")
    
    def delete_student(self):
        student_id = input("\nEnter Student ID to delete: ").strip()
        student = self.db.get_student(student_id)
        
        if not student:
            print("Student not found!")
            return
        
        print("\nStudent to be deleted:")
        student.display_info()
        
        confirm = input("\nAre you sure you want to delete this student? (y/n): ").lower()
        if confirm == 'y':
            self.db.delete_student(student_id)
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")
    
    def add_grades(self):
        student_id = input("\nEnter Student ID to add grades: ").strip()
        student = self.db.get_student(student_id)
        
        if not student:
            print("Student not found!")
            return
        
        print(f"\nAdding grades for: {student.name}")
        
        while True:
            subject = input("\nEnter subject name (or 'done' to finish): ").strip()
            if subject.lower() == 'done':
                break
            
            try:
                marks = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= marks <= 100:
                    student.add_grade(subject, marks)
                    self.db.update_student(student_id, student)
                    print(f"Grades for {subject} added successfully!")
                    
                    if len(student.grades) >= 2:
                        prediction = self.db.ml_analyzer.predict_final_score(student.grades, student.attendance)
                        print(f"   🧠 ML Update: {prediction}")
                else:
                    print("Marks must be between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")
    
    def add_attendance(self):
        student_id = input("\nEnter Student ID to add attendance: ").strip()
        student = self.db.get_student(student_id)
        
        if not student:
            print("Student not found!")
            return
        
        print(f"\nAdding attendance for: {student.name}")
        
        for subject in student.grades.keys():
            try:
                attendance = float(input(f"Enter attendance percentage for {subject} (0-100): "))
                if 0 <= attendance <= 100:
                    student.add_attendance(subject, attendance)
                    self.db.update_student(student_id, student)
                    print(f"Attendance for {subject} added successfully!")
                else:
                    print("Attendance must be between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")
                continue
    
    def ml_analysis(self):
        print("\n" + "="*50)
        print("           🧠 MACHINE LEARNING ANALYSIS")
        print("="*50)
        print("1. Class Performance Analysis")
        print("2. At-Risk Students Report")
        print("3. Individual Student Predictions")
        print("4. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            self.class_performance_analysis()
        elif choice == '2':
            self.at_risk_students()
        elif choice == '3':
            self.individual_predictions()
        elif choice == '4':
            return
        else:
            print("Invalid choice!")
    
    def class_performance_analysis(self):
        analysis = self.db.get_ml_analysis()
        
        if isinstance(analysis, str):
            print(analysis)
            return
        
        print("\n📊 CLASS PERFORMANCE ANALYSIS")
        print("="*40)
        print(f"Average Score: {analysis['average_score']}%")
        print(f"Standard Deviation: {analysis['standard_deviation']}")
        print(f"Pass Rate: {analysis['pass_rate']}%")
        print(f"Students Analyzed: {analysis['total_students_analyzed']}")
        
        if analysis['average_score'] < 50:
            print("\n🔴 Insight: Class needs academic intervention")
        elif analysis['average_score'] < 70:
            print("\n🟡 Insight: Class performance is moderate")
        else:
            print("\n🟢 Insight: Class performance is excellent")
    
    def at_risk_students(self):
        students = self.db.get_all_students()
        at_risk = [s for s in students if s.performance_risk == "High"]
        
        print("\n🔴 AT-RISK STUDENTS REPORT")
        print("="*50)
        
        if not at_risk:
            print("No at-risk students found! 🎉")
            return
        
        for student in at_risk:
            print(f"\n{student.name} (ID: {student.student_id})")
            print(f"GPA: {student.gpa} | Risk: {student.performance_risk}")
            recommendations = student.get_ml_recommendations()
            for rec in recommendations[:2]:
                print(f"  → {rec}")
    
    def individual_predictions(self):
        students = self.db.get_all_students()
        students_with_grades = [s for s in students if s.grades]
        
        print("\n🧠 INDIVIDUAL STUDENT PREDICTIONS")
        print("="*60)
        
        if not students_with_grades:
            print("No students with grade data available!")
            return
        
        for student in students_with_grades:
            prediction = self.db.ml_analyzer.predict_final_score(student.grades, student.attendance)
            print(f"{student.name:<20} | {prediction}")
    
    def generate_report(self):
        students = self.db.get_all_students()
        
        if not students:
            print("\nNo students found!")
            return
        
        print("\n" + "="*60)
        print("               STUDENT GRADE REPORT + ML INSIGHTS")
        print("="*60)
        
        for student in students:
            student.display_info()
        
        total_students = len(students)
        students_with_grades = len([s for s in students if s.grades])
        at_risk_count = len([s for s in students if s.performance_risk == "High"])
        
        print(f"\n🤖 ML SUMMARY STATISTICS:")
        print(f"Total Students: {total_students}")
        print(f"Students with Grades: {students_with_grades}")
        print(f"At-Risk Students: {at_risk_count}")
        
        analysis = self.db.get_ml_analysis()
        if not isinstance(analysis, str):
            print(f"Class Average: {analysis['average_score']}%")
            print(f"Pass Rate: {analysis['pass_rate']}%")
    
    def run(self):
        while True:
            self.clear_screen()
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-10): ").strip()
                
                if choice == '1':
                    self.add_student()
                elif choice == '2':
                    self.view_all_students()
                elif choice == '3':
                    self.search_student()
                elif choice == '4':
                    self.update_student()
                elif choice == '5':
                    self.delete_student()
                elif choice == '6':
                    self.add_grades()
                elif choice == '7':
                    self.add_attendance()
                elif choice == '8':
                    self.ml_analysis()
                elif choice == '9':
                    self.generate_report()
                elif choice == '10':
                    print("\nThank you for using Student Grade Management System with ML!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1-10.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Exiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to continue...")


if __name__ == "__main__":
    app = StudentGradeManager()
    app.run()