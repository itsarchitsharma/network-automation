resource "aws_route_table" "this" {
  vpc_id = var.vpc_id

  tags = {
    Name        = var.name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_route" "default" {
  count                  = var.is_public ? 1 : 0
  route_table_id         = aws_route_table.this.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = var.igw_id
}

resource "aws_route_table_association" "this" {
  subnet_id      = var.subnet_id
  route_table_id = aws_route_table.this.id
}