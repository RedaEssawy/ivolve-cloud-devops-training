<!-- # Objective
Create a Jenkins pipeline that automates the complete CI/CD workflow for a Java application: build, test, containerize, push to registry, and deploy to Kubernetes.

# Concepts Covered
- Jenkins Pipeline (Declarative/ Scripted)
- Jenkinsfile structure
- Docker integration
- Kubernetes deployment
- Environment variables management
- Post-build actions

# Prerequisites
- Jenkins installed with necessary plugins:
    - Pipeline
    - Docker Pipeline
    - Kubernetes
    - Git
- Docker installed on Jenkins node
- kubectl configured on Jenkins node
- Docker Hub account (or private registry)
- Kubernetes cluster access
- Git repository with application code



# Steps

## Step 1: Clone Source Code and Prepare Environment
<pre>
```
# SSH into Jenkins server or use Jenkins node
git clone https://github.com/lbrahim-Adel15/Jenkins_App.git
cd Jenkins_App

# Examine the project structure
ls -la
# Should see: Dockerfile, pom.xml (or build.gradle), src/

# Check Dockerfile
cat Dockerfile
```
</pre>

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
touch Jenkinsfile
</pre>
 -->
