variable "vpc_id" {
  description = "ID of the VPC"
  type        = string
}

variable "name" {
  description = "Name of the security group"
  type        = string
}

variable "description" {
  description = "Description of the security group"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}