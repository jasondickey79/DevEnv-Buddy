#!/bin/bash

echo "Running smoke test..."

# Try hitting the app at localhost:8080
if curl --fail http://localhost:8080 > /dev/null 2>&1; then
    echo "Soke test passed: App is reachable at http://localhost:8080"
    exit 0
else
    echo "Smoke test failed: App is not responding at http://localhost:8080"
    exit 1
fi
