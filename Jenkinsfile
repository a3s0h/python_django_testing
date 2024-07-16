pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/a3s0h/python_django_testing.git'
        DOCKER_IMAGE = 'python_django_testing_image'
        DOCKER_CREDENTIALS = 'docker_credentials'  // Replace with your actual Docker credentials ID
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: "${env.REPO_URL}", branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}", ".")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.withRegistry('', "${env.DOCKER_CREDENTIALS}") {
                        docker.image("${env.DOCKER_IMAGE}").inside {
                            // Ensure the correct paths and environment for Windows
                            bat 'docker run -v "%cd%":/workspace -w /workspace ${DOCKER_IMAGE} pytest'
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
