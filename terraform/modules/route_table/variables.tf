variable "vpc_id" {
  description = "ID of the VPC"
  type        = string
}

variable "subnet_id" {
  description = "ID of the subnet to associate"
  type        = string
}

variable "igw_id" {
  description = "ID of the Internet Gateway"
  type        = string
  default     = ""
}

variable "is_public" {
  description = "Whether this is a public route table"
  type        = bool
  default     = false
}

variable "name" {
  description = "Name tag"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}