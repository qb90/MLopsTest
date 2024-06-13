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
                    docker.image('korzepadawid/mlops:latest').inside {
                        sh 'python3 ./load_data.py'
                        archiveArtifacts artifacts: 'data.zip', onlyIfSuccessful: true
                    }
                }
            }
        }
        stage('Train') {
            steps {
                script {
                    def dockerVersion = sh(returnStdout: true, script: 'docker --version')
                    echo "Output: ${dockerVersion}"
                    docker.image('korzepadawid/mlops:latest').inside {
                        sh 'python ./model.py'
                        sh 'python ./predict.py'
                        archiveArtifacts artifacts: 'ner_model.zip, tokenizer.zip', onlyIfSuccessful: true
                    }
                }
            }
        }
    }
}
