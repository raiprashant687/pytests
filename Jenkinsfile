pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls your latest code from the GitHub repository configuration
                checkout scm
            }
        }

        stage('Setup Environment & Dependencies') {
            steps {
                echo 'Creating Python Virtual Environment...'
                // Best practice: Use a virtualenv inside the container to avoid permission conflicts
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; else pip install pytest requests;fi 
                '''
            }
        }

        stage('Execute Pytest Suite') {
            steps {
                echo 'Running Pytest tests...'
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=results.xml
                '''
            }
        }
    }
    
    post {
        always {
            // Parses the results.xml file to build pass/fail trend graphs on your Jenkins dashboard
            junit 'results.xml'
        }
    }
}
