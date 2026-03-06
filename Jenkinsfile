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
                bat 'python add.py'
            }
        }

    }
}
