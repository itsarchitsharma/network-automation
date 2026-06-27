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

module "vpc" {
  source      = "./modules/vpc"
  cidr_block  = var.vpc_cidr
  name        = "network-automation-vpc"
  environment = var.environment
}

module "public_subnet" {
  source            = "./modules/subnet"
  vpc_id            = module.vpc.vpc_id
  cidr_block        = var.public_subnet_cidr
  availability_zone = "${var.aws_region}a"
  name              = "public-subnet"
  environment       = var.environment
}

module "private_subnet" {
  source            = "./modules/subnet"
  vpc_id            = module.vpc.vpc_id
  cidr_block        = var.private_subnet_cidr
  availability_zone = "${var.aws_region}b"
  name              = "private-subnet"
  environment       = var.environment
}

module "igw" {
  source      = "./modules/igw"
  vpc_id      = module.vpc.vpc_id
  name        = "network-automation-igw"
  environment = var.environment
}

module "public_route_table" {
  source      = "./modules/route_table"
  vpc_id      = module.vpc.vpc_id
  subnet_id   = module.public_subnet.subnet_id
  igw_id      = module.igw.igw_id
  is_public   = true
  name        = "public-route-table"
  environment = var.environment
}

module "private_route_table" {
  source      = "./modules/route_table"
  vpc_id      = module.vpc.vpc_id
  subnet_id   = module.private_subnet.subnet_id
  is_public   = false
  name        = "private-route-table"
  environment = var.environment
}

module "security_group" {
  source      = "./modules/security_group"
  vpc_id      = module.vpc.vpc_id
  name        = "network-automation-sg"
  description = "Allow SSH inbound"
  environment = var.environment
}