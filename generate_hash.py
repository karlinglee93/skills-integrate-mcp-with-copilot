#!/usr/bin/env python3
"""
Password Hash Generator for Mergington High School System
Run this script to generate password hashes for users.json
"""

import hashlib

def hash_password(password: str) -> str:
    """Hash a password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

password = 'teacher123'
hash_value = hash_password(password)

print('=' * 60)
print('PASSWORD HASH GENERATOR')
print('=' * 60)
print(f'Password: {password}')
print(f'Hash: {hash_value}')
print('=' * 60)

# Verify it works
if hash_password(password) == hash_value:
    print('✓ Hash verification successful!')
    print('\nThis hash is already in users.json - ready to use!')
else:
    print('✗ Hash verification failed!')

print('\nTo test login, use:')
print('  Username: admin@mergington.edu')
print('  Password: teacher123')
print('=' * 60)

