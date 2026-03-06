from fastapi import HTTPException


def require_roles(allowed_roles):

    def checker(user):

        if user.role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )

        return user

    return checker