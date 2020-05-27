# Kubectl cheatsheet

`export KUBECONFIG=~/.kube/someconfig`

`kubectl get secrets secretsname -o=yaml`

`kubectl logs --since=20m podname | grep "email"`

`kubectl exec -ti podname bash`

`kubectl describe pod podname`

`kubectl get deployment deploymentname`
