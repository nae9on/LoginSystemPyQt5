from exceptions.login_exceptions import UsernameAlreadyExists, PasswordTooWeak, InvalidUsername, InvalidPassword,\
    UserNotLoggedIn

import hashlib
import json

from typing import Optional, Dict


class User:

    def __init__(self, username: str, password: Optional[str] = None) -> None:
        self.username: str = username
        self.encrypted_password: Optional[str] = self._encrypt_password(password) if password else None
        self.is_logged_in: bool = False

    def _encrypt_password(self, password: str) -> None:
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password: str) -> bool:
        return self._encrypt_password(password) == self.encrypted_password


class Authenticator:
    """
    Manages reading existing users, adding new users, logging in, logging out and other user management operations.
    """

    _cached_users_list_file = "./database/users_list.json"  # file containing username, encrypted password key-values

    def __init__(self) -> None:
        self.users: Dict[str, User] = {}  # username-user key-values
        cached_data: Optional[Dict[str, str]] = self._get_cached_users()
        if cached_data is not None:
            cached_users: Dict[str, User] = {}
            for username, encrypted_password in cached_data.items():
                user = User(username)
                user.encrypted_password = encrypted_password
                cached_users[username] = user
            self.users = cached_users

    @staticmethod
    def _get_cached_users() -> Optional[Dict[str, str]]:
        """
        Reads .json file containing username, encrypted password key-values and returns cached data.
        """
        cached_data: Optional[Dict[str, str]] = None
        with open(Authenticator._cached_users_list_file, 'r') as file:
            try:
                cached_data = json.load(file)
            except json.JSONDecodeError:
                print("No cached users")
        return cached_data

    def add_user(self, username: str, password: str) -> None:
        """
        Adds new user to the list of cached users and also saves new user's record to file.
        """
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooWeak(username)
        self.users[username] = User(username, password)
        self._write_to_file()

    def login(self, username: str, password: str) -> bool:
        """
        Tries to login using a given username and password.
        """
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not self.users[username].check_password(password):
            raise InvalidPassword(username)

        user.is_logged_in = True
        return True

    def logout(self, username: str) -> None:
        """
        Tries to logout using a given username.
        """
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if user.is_logged_in:
            user.is_logged_in = False
        else:
            raise UserNotLoggedIn(username)

    def is_logged_in(self, username: str) -> bool:
        """
        Returns true if a user is already logged in otherwise false.
        """
        if username in self.users:
            return self.users[username].is_logged_in
        return False

    def _write_to_file(self) -> None:
        """
        Writes username-encrypted password key-values to .json file.
        """
        username_password_dict: Dict[str, str] = {username: user.encrypted_password
                                                  for username, user in self.users.items()}
        with open(Authenticator._cached_users_list_file, 'w') as file:
            json.dump(username_password_dict, file, indent=4, sort_keys=True)