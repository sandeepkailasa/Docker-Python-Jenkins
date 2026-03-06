pipeline {
    agent any

    stages {

        stage('Checkout Code Sandeep') {
            steps {
                git 'https://github.com/sandeepkailasa/GitProject'
            }
        }
        //This stage helps in running addition function on given inputs in input.csv
        stage('Sandeep Running Python Script') {
            steps {
                bat 'python add.py'
            }
        }

        //This stage helps in Detecting Duplicate Cells given in cells.csv
        stage('Sandeep we are Detecting Duplicate Cells') {
            steps {
                bat 'python duplicate_cells.py'
            }
        }

    }
}
