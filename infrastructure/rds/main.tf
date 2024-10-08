resource "aws_security_group" "postgres_access" {
    name        = "allow_postgres_access"
    description = "Security group to allow postgres accesses"

    ingress {
        from_port   = 5432
        to_port     = 5432
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_db_instance" "olympics_rds" {
    db_name                = "olympics"
    engine                 = "postgres"
    engine_version         = "16.3"
    instance_class         = var.instance_class
    allocated_storage      = var.storage
    username               = var.db_username
    password               = var.db_password
    skip_final_snapshot    = true
    publicly_accessible    = true
    vpc_security_group_ids = [aws_security_group.postgres_access.id]
}