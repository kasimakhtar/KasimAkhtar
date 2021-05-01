# Terraform script to build VPC and EC2 instance

Terraform is an infastructure provisioning tool that is cloud agnostic. It is an example of infastructure as a code (IaC), where you describe what your environment looks like, and then use the 'apply' command to execute. Manually building s cloud architecture can be time consuming, prone to error, and is not easily repeatable. Automation with IaC saves time and reduces human error.
&nbsp;
~~~
provider "aws" {
    region = "us-east-1"
}


resource "aws_vpc" "TerraformVPC" {
    cidr_block = "10.0.0.0/16"

    tags = {
        Name = "TerraformVPC"
    }
}


resource "aws_subnet" "Public_Subnet" {
    vpc_id = aws_vpc.TerraformVPC.id
    cidr_block = "10.0.1.0/24"

    tags = {
        Name = "Public Subnet"
    }
}

resource "aws_internet_gateway" "TerraformIGW" {
    vpc_id = aws_vpc.TerraformVPC.id

    tags = {
        Name = "TerraformIGW"
    }
}

resource "aws_route_table" "Terraform_RT" {
    vpc_id = aws_vpc.TerraformVPC.id

    tags = {
        Name = "Terraform RT"
    }
}

resource "aws_route" "route" {
    route_table_id = aws_route_table.Terraform_RT.id
    destination_cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.TerraformIGW.id
}

resource "aws_security_group" "Terraform_SG" {
    description = "WebDMZ"
    name = "WebDMZ"
    vpc_id = aws_vpc.TerraformVPC.id
}

resource "aws_network_interface" "Terraform_NI" {
    subnet_id = aws_subnet.Public_Subnet.id
    description = "Primary network interface"
    security_groups = [aws_security_group.Terraform_SG.id]
}


resource "aws_instance" "pubInstance" {
    ami = "ami-048f6ed62451373d9"
    key_name = "key_for_instance"
    instance_type = "t2.micro"
    tenancy = "default"
    monitoring = false
    disable_api_termination = false
    instance_initiated_shutdown_behavior = "stop"
    credit_specification {
        cpu_credits = "standard"
    }

    tags = {
        Name = "pubInstance"
    }

    ebs_optimized = false
    root_block_device {
        volume_type = "gp2"
        volume_size = 8
    }

}

~~~
