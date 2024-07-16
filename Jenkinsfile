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
        stage('Prepare Directory') {
            steps {
                script {
                    // Ensure the testProject directory is ready for use
                    bat 'mkdir workspace\\testPipeline'
                    // Move repository contents to testProject directory
                    bat 'move * workspace\\testPipeline\\'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}", "workspace/testPipeline")
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
