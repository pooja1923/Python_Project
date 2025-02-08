pipeline {
    agent any

    stages {
        // Build Stage: Clones the repository and installs dependencies
        stage('Build') {
            steps {
                git 'https://github.com/pooja1923/Python_Project.git'  // Replace with your GitLab repository URL
                sh 'pip install -r requirements.txt'  // Install dependencies
            }
        }

        // Test Stage: Runs unit tests
        stage('Test') {
            steps {
                script {
                    try {
                        sh 'pytest tests/'  // Adjust to your test framework
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'  // Set build result to failure if tests fail
                        throw e  // Re-throw the exception to stop the pipeline
                    }
                }
            }
        }

        // Deploy Stage: Prints "Deployment Successful" if the tests pass
        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }  // Only run if previous stages succeed
            }
            steps {
                echo 'Deployment Successful'  // Placeholder for actual deployment logic
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'  // Prints if pipeline succeeds
        }
        failure {
            echo 'Pipeline failed.'  // Prints if pipeline fails
        }
    }
}
