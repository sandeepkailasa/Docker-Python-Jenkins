pipeline {
    agent any

    stages {
        stage('Sandeep: Build Docker Image') {
            steps {
                sh 'docker build -t python-docker-app .'
            }
        }

        stage('Sandeep: Run Docker Container') {
            steps {
                sh 'docker run --rm python-docker-app'
            }
        }

    }
}
