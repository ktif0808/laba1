pipeline {
    agent any
    stages {
        stage ('Dependency Installation') {
            script {
                docker.image('python:3.9').inside {
                    sh 'pip install -r requirement.txt'
                }
            }
        }
        stage ('Build'){
            steps {
                echo "Start"
                echo "Doing"
                echo "End"  
            }
           
        }
        stage ('Test'){
            steps {
                echo "Start"
                echo "Doing"
                echo "End"  
            }
           
        }
        stage ('Deploy'){
            steps {
                echo "Start"
                echo "Doing"
                echo "End"  
            }
            sh "python --version"
            echo "End of stage"
           
        }
    }
}
