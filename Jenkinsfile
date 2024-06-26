pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo Building...'
                sh 'docker build -t omritz243/worldofgames:1.0 .'
                sh 'docker images omritz243/worldofgames:1.0'
            }
        }
        stage('Run') {
            steps {
                sh 'echo Running...'
                sh 'docker run --name worldofgames -d --rm --publish 8777:8777 --env FLASK_APP=WorldOfGames --env FLASK_RUN_HOST=0.0.0.0 --env FLASK_RUN_PORT=8777 omritz243/worldofgames:1.0'
                sh 'docker ps -a'
            }
        }
        stage('Test') {
            steps {
                script {
                    sh "docker exec -i worldofgames sh -c 'python3 WorldOfGames/e2e.py'"
                }
            }
        }
        stage('Finalize') {
            environment {
                DOCKER_TOKEN = 'dckr_pat_n0cmLcQOE42phkP2_FJppAJHa2Q'
            }
            steps {
                sh 'echo Finalizing...'
                sh 'docker login -u omritz243 -p $DOCKER_TOKEN'
                sh 'docker push omritz243/worldofgames:1.0'
            }
        }
        stage('Clear') {
            steps {
                sh 'echo Clearing...'
                sh 'docker stop worldofgames'
                sh 'docker rmi omritz243/worldofgames:1.0'
            }
        }
    }
}
