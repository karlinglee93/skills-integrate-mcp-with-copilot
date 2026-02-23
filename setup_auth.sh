#!/bin/bash
# Quick Setup Script for Authentication System

echo "======================================"
echo "Authentication System Setup"
echo "======================================"
echo ""

# Step 1: Install dependencies
echo "Installing dependencies..."
cd /workspaces/skills-integrate-mcp-with-copilot
pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi

echo ""
echo "======================================"
echo "✓ Setup Complete!"
echo "======================================"
echo ""
echo "The authentication system is ready to use!"
echo ""
echo "Login credentials:"
echo "  Username: admin@mergington.edu"
echo "  Password: teacher123"
echo ""
echo "You can also use:"
echo "  - prof.smith@mergington.edu / teacher123"
echo "  - mr.jones@mergington.edu / teacher123"
echo ""
echo "======================================"
