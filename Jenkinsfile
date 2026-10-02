```groovy
pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Student Attendance Management System'
                bat 'python --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                bat 'python -m unittest test_attendance.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Student Attendance System deployment completed'
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESSFUL'
        }

        failure {
            echo 'BUILD FAILED'
        }
    }
}
```

