pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'cd /code & python manage.py test'
            }
        }
    }
}
