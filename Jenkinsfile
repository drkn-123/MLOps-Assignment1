pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "drnk1/mlops-ass1" 
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/drkn-123/MLOps-Assignment1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'  // Build Docker image
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                    bat 'docker push %DOCKER_IMAGE%'  // Push Docker image
                }
            }
        }
    }
}
