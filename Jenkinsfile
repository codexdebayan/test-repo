pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                script{
                    docker.build('todo')
                }
            }
        }
        
        stage('Test'){
            steps{
                script{
                    def path = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    sh "docker run -v ${path}:${path} -w ${path} todo pytest test_app.py"
                }
            }
        }
        stage('Deploy'){
            steps{
                timeout(time: 2, unit: 'MINUTES') {
                    script{
                        def path = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                        sh "docker run -d -v ${path}:${path} -w ${path} todo python app.py"
                    }
                }
            }
        }
    }

    post{
        success{
            echo "Depoyed Scccessfully !"
        }

        failure{
            echo "Failed Deplyment"
        }
    }
}
