pipeline {
    agent any
    environment {
        REPO_URL = 'https://github.com/a3s0h/python_django_testing.git'
        DOCKER_IMAGE = 'python_django_testing_image'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: "${REPO_URL}", branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("${DOCKER_IMAGE}", '.')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.withRegistry('', '') {
                        docker.image("${env.DOCKER_IMAGE}").inside {
                            sh 'pwd'
                            sh 'pytest'
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
