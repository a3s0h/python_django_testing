pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/a3s0h/python_django_testing.git'
        DOCKER_IMAGE = 'python_django_testing_image'
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
                    docker.withRegistry('') {
                        docker.image("${env.DOCKER_IMAGE}").inside {
                            bat 'pytest'
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
