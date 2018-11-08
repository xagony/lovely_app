pipeline {
  environment {
    registry = "ipoder2007/lovely"
    registryCredential = 'dockerhub'
  }
    agent any
    stages {
        stage('Build Image') {
            steps {
                script {
                    docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image(registry + ":$BUILD_NUMBER").Run() {
                        sh 'cd /code & python manage.py test'
                    }  
                }
            }
        }
        stage('Pull image') {
            steps {
                script {
                    docker.withRegistry( ‘’, registryCredential ) {
                      dockerImage.push()
                    }
                }
            }
        }
    }
}
