terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC
resource "aws_vpc" "gridedge" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true

  tags = {
    Name        = "gridedge-vpc"
    Project     = "GridEdge Migration"
    ManagedBy   = "terraform"
  }
}

# Public Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.gridedge.id
  cidr_block              = var.public_subnet_cidr
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true

  tags = {
    Name      = "gridedge-public-subnet"
    ManagedBy = "terraform"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "gridedge" {
  vpc_id = aws_vpc.gridedge.id

  tags = {
    Name      = "gridedge-igw"
    ManagedBy = "terraform"
  }
}

# Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.gridedge.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gridedge.id
  }

  tags = {
    Name      = "gridedge-public-rt"
    ManagedBy = "terraform"
  }
}

# Route Table Association
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# Security Group — NMS Server
resource "aws_security_group" "nms" {
  name        = "gridedge-nms-sg"
  description = "GridEdge NMS Server"
  vpc_id      = aws_vpc.gridedge.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "SSH"
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "NMS Web Interface"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name      = "gridedge-nms-sg"
    ManagedBy = "terraform"
  }
}

# NMS Server EC2 Instance
resource "aws_instance" "nms" {
  ami                    = var.nms_ami
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.nms.id]

  tags = {
    Name      = "gridedge-nms-server"
    Role      = "NMS"
    Project   = "GridEdge Migration"
    ManagedBy = "terraform"
  }
}

# Elastic IP for NMS Server
resource "aws_eip" "nms" {
  instance = aws_instance.nms.id
  domain   = "vpc"

  tags = {
    Name      = "gridedge-nms-eip"
    ManagedBy = "terraform"
  }
}