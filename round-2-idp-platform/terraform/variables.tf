variable "aws_region" {
  description = "AWS region to create resources"
  type        = string
  default     = "us-east-1"
}

variable "service_name" {
  description = "Name of the microservice"
  type        = string
}

variable "team_name" {
  description = "Owning team name"
  type        = string
}

variable "repo_url" {
  description = "Source code repository URL"
  type        = string
}
