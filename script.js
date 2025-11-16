// Navigation fix - Add this at the beginning of script.js
function showTab(tabName, event) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked button
    if (event && event.target) {
        event.target.classList.add('active');
    }
    
    // Load data for specific tabs
    switch(tabName) {
        case 'dashboard':
            loadDashboard();
            break;
        case 'students':
            loadAllStudents();
            break;
        case 'ml-analysis':
            loadMLAnalysis();
            break;
        case 'reports':
            loadReports();
            break;
    }
}

// Update all navigation buttons in index.html
// Replace onclick="showTab('dashboard')" with onclick="showTab('dashboard', event)"// Student Data - Your 10 students with exact details
const studentData = [
    {
        student_id: "100",
        name: "Aarav Sharma",
        email: "aarav.sharma100@example.com",
        phone: "9876500100",
        grades: {
            "Maths": 88,
            "Science": 91,
            "English": 85,
            "Computer": 94,
            "Social Studies": 82
        },
        attendance: {
            "Maths": 93,
            "Science": 95,
            "English": 90,
            "Computer": 96,
            "Social Studies": 92
        },
        gpa: 8.80,
        performance_risk: "Low"
    },
    {
        student_id: "101",
        name: "Riya Mehta",
        email: "riya.mehta101@example.com",
        phone: "9876500101",
        grades: {
            "Maths": 92,
            "Science": 89,
            "English": 90,
            "Computer": 96,
            "Social Studies": 88
        },
        attendance: {
            "Maths": 97,
            "Science": 94,
            "English": 95,
            "Computer": 98,
            "Social Studies": 96
        },
        gpa: 9.10,
        performance_risk: "Low"
    },
    {
        student_id: "102",
        name: "Kabir Verma",
        email: "kabir.verma102@example.com",
        phone: "9876500102",
        grades: {
            "Maths": 76,
            "Science": 81,
            "English": 79,
            "Computer": 88,
            "Social Studies": 74
        },
        attendance: {
            "Maths": 88,
            "Science": 85,
            "English": 82,
            "Computer": 90,
            "Social Studies": 84
        },
        gpa: 7.96,
        performance_risk: "Medium"
    },
    {
        student_id: "103",
        name: "Ananya Singh",
        email: "ananya.singh103@example.com",
        phone: "9876500103",
        grades: {
            "Maths": 95,
            "Science": 94,
            "English": 92,
            "Computer": 98,
            "Social Studies": 90
        },
        attendance: {
            "Maths": 99,
            "Science": 98,
            "English": 97,
            "Computer": 99,
            "Social Studies": 98
        },
        gpa: 9.38,
        performance_risk: "Low"
    },
    {
        student_id: "104",
        name: "Vihaan Kapoor",
        email: "vihaan.kapoor104@example.com",
        phone: "9876500104",
        grades: {
            "Maths": 83,
            "Science": 87,
            "English": 80,
            "Computer": 90,
            "Social Studies": 79
        },
        attendance: {
            "Maths": 91,
            "Science": 89,
            "English": 86,
            "Computer": 93,
            "Social Studies": 88
        },
        gpa: 8.38,
        performance_risk: "Low"
    },
    {
        student_id: "105",
        name: "Sneha Patel",
        email: "sneha.patel105@example.com",
        phone: "9876500105",
        grades: {
            "Maths": 89,
            "Science": 86,
            "English": 93,
            "Computer": 91,
            "Social Studies": 85
        },
        attendance: {
            "Maths": 95,
            "Science": 92,
            "English": 96,
            "Computer": 97,
            "Social Studies": 94
        },
        gpa: 8.88,
        performance_risk: "Low"
    },
    {
        student_id: "106",
        name: "Arjun Khanna",
        email: "arjun.khanna106@example.com",
        phone: "9876500106",
        grades: {
            "Maths": 78,
            "Science": 82,
            "English": 75,
            "Computer": 85,
            "Social Studies": 71
        },
        attendance: {
            "Maths": 84,
            "Science": 87,
            "English": 80,
            "Computer": 88,
            "Social Studies": 82
        },
        gpa: 7.82,
        performance_risk: "Medium"
    },
    {
        student_id: "107",
        name: "Ishika Jain",
        email: "ishika.jain107@example.com",
        phone: "9876500107",
        grades: {
            "Maths": 94,
            "Science": 90,
            "English": 96,
            "Computer": 97,
            "Social Studies": 92
        },
        attendance: {
            "Maths": 98,
            "Science": 97,
            "English": 99,
            "Computer": 99,
            "Social Studies": 97
        },
        gpa: 9.38,
        performance_risk: "Low"
    },
    {
        student_id: "108",
        name: "Manav Choudhary",
        email: "manav.choudhary108@example.com",
        phone: "9876500108",
        grades: {
            "Maths": 71,
            "Science": 74,
            "English": 70,
            "Computer": 80,
            "Social Studies": 68
        },
        attendance: {
            "Maths": 82,
            "Science": 80,
            "English": 78,
            "Computer": 85,
            "Social Studies": 79
        },
        gpa: 7.26,
        performance_risk: "High"
    },
    {
        student_id: "109",
        name: "Prachi Desai",
        email: "prachi.desai109@example.com",
        phone: "9876500109",
        grades: {
            "Maths": 90,
            "Science": 92,
            "English": 94,
            "Computer": 95,
            "Social Studies": 89
        },
        attendance: {
            "Maths": 97,
            "Science": 96,
            "English": 98,
            "Computer": 99,
            "Social Studies": 95
        },
        gpa: 9.20,
        performance_risk: "Low"
    }
];

