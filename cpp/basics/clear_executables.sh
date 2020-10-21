#!/usr/bin/env bash
find . -type f ! -name "*.cpp" ! -name "*.sh" ! -name ".gitignore" -exec rm -rf {} \;
