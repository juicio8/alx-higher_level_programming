#!/bin/bash
#Send a GET req to URL with a header variable
curl -sH "X-School-User-Id: 98" "$1"
