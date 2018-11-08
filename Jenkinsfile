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
                    docker.exec registry + ":$BUILD_NUMBER" cd /code & python manage.py test'
                   
                }
            }
        }
        stage('Test') {
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
