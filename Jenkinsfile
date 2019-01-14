pipeline {
  agent any
  stages {
    stage('Build') {
      agent {
        docker {
          image 'flaskwebapp_flask-app'
        }

      }
      steps {
        echo 'Build Stage'
      }
    }
    stage('Test') {
      steps {
        echo 'Test Stage'
      }
    }
    stage('Deploy QA') {
      when {
        branch 'qa'
      }
      steps {
        echo 'Deploy QA'
      }
    }
    stage('Deploy Prod') {
      when {
        branch 'prod'
      }
      steps {
        echo 'Deploy Prod'
      }
    }
  }
}