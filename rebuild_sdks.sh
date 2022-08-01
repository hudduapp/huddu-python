#!/bin/bash

sudo rm -r ./sdks

java -jar swagger-codegen-cli.jar generate -i https://api.huddu.io/openapi.json -l ruby -o ./sdks/ruby
java -jar swagger-codegen-cli.jar generate -i https://api.huddu.io/openapi.json -l python -o ./sdks/python
java -jar swagger-codegen-cli.jar generate -i https://api.huddu.io/openapi.json -l go -o ./sdks/go
java -jar swagger-codegen-cli.jar generate -i https://api.huddu.io/openapi.json -l java -o ./sdks/java
java -jar swagger-codegen-cli.jar generate -i https://api.huddu.io/openapi.json -l kotlin-client -o ./sdks/kotlin
java -jar swagger-codegen-cli.jar generate -i https://api.huddu.io/openapi.json -l swift5 -o ./sdks/swift5