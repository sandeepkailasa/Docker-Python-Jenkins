pipeline {
    agent any
	environment {
	    KUBECONFIG = 'C:\\Users\\Sandeep\\.kube\\config'
	}
    stages {
        stage('Sandeep: Build Docker Image') {
            steps {
                bat 'docker build -t python-docker-app .'
            }
        }
        /*
        stage('Sandeep: Run Docker Container') {
            steps {
                bat 'docker run --rm python-docker-app'
            }
        }
	*/
	stage('Sandeep : Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/deployment.yaml'
            }
        }
	stage('Sandeep: Verifying  Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl logs -l app=python-app'
            }
        }

    }
}
