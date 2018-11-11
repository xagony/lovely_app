pipeline {

    agent { 
        dockerfile true 
    }


    stages {
        stage('test') {
            steps {
                echo 'Running app tests'
                sh 'cd /code & python manage.py test'
            }
        }
        stage('push') {
            steps {
                echo 'Pushing to docker hub'
            }
        }
    }
}
