output "ecr_repository_url" {
  description = "ECR repository URL for the service"
  value       = aws_ecr_repository.service.repository_url
}

output "iam_role_arn" {
  description = "IAM role ARN assigned to the microservice"
  value       = aws_iam_role.service_role.arn
}
