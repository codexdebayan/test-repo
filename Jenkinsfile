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
                    bat "docker run -v ${path}:${path} -w ${path} todo pytest test_app.py"
                }
            }
        }
        stage('Deploy'){
            steps{
                script{
                    def path = pwd().replaceAll('C:', '/c').replaceAll('\\\\', '/')
                    bat "docker run -v ${path}:${path} -w ${path} todo python app.py"
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
