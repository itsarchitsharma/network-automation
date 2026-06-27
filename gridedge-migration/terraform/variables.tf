variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-southeast-2"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "Public subnet CIDR"
  type        = string
  default     = "10.0.1.0/24"
}

variable "instance_type" {
  description = "EC2 instance type for NMS server"
  type        = string
  default     = "t3.micro"
}

variable "nms_ami" {
  description = "AMI ID for NMS server — Amazon Linux 2023 ap-southeast-2"
  type        = string
  default     = "ami-0310483fb2b488153"
}