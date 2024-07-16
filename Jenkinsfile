pipeline {
    agent any  // Runs on any available agent

    environment {
        REPO_URL = 'https://github.com/a3s0h/python_django_testing.git'  
        DOCKER_IMAGE = 'python_django_testing_image' 
        WORKSPACE_DIR = "${C:\ProgramData\Jenkins\.jenkins\workspace\testPipeline}\@tmp" 
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
                        sh 'pytest --junitxml=${WORKSPACE_DIR}/test-results.xml'  
                    }
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit '${WORKSPACE_DIR}/test-results.xml'  
            }
        }
    }

    post {
        always {
            cleanWs()  
        }
    }
}
