#!/bin/bash


sudo apt update -y
sudo apt install -y default-jdk
sudo apt install -y maven

wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.34/swagger-codegen-cli-3.0.34.jar -O swagger-codegen-cli.jar