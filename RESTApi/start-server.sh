#!/bin/sh
echo "Starting REST API server..."

# Important: -u permet de ne pas bufferiser les logs
python -u MyRamesServer.py
