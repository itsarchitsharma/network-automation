variable "vpc_id" {
  description = "ID of the VPC"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for the subnet"
  type        = string
}

variable "availability_zone" {
  description = "Availability zone"
  type        = string
}

variable "name" {
  description = "Name tag for the subnet"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}