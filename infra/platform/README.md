# Platform Deployment

### Build
~~~sh
terraform init
terraform apply
~~~

### Fix External IP pending (Minikube)
~~~sh
minikube tunnel
~~~

### Expose Trino
~~~sh
POD_NAME=$(kubectl get pods -n trino -l 'app=trino,release=trino,component=coordinator' --field-selector=status.phase=Running -o jsonpath='{.items[0].metadata.name}')

kubectl port-forward $POD_NAME -n trino 8080:8080
~~~
Now you can connect to the Trino coordinator at http://localhost:8080, with trino user.

### Useful links
- [MinIO Operator Helm](https://min.io/docs/minio/kubernetes/upstream/operations/install-deploy-manage/deploy-operator-helm.html)
- [MinIO Tenant Helm](https://min.io/docs/minio/kubernetes/openshift/operations/install-deploy-manage/deploy-minio-tenant-helm.html)
- [Trino Helm](https://trino.io/docs/current/installation/kubernetes.html#creating-your-own-yaml)