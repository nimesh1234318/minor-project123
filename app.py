from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os
import sys

# Add parent directory to import ML modules
sys.path.append('..')

app = Flask(__name__, static_folder='.', template_folder='.')
CORS(app)

# Your exact student data
student_data = {
    "100": {
        "student_id": "100",
        "name": "Aarav Sharma",
        "email": "aarav.sharma100@example.com",
        "phone": "9876500100",
        "grades": {
            "Maths": 88,
            "Science": 91,
            "English": 85,
            "Computer": 94,
            "Social Studies": 82
        },
        "attendance": {
            "Maths": 93,
            "Science": 95,
            "English": 90,
            "Computer": 96,
            "Social Studies": 92
        },
        "gpa": 8.80,
        "performance_risk": "Low"
    },
    "101": {
        "student_id": "101",
        "name": "Riya Mehta",
        "email": "riya.mehta101@example.com",
        "phone": "9876500101",
        "grades": {
            "Maths": 92,
            "Science": 89,
            "English": 90,
            "Computer": 96,
            "Social Studies": 88
        },
        "attendance": {
            "Maths": 97,
            "Science": 94,
            "English": 95,
            "Computer": 98,
            "Social Studies": 96
        },
        "gpa": 9.10,
        "performance_risk": "Low"
    },
    "102": {
        "student_id": "102",
        "name": "Kabir Verma",
        "email": "kabir.verma102@example.com",
        "phone": "9876500102",
        "grades": {
            "Maths": 76,
            "Science": 81,
            "English": 79,
            "Computer": 88,
            "Social Studies": 74
        },
        "attendance": {
            "Maths": 88,
            "Science": 85,
            "English": 82,
            "Computer": 90,
            "Social Studies": 84
        },
        "gpa": 7.96,
        "performance_risk": "Medium"
    },
    "103": {
        "student_id": "103",
        "name": "Ananya Singh",
        "email": "ananya.singh103@example.com",
        "phone": "9876500103",
        "grades": {
            "Maths": 95,
            "Science": 94,
            "English": 92,
            "Computer": 98,
            "Social Studies": 90
        },
        "attendance": {
            "Maths": 99,
            "Science": 98,
            "English": 97,
            "Computer": 99,
            "Social Studies": 98
        },
        "gpa": 9.38,
        "performance_risk": "Low"
    },
    "104": {
        "student_id": "104",
        "name": "Vihaan Kapoor",
        "email": "vihaan.kapoor104@example.com",
        "phone": "9876500104",
        "grades": {
            "Maths": 83,
            "Science": 87,
            "English": 80,
            "Computer": 90,
            "Social Studies": 79
        },
        "attendance": {
            "Maths": 91,
            "Science": 89,
            "English": 86,
            "Computer": 93,
            "Social Studies": 88
        },
        "gpa": 8.38,
        "performance_risk": "Low"
    },
    "105": {
        "student_id": "105",
        "name": "Sneha Patel",
        "email": "sneha.patel105@example.com",
        "phone": "9876500105",
        "grades": {
            "Maths": 89,
            "Science": 86,
            "English": 93,
            "Computer": 91,
            "Social Studies": 85
        },
        "attendance": {
            "Maths": 95,
            "Science": 92,
            "English": 96,
            "Computer": 97,
            "Social Studies": 94
        },
        "gpa": 8.88,
        "performance_risk": "Low"
    },
    "106": {
        "student_id": "106",
        "name": "Arjun Khanna",
        "email": "arjun.khanna106@example.com",
        "phone": "9876500106",
        "grades": {
            "Maths": 78,
            "Science": 82,
            "English": 75,
            "Computer": 85,
            "Social Studies": 71
        },
        "attendance": {
            "Maths": 84,
            "Science": 87,
            "English": 80,
            "Computer": 88,
            "Social Studies": 82
        },
        "gpa": 7.82,
        "performance_risk": "Medium"
    },
    "107": {
        "student_id": "107",
        "name": "Ishika Jain",
        "email": "ishika.jain107@example.com",
        "phone": "9876500107",
        "grades": {
            "Maths": 94,
            "Science": 90,
            "English": 96,
            "Computer": 97,
            "Social Studies": 92
        },
        "attendance": {
            "Maths": 98,
            "Science": 97,
            "English": 99,
            "Computer": 99,
            "Social Studies": 97
        },
        "gpa": 9.38,
        "performance_risk": "Low"
    },
    "108": {
        "student_id": "108",
        "name": "Manav Choudhary",
        "email": "manav.choudhary108@example.com",
        "phone": "9876500108",
        "grades": {
            "Maths": 71,
            "Science": 74,
            "English": 70,
            "Computer": 80,
            "Social Studies": 68
        },
        "attendance": {
            "Maths": 82,
            "Science": 80,
            "English": 78,
            "Computer": 85,
            "Social Studies": 79
        },
        "gpa": 7.26,
        "performance_risk": "High"
    },
    "109": {
        "student_id": "109",
        "name": "Prachi Desai",
        "email": "prachi.desai109@example.com",
        "phone": "9876500109",
        "grades": {
            "Maths": 90,
            "Science": 92,
            "English": 94,
            "Computer": 95,
            "Social Studies": 89
        },
        "attendance": {
            "Maths": 97,
            "Science": 96,
            "English": 98,
            "Computer": 99,
            "Social Studies": 95
        },
        "gpa": 9.20,
        "performance_risk": "Low"
    }
}

