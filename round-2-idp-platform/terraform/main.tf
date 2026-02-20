provider "aws" {
  region = var.aws_region
}

resource "aws_ecr_repository" "service" {
  name = var.service_name

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Service = var.service_name
    Team    = var.team_name
  }
}

resource "aws_iam_role" "service_role" {
  name = "${var.service_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "eks.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })

  tags = {
    Service = var.service_name
    Team    = var.team_name
  }
}
