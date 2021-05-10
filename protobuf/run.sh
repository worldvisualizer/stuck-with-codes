#!/usr/bin/env bash

rm -rf example_pb2.py
protoc --python_out=. example.proto
protoc --js_out=import_style=commonjs,binary:. example.proto
