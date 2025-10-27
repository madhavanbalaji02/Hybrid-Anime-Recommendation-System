pipeline {
    agent any


    stages{

        stage("Cloning from Github...."){
            steps{
                script{
                    echo 'Cloning from Github...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/madhavanbalaji02/Hybrid-Anime-Recommendation-System.git']])

                }
            }
        }
    }
} 