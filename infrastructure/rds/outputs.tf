output "arn" {
    value = aws_db_instance.olympics_rds.arn
}

output "endpoint" {
    value = aws_db_instance.olympics_rds.endpoint
}

output "vpc_security_group_ids" {
    value = aws_db_instance.olympics_rds.vpc_security_group_ids
}