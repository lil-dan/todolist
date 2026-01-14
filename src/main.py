from src.auth import AuthManager


def pre_login_menu() -> None:
    auth = AuthManager()
    while True:
        print("=== To-Do CLI ===")
        print("1) Login")
        print("2) Sign Up")
        print("3) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if auth.login(username, password):
                print(f"Welcome back, {username}!")
                # Placeholder: would transition to main app loop here
                break
            else:
                print("Invalid credentials.\n")

        elif choice == "2":
            username = input("Choose a username: ").strip()
            password = input("Choose a password: ").strip()
            if auth.sign_up(username, password):
                print("Sign up successful. Please login.\n")
            else:
                print("Username already exists.\n")

        elif choice == "3":
            print("Goodbye.")
            return

        else:
            print("Invalid selection.\n")


if __name__ == "__main__":
    pre_login_menu()
