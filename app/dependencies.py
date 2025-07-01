"""
Shared dependencies for FastAPI app (DB, Auth, etc.)
"""

from fastapi import Depends, HTTPException, status

# Example: Dependency for getting current user (placeholder)
def get_current_user():
    # Implement your logic here (e.g., decode JWT, fetch user from DB)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

# Add more dependencies as needed
