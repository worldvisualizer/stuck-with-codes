#!/usr/bin/env bash
find . -maxdepth 1 -type f ! -name "*.cpp" ! -name "*.sh" ! -name ".gitignore" -exec rm -rf {} \;
