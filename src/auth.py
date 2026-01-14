import json
import os
from typing import List, Dict


class AuthManager:
    """Simple username/password manager backed by a JSON file.

    Passwords are stored in plaintext for this prototype (per spec).
    """

    def __init__(self, path: str = "data/users.json") -> None:
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, str]]:
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, users: List[Dict[str, str]]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2)

    def sign_up(self, username: str, password: str) -> bool:
        users = self._load()
        if any(u["username"] == username for u in users):
            return False
        users.append({"username": username, "password": password})
        self._save(users)
        return True

    def login(self, username: str, password: str) -> bool:
        users = self._load()
        return any(u["username"] == username and u["password"] == password for u in users)
