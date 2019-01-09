pipeline {
  agent any
  stages {
    stage('Build') {
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
                branch 'production'
      }
      steps {
        echo 'Deploy QA'
      }
    }
    stage('Deploy Prod') {
      when {
                branch 'production'
      }
      steps {
        echo 'Deploy Prod'
      }
    }
  }
}
