pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull the source code from the repository
                git 'https://github.com/yourusername/your-repo.git'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                script {
                    docker.build('my-django-app')
                }
            }
        }

        stage('Test') {
            steps {
                // Run the tests inside the Docker container
                script {
                    docker.image('my-django-app').inside {
                        sh 'pytest'
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive test results and reports
            junit 'test-results.xml'
        }
    }
}
