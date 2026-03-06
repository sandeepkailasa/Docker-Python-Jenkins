pipeline {
    agent any

    stages {

        stage('Checkout Code Sandeep') {
            steps {
                git 'https://github.com/sandeepkailasa/GitProject'
            }
        }

        stage('Sandeep Running Python Script') {
            steps {
                bat '"C:\\Users\\Sandeep\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" add.py'
            }
        }

    }
}
