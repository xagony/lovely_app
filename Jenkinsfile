pipeline {
  environment {
    registry = "ipoder2007/lovely"
    registryCredential = 'dockerhub'
  }
    agent any
    stages {
        stage('Build Image') {
            steps {
                node {
                    def customImage = docker.build(registry + ":$BUILD_NUMBER")

                    customImage.inside {
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
