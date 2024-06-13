pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                checkout scm
            }
        }
        stage("Download image") {
            steps {
                docker.pull('korzepadawid/mlops:latest')
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
                        archiveArtifacts artifacts: 'ner_model.zip, tokenizer.zip', onlyIfSuccessful: true
                    }
                }
            }
        }
    }
}
