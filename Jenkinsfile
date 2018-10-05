pipeline {
    stages {
        stage('build') {
            steps {
                sh """
                    docker build \\
                        -t acme/zoom.build \\
                        -f Dockerfile \\
                        --target build .
                """
            }
        }

        stage('lint') {
            steps {
                sh "docker build -t acme/zoom.lint -f Dockerfile --target lint ."
                sh "docker run acme/zoom.lint"
            }
        }

        stage('test') {
            steps {
                sh """
                    docker build \\
                        -t acme/zoom.test \\
                        -f Dockerfile \\
                        --target test .
                """
                sh 'docker run acme/zoom.test'
            }
        }

        stage('publish') {
            steps {
                sh """
                    docker build \\
                        -t joffrey/sample \\
                        -f Dockerfile \\
                        --target publish .
                """            }
        }

        stage('deploy') {
            steps {
                sh 'docker push docker.io/joffrey/sample'
            }
        }
    }
}
