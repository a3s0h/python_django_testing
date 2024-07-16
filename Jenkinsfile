pipeline {
    agent any

    environment {
        // Define any environment variables you might need
        REPO_URL = 'https://github.com/a3s0h/python_django_testing.git'
        DOCKER_IMAGE = 'python_django_testing_image'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").inside {
                        sh 'pip install -r requirements.txt'
                        sh 'pytest --junitxml=test-results.xml'
                    }
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after the build
        }
    }
}
