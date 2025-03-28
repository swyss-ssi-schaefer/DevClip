import time
import logging
import requests

# Create a logger for the console module
logger = logging.getLogger(__name__)

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
    print("3. Stop a module")
    print("4. Sync data across modules")
    print("5. Exit")

def get_user_choice():
    """Gets user input for menu selection."""
    choice = input("Enter your choice: ")
    return choice.strip()

def fetch_status():
    """Fetch the module status from the API"""
    try:
        response = requests.get("http://127.0.0.1:8000/status")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching status: {e}")
        return {"error": "Failed to fetch status"}

def run_console():
    """Runs the console management tool."""
    display_welcome()
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == "1":
            print("Fetching module status...")
            status = fetch_status()
            print(status)
        elif choice == "2":
            module_name = input("Enter module name to start: ")
            print(f"Starting module {module_name}...")
            # Logic to start module here
        elif choice == "3":
            module_name = input("Enter module name to stop: ")
            print(f"Stopping module {module_name}...")
            # Logic to stop module here
        elif choice == "4":
            print("Syncing data across modules...")
            # Trigger sync across modules
            try:
                response = requests.post("http://127.0.0.1:8000/sync-data")
                print(response.json())
            except requests.exceptions.RequestException as e:
                logger.error(f"Error syncing data: {e}")
        elif choice == "5":
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please try again.")
