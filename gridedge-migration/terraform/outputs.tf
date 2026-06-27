output "nms_public_ip" {
  description = "Public IP of the GridEdge NMS server"
  value       = aws_eip.nms.public_ip
}

output "nms_instance_id" {
  description = "EC2 instance ID of the NMS server"
  value       = aws_instance.nms.id
}

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.gridedge.id
}