// Global variables
let allStudents = studentData;
let currentStudentForGrades = null;
let currentStudentForAttendance = null;

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    console.log("🎓 Student Management System Started");
    loadAllStudents();
    setupEventListeners();
});

function setupEventListeners() {
    // Add student form
    document.getElementById('add-student-form').addEventListener('submit', function(e) {
        e.preventDefault();
        addStudent();
    });
}

// Tab navigation
function showTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
    
    // Load data for specific tabs
    switch(tabName) {
        case 'students':
            loadAllStudents();
            break;
        case 'ml-analysis':
            loadMLAnalysis();
            break;
        case 'reports':
            loadReports();
            break;
    }
}

// Load all students
function loadAllStudents() {
    displayAllStudents(allStudents);
}

function displayAllStudents(students) {
    const tbody = document.getElementById('students-table-body');
    
    if (students.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7">No students found.</td></tr>';
        return;
    }
    
    let html = '';
    students.forEach(student => {
        const riskClass = `risk-${student.performance_risk.toLowerCase()}`;
        html += `
            <tr>
                <td>${student.student_id}</td>
                <td>${student.name}</td>
                <td>${student.email}</td>
                <td>${student.phone}</td>
                <td>${student.gpa.toFixed(2)}</td>
                <td><span class="${riskClass}">${student.performance_risk}</span></td>
                <td>
                    <button class="btn btn-primary" onclick="viewStudent('${student.student_id}')">
                        <i class="fas fa-eye"></i> View
                    </button>
                    <button class="btn btn-danger" onclick="deleteStudent('${student.student_id}')">
                        <i class="fas fa-trash"></i> Delete
                    </button>
                </td>
            </tr>
        `;
    });
    
    tbody.innerHTML = html;
}

// Search functionality
function searchStudents() {
    const searchTerm = document.getElementById('search-input').value.toLowerCase();
    const rows = document.querySelectorAll('#students-table-body tr');
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(searchTerm) ? '' : 'none';
    });
}

// View student details
function viewStudent(studentId) {
    const student = allStudents.find(s => s.student_id === studentId);
    if (student) {
        let message = `STUDENT DETAILS:\n\n`;
        message += `ID: ${student.student_id}\n`;
        message += `Name: ${student.name}\n`;
        message += `Email: ${student.email}\n`;
        message += `Phone: ${student.phone}\n`;
        message += `GPA: ${student.gpa.toFixed(2)}\n`;
        message += `Risk Level: ${student.performance_risk}\n\n`;
        
        message += `GRADES:\n`;
        for (const [subject, marks] of Object.entries(student.grades)) {
            message += `• ${subject}: ${marks}/100\n`;
        }
        
        message += `\nATTENDANCE:\n`;
        for (const [subject, attendance] of Object.entries(student.attendance)) {
            message += `• ${subject}: ${attendance}%\n`;
        }
        
        alert(message);
    }
}

