import time

def display_welcome():
    """Displays the ASCII welcome screen."""
    print("""
     ____             _ _      _    
    |  _ \  ___  ___ | (_) ___| |_  
    | | | |/ _ \/ _ \| | |/ _ \ __| 
    | |_| |  __/ (_) | | |  __/ |_  
    |____/ \___|\___/|_|_|\___|\__| 
    
    DevClip Server Management Console
    """)

def show_menu():
    """Displays the main menu."""
    print("\nMain Menu:")
    print("1. Show module status")
    print("2. Start a module")
    print("3. Exit")

def get_user_choice():
    """Gets user input for menu selection."""
    choice = input("Enter your choice: ")
    return choice.strip()

def run_console():
    """Runs the console management tool."""
    display_welcome()
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == "1":
            print("Fetching module status...")
            # Fetch and display module status here
        elif choice == "2":
            module_name = input("Enter module name to start: ")
            print(f"Starting module {module_name}...")
            # Logic to start module here
        elif choice == "3":
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_console()
