#!/usr/bin/env python3
"""
Test Authentication System
This script tests the authentication setup to make sure everything is working.
"""

import hashlib
import json
import os
from pathlib import Path

def hash_password(password: str) -> str:
    """Hash a password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def test_auth():
    print("=" * 60)
    print("TESTING AUTHENTICATION SYSTEM")
    print("=" * 60)
    print()
    
    # Test 1: Check if users.json exists
    print("Test 1: Checking users.json file...")
    users_file = Path(__file__).parent / "src" / "users.json"
    if not users_file.exists():
        print("❌ FAILED: users.json not found!")
        return False
    print("✅ PASSED: users.json exists")
    print()
    
    # Test 2: Load and parse users.json
    print("Test 2: Loading users.json...")
    try:
        with open(users_file, 'r') as f:
            data = json.load(f)
        users = {user['username']: user for user in data['users']}
        print(f"✅ PASSED: Loaded {len(users)} users")
        print(f"   Users: {list(users.keys())}")
    except Exception as e:
        print(f"❌ FAILED: Could not load users.json - {e}")
        return False
    print()
    
    # Test 3: Verify password hashes
    print("Test 3: Verifying password hashes...")
    test_password = "teacher123"
    expected_hash = hash_password(test_password)
    print(f"   Password: {test_password}")
    print(f"   Expected hash: {expected_hash}")
    print()
    
    all_match = True
    for username, user in users.items():
        stored_hash = user['password_hash']
        if stored_hash == expected_hash:
            print(f"   ✅ {username}: Hash matches")
        else:
            print(f"   ❌ {username}: Hash mismatch!")
            print(f"      Stored:   {stored_hash}")
            print(f"      Expected: {expected_hash}")
            all_match = False
    
    if not all_match:
        print()
        print("❌ FAILED: Some password hashes don't match")
        return False
    print()
    print("✅ PASSED: All password hashes are correct")
    print()
    
    # Test 4: Check dependencies
    print("Test 4: Checking dependencies...")
    try:
        from jose import jwt
        print("   ✅ python-jose: installed")
    except ImportError:
        print("   ❌ python-jose: NOT installed")
        all_match = False
    
    try:
        from fastapi import FastAPI
        print("   ✅ fastapi: installed")
    except ImportError:
        print("   ❌ fastapi: NOT installed")
        all_match = False
    
    if not all_match:
        print()
        print("❌ FAILED: Some dependencies missing")
        print("   Run: pip install -r requirements.txt")
        return False
    print()
    print("✅ PASSED: All dependencies installed")
    print()
    
    # Summary
    print("=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)
    print()
    print("Your authentication system is ready to use!")
    print()
    print("Login with:")
    print("  Username: admin@mergington.edu")
    print("  Password: teacher123")
    print()
    print("=" * 60)
    return True

if __name__ == "__main__":
    test_auth()
