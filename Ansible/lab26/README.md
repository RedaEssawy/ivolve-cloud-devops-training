# Objective
Install and configure Ansible Automation Platform, set up SSH key-based authentication to managed nodes, and execute ad-hoc commands for basic system administration tasks.

# Concepts Covered
- Ansible architecture (control vs managed nodes)
- SSH key authentication
- Inventory file creation and management
- Ad-hoc command execution
- Ansible configuration files

# Prerequisites
- Two Linux machines (one control node, one managed node)
- Python 3.x installed on both nodes
- SSH server running on managed node
- sudo/root access on both nodes
- Network connectivity between nodes


# Steps

## Step 1: Install Ansible on Control Node
### As I use ubuntu 

```bash
sudo apt update
sudo apt install software-properties-common -y
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
# Verify installation
ansible --version
```

<!-- 
## Step 2: Install Required Jenkins Plugins

In Jenkins Web UI:

1. Go to **Manage Jenkins → Manage Plugins → Available**
2. Search and install:
    - **Pipeline**
    - **Docker Pipeline**
    - **Kubernetes CLI Plugin**
    - **GitHub Integration** (optional)
    - **Blue Ocean** (optional, for visualization)
3. Restart Jenkins if required


## Step 3: Configure Jenkins Credentials

Add credentials to Jenkins:

**Docker Hub Credentials:**

1. Go to **Manage Jenkins → Manage Credentials**
2. Click **Global credentials → Add Credentials**
3. Select **Username with password**
4. Enter:
    - Username: Your Docker Hub username
    - Password: Your Docker Hub password/token
    - ID: `docker-hub-creds`
    - Description: Docker Hub credentials

**Kubernetes kubeconfig:**

1. Add new credential of type Secret file
2. Upload your kubeconfig file
3. ID: `kubeconfig-file`

**GitHub Token (optional):**
1. Add GitHub personal access token
2. ID: `github-token`

## Step 4: Create Jenkins Pipeline Job

1. Go to Jenkins Dashboard → **New Item**
2. Enter name:`java-app-cicd-pipeline`
3. Select **Pipeline**
4. Click **OK**

## Step 5: Configure Pipeline

In the job configuration:

**General Tab:**

- Add description: "CI/CD Pipeline for Java Application"
- Check "GitHub project" and add project URL if using GitHub

**Build Triggers:**

- Select "GitHub hook trigger for GITScm polling" (for webhooks)
- Or "Poll SCM" with schedule: `H/5 * * * *` (every 5 minutes)

**Pipeline Definition:**

- Select **Pipeline script from SCM**
- SCM: **Git**
- Repository URL: `https://github.com/lbrahim-Adel15/Jenkins_App.git`
- Credentials: Add if repository is private
- Branch: `*/main` or `*/master`
- Script Path: `Jenkinsfile` (or create one)

## Step 6: Create Jenkinsfile

Create a `Jenkinsfile` in your repository root:

<pre>
Touch Jenkinsfile
</pre>
Put the following contents in it:
<pre>
pipeline{
    agent any

    environment {
        IMAGE_NAME="redaeid/kubernets-app_web-app"
        DEPLOYMENT_FILE="deployment.yaml"
    }

    stages {
        stage('Run Unit Tests') {
            steps {
                dir('ci-cd/lab22/Jenkins_App') {
                    sh 'mvn test'
                }
            }
        }
        stage('Build Application') {

            steps {
                dir('ci-cd/lab22/Jenkins_App') {
                sh 'mvn package'
            }
        }}
        stage('Build Docker Image') {
            steps {
                dir('ci-cd/lab22/Jenkins_App') {
                sh "docker build -t $IMAGE_NAME:$BUILD_NUMBER ."
            }
        }}
        
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerHub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh """
                      echo $DOCKERHUB_PASSWORD  | docker login -u '$DOCKERHUB_USERNAME' --password-stdin
                        docker push $IMAGE_NAME:$BUILD_NUMBER
                    """
                }
            }
        }
        stage('Delete Local Docker Image') {
            steps {
                sh "docker rmi $IMAGE_NAME:$BUILD_NUMBER || true"
            }
        }
        stage('Update Deployment File') {
            steps {
                dir('ci-cd/lab22/Jenkins_App') {
                sh """
                    sed -i 's|image: .*|image: $IMAGE_NAME:$BUILD_NUMBER|' $DEPLOYMENT_FILE
                """
            }}
        }
        stage('Deploy to Kubernetes') {
            
            steps {
                withCredentials([
                string(credentialsId: 'APIServer', variable: 'API_SERVER'),
                string(credentialsId: 'ServiceAccount-Token', variable: 'KUBE_TOKEN')

            ]){
            dir('ci-cd/lab22/Jenkins_App')
            {
                sh "kubectl apply -f $DEPLOYMENT_FILE --server=$API_SERVER --token=$KUBE_TOKEN --insecure-skip-tls-verify=true"
            }
        }
        }
        }
        
         
    }
    post {
        always {
            echo "Pipeline completed."
        }
        success{
            echo "Pipeline succeeded."
        }
        failure{
            echo "Pipeline failed."
        }
    }


}
</pre>

## Step 7: Create deployment.yaml File (Alternative)
<pre>
Touch deployment.yaml
</pre>
Put the following contents in it:
<pre>
<pre>
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: app-deployment
  name: app-deployment
  namespace: ivolve
spec:
  replicas: 1
  selector:
    matchLabels:
      app: app-deployment
  strategy: {}
  template:
    metadata:
      labels:
        app: app-deployment
    spec:
      containers:
      - image: redaeid/kubernets-app_web-app
        name: kubernets-app-web-app-gks5b
        ports:
        - containerPort: 80
          protocol: TCP
        imagePullPolicy: Always
        resources: {}
status: {}

</pre>

## Step 8: Run the Pipeline

1. Click Build Now on your pipeline job
2. Watch the pipeline progress in Blue Ocean or classic view
3. Check each stage output

![Alt Text](assets/images/successed-pipeline.png) -->