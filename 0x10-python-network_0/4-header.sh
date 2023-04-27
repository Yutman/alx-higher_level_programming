#!/bin/bash
# Send a custom header
curl -sH "X-School-User-Id: 98" "$1"
