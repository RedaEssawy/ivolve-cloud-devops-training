# Lab Overview 
# This lab demonstrates the best practices for managing environment-specific configurations and sensitive data in Kubernetes. By using ConfigMaps for non-sensitive data (like hostnames) and Secrets for sensitive data (like passwords), you can maintain a more secure and flexible infrastructure. 

# Objectives
# Create a ConfigMap for MySQL connection parameters.
# Create a Secret containing base64-encoded administrative and user passwords.
# Prepare the environment for a MySQL StatefulSet deployment.

# Lab Instructions
# 1. Define the ConfigMap
#      Redirect the output of the command to a file and then apply it 
#      $  kubectl create  configmap non-sensitive-env --from-literal=DB_HOST=dbhost --from-literal=DB_USER=dbuser --dry-run=client -o yaml > non-sensitive-env.yaml
#      $ Create the configMap using the file
#      $ kubectl apply -f non-sensitive-env.yaml
# 2. Define the Secret
#       Redirect the output of the command to a file and then apply it
#       $ kubectl create  secret generic  sensitive-var --from-literal=DB_HOST=dbhost --from-literal=DB_USER=dbuser --dry-run=client -o yaml > sensitive-var.yaml
#      create the Secret using the file
#       $ kubectl apply -f sensitive-var.yaml