def calculate_gpa(student):
    """Calculate GPA based on grades"""
    grades = student.get('grades', {})
    if not grades:
        return 0.0
    
    total_marks = sum(grades.values())
    average_marks = total_marks / len(grades)
    return round(average_marks / 10, 2)

def calculate_performance_risk(student):
    """Calculate performance risk based on GPA"""
    gpa = student.get('gpa', 0)
    if gpa < 6.0:
        return "High"
    elif gpa < 8.0:
        return "Medium"
    else:
        return "Low"

# Routes
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# API Routes
@app.route('/api/students', methods=['GET'])
def get_students():
    try:
        students = list(student_data.values())
        print(f"✅ Loaded {len(students)} students")
        return jsonify(students)
    except Exception as e:
        print(f"❌ Error in /api/students: {e}")
        return jsonify([])

@app.route('/api/stats', methods=['GET'])
def get_stats():
    try:
        students = list(student_data.values())
        
        total_students = len(students)
        
        # Calculate average GPA
        avg_gpa = sum(student['gpa'] for student in students) / total_students
        
        # Count at-risk students
        at_risk = len([s for s in students if s['performance_risk'] == 'High'])
        
        # Calculate pass rate (GPA >= 5.0 is pass)
        pass_count = len([s for s in students if s['gpa'] >= 5.0])
        pass_rate = (pass_count / total_students * 100)
        
        stats = {
            'total_students': total_students,
            'avg_gpa': round(avg_gpa, 2),
            'at_risk': at_risk,
            'pass_rate': round(pass_rate, 2)
        }
        
        print(f"📊 Stats: {stats}")
        return jsonify(stats)
        
    except Exception as e:
        print(f"❌ Error in /api/stats: {e}")
        return jsonify({
            'total_students': 0,
            'avg_gpa': 0,
            'at_risk': 0,
            'pass_rate': 0
        })