// Add new student
function addStudent() {
    const studentData = {
        student_id: document.getElementById('student-id').value,
        name: document.getElementById('student-name').value,
        email: document.getElementById('student-email').value,
        phone: document.getElementById('student-phone').value
    };
    
    // Validation
    if (!studentData.student_id || !studentData.name || !studentData.email || !studentData.phone) {
        alert('Please fill all required fields!');
        return;
    }
    
    // Check if student ID already exists
    if (allStudents.find(s => s.student_id === studentData.student_id)) {
        alert('Student ID already exists!');
        return;
    }
    
    // Add new student with default values
    const newStudent = {
        ...studentData,
        grades: {},
        attendance: {},
        gpa: 0.0,
        performance_risk: "Low"
    };
    
    allStudents.push(newStudent);
    alert(`Student ${studentData.name} added successfully!`);
    document.getElementById('add-student-form').reset();
    loadAllStudents();
    showTab('students');
}

// Delete student
function deleteStudent(studentId) {
    if (confirm(`Are you sure you want to delete student ${studentId}?`)) {
        allStudents = allStudents.filter(s => s.student_id !== studentId);
        alert('Student deleted successfully!');
        loadAllStudents();
    }
}

// Grades Management
function loadStudentForGrades() {
    const studentId = document.getElementById('grade-student-id').value;
    if (!studentId) {
        alert('Please enter a student ID');
        return;
    }

    const student = allStudents.find(s => s.student_id === studentId);
    
    if (student) {
        currentStudentForGrades = student;
        document.getElementById('student-grades-name').textContent = `Student: ${student.name}`;
        document.getElementById('grades-content').style.display = 'block';
        displayCurrentGrades(student.grades);
    } else {
        alert('Student not found!');
    }
}

function displayCurrentGrades(grades) {
    const container = document.getElementById('current-grades');
    
    if (Object.keys(grades).length === 0) {
        container.innerHTML = '<p>No grades added yet.</p>';
        return;
    }
    
    let html = '<h5>Current Grades:</h5><table class="students-table"><thead><tr><th>Subject</th><th>Marks</th><th>Grade</th><th>Action</th></tr></thead><tbody>';
    
    for (const [subject, marks] of Object.entries(grades)) {
        const grade = getGradeLetter(marks);
        html += `
            <tr>
                <td>${subject}</td>
                <td>${marks}/100</td>
                <td>${grade}</td>
                <td>
                    <button class="btn btn-danger" onclick="removeGrade('${subject}')">
                        <i class="fas fa-trash"></i> Remove
                    </button>
                </td>
            </tr>
        `;
    }
    
    html += '</tbody></table>';
    container.innerHTML = html;
}

function addGrade() {
    if (!currentStudentForGrades) {
        alert('Please load a student first');
        return;
    }
    
    const subject = document.getElementById('grade-subject').value;
    const marks = parseInt(document.getElementById('grade-marks').value);
    
    if (!subject || isNaN(marks)) {
        alert('Please enter both subject and marks');
        return;
    }
    
    if (marks < 0 || marks > 100) {
        alert('Marks must be between 0 and 100');
        return;
    }
    
    // Update student grades
    currentStudentForGrades.grades[subject] = marks;
    
    // Recalculate GPA
    calculateGPA(currentStudentForGrades);
    
    alert('Grade added successfully!');
    document.getElementById('grade-marks').value = '';
    displayCurrentGrades(currentStudentForGrades.grades);
    loadAllStudents();
}

function removeGrade(subject) {
    if (confirm(`Remove grade for ${subject}?`)) {
        delete currentStudentForGrades.grades[subject];
        calculateGPA(currentStudentForGrades);
        alert('Grade removed successfully!');
        displayCurrentGrades(currentStudentForGrades.grades);
        loadAllStudents();
    }
}

// Attendance Management
function loadStudentForAttendance() {
    const studentId = document.getElementById('attendance-student-id').value;
    if (!studentId) {
        alert('Please enter a student ID');
        return;
    }

    const student = allStudents.find(s => s.student_id === studentId);
    
    if (student) {
        currentStudentForAttendance = student;
        document.getElementById('student-attendance-name').textContent = `Student: ${student.name}`;
        document.getElementById('attendance-content').style.display = 'block';
        displayAttendanceDetails(student.attendance);
    } else {
        alert('Student not found!');
    }
}

