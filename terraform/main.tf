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
  cidr_block        = "10.1.2.0/24"
  availability_zone = "${var.aws_region}b"
  name              = "private-subnet"
  environment       = var.environment
}