@app.route('/api/students/add', methods=['POST'])
def add_student():
    try:
        data = request.json
        
        # Check if student exists
        if data['student_id'] in student_data:
            return jsonify({'success': False, 'error': 'Student ID already exists'})
        
        # Add new student
        student_data[data['student_id']] = {
            'student_id': data['student_id'],
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
            'grades': {},
            'attendance': {},
            'gpa': 0.0,
            'performance_risk': 'Low'
        }
        
        print(f"✅ Added student: {data['name']} ({data['student_id']})")
        return jsonify({'success': True})
            
    except Exception as e:
        print(f"❌ Error adding student: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        if student_id not in student_data:
            return jsonify({'success': False, 'error': 'Student not found'})
        
        deleted_student = student_data.pop(student_id)
        
        print(f"✅ Deleted student: {student_id}")
        return jsonify({'success': True})
            
    except Exception as e:
        print(f"❌ Error deleting student: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/students/<student_id>/grades', methods=['POST'])
def add_grade(student_id):
    try:
        data = request.json
        
        if student_id not in student_data:
            return jsonify({'success': False, 'error': 'Student not found'})
        
        student = student_data[student_id]
        student['grades'][data['subject']] = data['marks']
        
        # Recalculate GPA and performance risk
        student['gpa'] = calculate_gpa(student)
        student['performance_risk'] = calculate_performance_risk(student)
        
        print(f"✅ Added grade for {student_id}: {data['subject']} = {data['marks']}")
        return jsonify({'success': True})
            
    except Exception as e:
        print(f"❌ Error adding grade: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/students/<student_id>/grades/<subject>', methods=['DELETE'])
def remove_grade(student_id, subject):
    try:
        if student_id not in student_data:
            return jsonify({'success': False, 'error': 'Student not found'})
        
        student = student_data[student_id]
        
        if subject not in student['grades']:
            return jsonify({'success': False, 'error': 'Grade not found'})
        
        del student['grades'][subject]
        
        # Recalculate GPA and performance risk
        student['gpa'] = calculate_gpa(student)
        student['performance_risk'] = calculate_performance_risk(student)
        
        print(f"✅ Removed grade for {student_id}: {subject}")
        return jsonify({'success': True})
            
    except Exception as e:
        print(f"❌ Error removing grade: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/students/<student_id>/attendance', methods=['POST'])
def update_attendance(student_id):
    try:
        data = request.json
        
        if student_id not in student_data:
            return jsonify({'success': False, 'error': 'Student not found'})
        
        student = student_data[student_id]
        student['attendance'][data['subject']] = data['percentage']
        
        print(f"✅ Updated attendance for {student_id}: {data['subject']} = {data['percentage']}%")
        return jsonify({'success': True})
            
    except Exception as e:
        print(f"❌ Error updating attendance: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/ml/analysis', methods=['GET'])
def ml_analysis():
    try:
        students = list(student_data.values())
        
        # Basic ML analysis
        analysis = {
            'total_students': len(students),
            'average_gpa': round(sum(s['gpa'] for s in students) / len(students), 2),
            'at_risk_count': len([s for s in students if s['performance_risk'] == 'High']),
            'top_performer': max(students, key=lambda x: x['gpa'])['name'],
            'subject_averages': {
                'Maths': round(sum(s['grades'].get('Maths', 0) for s in students) / len(students), 1),
                'Science': round(sum(s['grades'].get('Science', 0) for s in students) / len(students), 1),
                'English': round(sum(s['grades'].get('English', 0) for s in students) / len(students), 1),
                'Computer': round(sum(s['grades'].get('Computer', 0) for s in students) / len(students), 1),
                'Social Studies': round(sum(s['grades'].get('Social Studies', 0) for s in students) / len(students), 1)
            }
        }
        
        return jsonify(analysis)
        
    except Exception as e:
        print(f"❌ Error in ML analysis: {e}")
        return jsonify({'error': 'ML analysis failed'})

if __name__ == '__main__':
    print("🚀 Starting Student Management System Frontend...")
    print("📍 Web Interface: http://localhost:5000")
    print("📊 API Server: http://localhost:5000/api/")
    print("🎯 Features: Dashboard, Students, Grades, Attendance, ML Analysis, Reports")
    print("👨‍🎓 Total Students: 10")
    print("✅ Server is running!")
    app.run(debug=True, port=5000)