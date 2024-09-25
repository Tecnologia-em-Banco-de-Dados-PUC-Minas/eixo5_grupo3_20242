variable "cpus" {
    type        = number
    description = "Number of CPUs for Minikube"
    default     = 6
}

variable "memory" {
    type        = number
    description = "Memory (in MB) for Minikube"
    default     = 14336
}