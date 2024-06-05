pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Load data') {
            steps {
                script {
                    def mlopsImage = docker.build('mlops')
                    mlopsImage.inside {
                        sh 'python3 ./load_data.py'
                    }
                }
            }
        }
        stage('Train') {
            steps {
                script {
                    def mlopsImage = docker.build('mlops')
                    mlopsImage.inside {
                        sh 'python3 ./model.py'
                    }
                }
            }
        }
    }
}
