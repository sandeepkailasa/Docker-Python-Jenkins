pipeline {
    agent any

    stages {
        stage('Sandeep: Build Docker Image') {
            steps {
                bat 'docker build -t python-docker-app .'
            }
        }

        stage('Sandeep: Run Docker Container') {
            steps {
                bat 'docker run --rm python-docker-app'
            }
        }

    }
}
