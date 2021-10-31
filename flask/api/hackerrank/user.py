from flask import request

class User:
    # Users [username, password, role]
    users: list[list[str]] = [["guest", "guest134", "guest"],
                              ["admin", "admin124", "admin"]]

    def is_authenticated(self) -> bool:
        """Basicauth."""

        if request.authorization is None:
            return False

        username = request.authorization["username"]
        password = request.authorization["password"]

        for user in self.users:
            if user[0] == username and user[1] == password:
                return True

        return False

    def has_role(self, role: str, username: str | None = None):
        """Check user role."""
        
        if username is None:
            username = request.authorization["username"]

        for user in self.users:
            if user[0] == username and user[2] == role:
                return True

        return False