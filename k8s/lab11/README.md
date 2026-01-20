# Lab Overview
# this lab covers the creation of a dedicated Namespace and the implementation of a Resource Quota.
# Resource Quotas ensure that no single team or project consume more than their allocated share of the cluster by limiting the total number of objects (like pods) that can exit within a specific namespace.

# Objectives
# 1. Create a logically isolated environment using a Namespace named ivolve.
# 2. Enforce a hard limit on the total number of Pods allowed in that namespace (max: 2).
# 3. Verify that the quota correctly rejects any Pods created byond the limit.

# Lab Instractions
# 1. Create a namespace called ivolve.
#   - redirect the output to  a yml file contains the instraction 
#   $ kubectl create namespace ivolve --dry-run=client -o yaml >  create-ivolve-namespace.yaml
#   $ kubectl apply -f create-ivolve-namespace.yaml
# 2. apply resource quota to limit pods number to only 2 pods within the namespace.
