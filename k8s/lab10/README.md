# Lab Overview
# This lab demonstrates how to control pod scheduling by implementing Node Taints. 
# Taints allow a node to repel a set of pods unless those have a matching "toleration" .
# This is a fundamental concept for node isolation, dedicated hardware allocation, and cluster maintainance.

# Objectives
# 1. Configure a Kubernetes cluster with at least two nodes.
# 2. Apply a NoSchedule taint to a specific worker node.
# 3. Verify the configureation using Kubernetes inspection command

# Prerquisites
# 1. A running Kubernetes cluster
# 2. kubectl command-line tool installed and configured to communicate with your cluster

# Lab Instractions
# 1. Run Kubernetes cluster with 2 nodes.
# $ minikube start --nodes=2

# 2. Taint one node with a specific key-value ‘node=worker’ and effect NoSchedule.
# $ kubectl taint node minikube node=wroker:NoSchedule

# 3. Describe all nodes to verify the taint.
# $ kubectl describe nodes minikube  | grep -i taint
# $ kubectl describe nodes minikube-m02 | grep -i taint