function displayAttendanceDetails(attendance) {
    const container = document.getElementById('attendance-details');
    
    if (Object.keys(attendance).length === 0) {
        container.innerHTML = '<p>No attendance records yet.</p>';
        return;
    }
    
    let html = '<table class="students-table"><thead><tr><th>Subject</th><th>Attendance</th><th>Status</th></tr></thead><tbody>';
    
    for (const [subject, percentage] of Object.entries(attendance)) {
        const status = percentage >= 75 ? 'Good' : percentage >= 60 ? 'Average' : 'Poor';
        const statusClass = percentage >= 75 ? 'risk-low' : percentage >= 60 ? 'risk-medium' : 'risk-high';
        html += `
            <tr>
                <td>${subject}</td>
                <td>${percentage}%</td>
                <td><span class="${statusClass}">${status}</span></td>
            </tr>
        `;
    }
    
    html += '</tbody></table>';
    container.innerHTML = html;
}

function updateAttendance() {
    if (!currentStudentForAttendance) {
        alert('Please load a student first');
        return;
    }
    
    const subject = document.getElementById('attendance-subject').value;
    const percentage = parseInt(document.getElementById('attendance-percentage').value);
    
    if (!subject || isNaN(percentage)) {
        alert('Please enter both subject and percentage');
        return;
    }
    
    if (percentage < 0 || percentage > 100) {
        alert('Percentage must be between 0 and 100');
        return;
    }
    
    // Update attendance
    currentStudentForAttendance.attendance[subject] = percentage;
    
    alert('Attendance updated successfully!');
    document.getElementById('attendance-percentage').value = '';
    displayAttendanceDetails(currentStudentForAttendance.attendance);
}

// ML Analysis
function loadMLAnalysis() {
    // Data is already hardcoded in HTML
    console.log("ML Analysis loaded");
}

// Reports
function loadReports() {
    // Data is already hardcoded in HTML
    console.log("Reports loaded");
}

function generateReport() {
    let report = "STUDENT GRADE MANAGEMENT SYSTEM - ACADEMIC REPORT\n";
    report += "Generated on: " + new Date().toLocaleDateString() + "\n\n";
    
    report += "CLASS SUMMARY:\n";
    report += "Total Students: " + allStudents.length + "\n";
    report += "Average GPA: " + (allStudents.reduce((sum, s) => sum + s.gpa, 0) / allStudents.length).toFixed(2) + "\n";
    report += "Pass Rate: 100%\n\n";
    
    report += "STUDENT DETAILS:\n";
    report += "=".repeat(50) + "\n";
    
    allStudents.forEach(student => {
        report += `ID: ${student.student_id} | Name: ${student.name} | GPA: ${student.gpa.toFixed(2)} | Risk: ${student.performance_risk}\n`;
        report += "Grades: ";
        for (const [subject, marks] of Object.entries(student.grades)) {
            report += `${subject}: ${marks} `;
        }
        report += "\nAttendance: ";
        for (const [subject, attendance] of Object.entries(student.attendance)) {
            report += `${subject}: ${attendance}% `;
        }
        report += "\n" + "-".repeat(50) + "\n";
    });
    
    // Create download link
    const blob = new Blob([report], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'student_report.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    alert('Report generated and downloaded successfully!');
}

// Utility functions
function calculateGPA(student) {
    const grades = Object.values(student.grades);
    if (grades.length === 0) {
        student.gpa = 0.0;
        student.performance_risk = "Low";
        return;
    }
    
    const averageMarks = grades.reduce((sum, mark) => sum + mark, 0) / grades.length;
    student.gpa = (averageMarks / 10);
    
    // Update performance risk
    if (averageMarks < 40) {
        student.performance_risk = "High";
    } else if (averageMarks < 60) {
        student.performance_risk = "Medium";
    } else {
        student.performance_risk = "Low";
    }
}

function getGradeLetter(marks) {
    if (marks >= 90) return 'A+';
    if (marks >= 80) return 'A';
    if (marks >= 70) return 'B';
    if (marks >= 60) return 'C';
    if (marks >= 50) return 'D';
    return 'F';
}

// Export functions for global access
window.showTab = showTab;
window.viewStudent = viewStudent;
window.deleteStudent = deleteStudent;
window.searchStudents = searchStudents;
window.loadStudentForGrades = loadStudentForGrades;
window.addGrade = addGrade;
window.removeGrade = removeGrade;
window.loadStudentForAttendance = loadStudentForAttendance;
window.updateAttendance = updateAttendance;
window.generateReport = generateReport;