resource "null_resource" "start_minikube" {
    provisioner "local-exec" {
        command = "minikube start --driver=docker --cpus=${var.cpus} --memory=${var.memory} && kubectl config use-context minikube"
    }
}

resource "null_resource" "delete_minikube" {
    provisioner "local-exec" {
        command = "minikube delete"
        when    = destroy
    }
}