pipeline {
  environment {
    registry = "ipoder2007/lovely"
    registryCredential = 'dockerhub'
  }
    stages {
        stage('Test') {
            steps {
                sh 'cd /code & python manage.py test'
            }
        }
        stage('Upload') {
            steps {
                script {
                    docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
    }
}
