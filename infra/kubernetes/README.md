# Kubernetes with Minikube

### Install
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

### Build
Pay attention to the amount of CPU and memory that your computer can make available for Minikube and change the variables in the `variables.tf` file before running the commands below.
~~~sh
terraform init
terraform apply
~~~