pipeline{
  agent any

  environment{
    AWS_CREDENTIALS_ID = 'aws-cred'
    DOCKER_CREDENTIALS_ID = 'dockerhub-cred'
    GITHUB_CREDENTIALS_ID = 'githubpat'
    KUBECONFIG_PATH = '/home/ubuntu/.kube/config'
    HELM_CHART_PATH = '/home/ubuntu/calci-chart'
  }
// I am using pipeline script from scm(source code management) option so no need of checkout stage that is cloning of repo. If u are directly writing pipeline script at the time of creation u need to clone the rep first.stage('Checkout Code') {
//steps {
                // Checkout code from GitHub
                //git credentialsId: env.GITHUB_CREDENTIALS_ID, url: 'https://github.com/your-repo-url.git'
            //}
        //}
  stages{
    stage('build docker image'){
      steps{
        sh 'docker build -t ajay302001/projectcalci:${BUILD_NUMBER} . ' // builds docker image, build_number is the tag a new tag will be assigned everytime when the image is built.
      }
    }
    stage('push docker image to dockerhub'){
      steps{
        withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsID: env.DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', usernamePassword: 'DOCKER_PASSWORD' ]]){
          sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
          sh 'docker push ajay302001/projectcalci:${BUILD_NUMBER}'
        }
      }  
    }
    stage('deploy the app to aws-eks'){
      steps{
        withCredentials([file(credentialsId: env.AWS_CREDENTIALS_ID, variable: 'AWS_CONFIG_FILE')]){
          sh """
          mkdir -p ~/.kube
          cp ${AWS_CONFIG_FILE} ~/.kube/config
          export KUBECONFIG=${env.KUBECONFIG_PATH}
          """
          sh "helm upgrade --install calci-chart --set image.tag=${BUILD_NUMBER} ${env.HELM_CHART_PATH}"
        }
      }
    }
  }
}
