# Authentication Setup Instructions

## Quick Start - The System is Ready!

The authentication system is **already configured and ready to use**! 🎉

### Login Credentials

Use these accounts to login:

1. **Admin Account**
   - Username: `admin@mergington.edu`
   - Password: `teacher123`
   - Role: Admin

2. **Staff Account 1**
   - Username: `prof.smith@mergington.edu`
   - Password: `teacher123`
   - Role: Staff

3. **Staff Account 2**
   - Username: `mr.jones@mergington.edu`
   - Password: `teacher123`
   - Role: Staff

### How to Use

1. **Start the application** (if not already running)
2. **Click the "Login" button** in the top-right corner
3. **Enter credentials** (use any of the accounts above)
4. **Click Login**
5. You should see your name appear in the top-right corner
6. Now you can register and unregister students!

### Security Features

- ✅ Students (not logged in) can only **view** activities
- ✅ Only logged-in staff/admin can **register** students
- ✅ Only logged-in staff/admin can **unregister** students
- ✅ Passwords are hashed using SHA256
- ✅ JWT tokens for session management (8-hour expiration)

### Troubleshooting

#### "Login Failed" Error
1. Make sure you're using the exact credentials listed above
2. Check that the username includes `@mergington.edu`
3. Password is case-sensitive: `teacher123` (all lowercase)

#### Can't See Login Button
1. Check that the application is running
2. Refresh the page
3. Clear your browser cache

#### Dependencies Missing
If you see import errors, install dependencies:
```bash
cd /workspaces/skills-integrate-mcp-with-copilot
pip install -r requirements.txt
```

### Technical Notes

This system uses:
- **SHA256 hashing** for password storage (simpler than bcrypt, suitable for educational purposes)
- **JWT tokens** for authentication
- **Role-based access control** (Admin, Staff, Student)

For production use, consider upgrading to bcrypt or Argon2 for password hashing.
