#!/usr/bin/env bash

echo "creating new namespaces..."
kubectl apply -f namespaces

echo "setting up jenkins..."
helm repo add jenkins https://charts.jenkins.io || \
    helm repo update && \
    helm install jenkins jenkins/jenkins -n jenkins

echo "Use the command bellow to get an initial password"
echo "kubectl exec --namespace jenkins -it svc/jenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo"
echo "It might take a while, before a Jenkins container will be accessible..."