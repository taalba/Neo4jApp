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
        mail(subject: 'Deploy to prod', body: 'Would you like to deploy to prod', from: 'admin@jenkins.com', to: 'ytaalba@bluebeesoftware.com')
        input 'Confirm delpoy'
      }
    }
  }
}