# DevClip – Smart Clipboard & Issue Tracker

DevClip is a smart clipboard manager and issue tracker designed to help developers efficiently store and organize code snippets, logs, and stack traces. The app also integrates automatic issue generation for GitHub/Jira based on detected errors.

## MVP Features

- **Clipboard Monitoring**: Automatically detects and saves copied code snippets, logs, or stack traces.
- **Snippet Categorization**: Categorizes saved snippets based on programming language or content.
- **Issue Generation**: Converts stack traces and logs into structured GitHub/Jira issues.
- **Offline Mode**: Local storage using NeDB, allows functionality even without server sync.
- **Sync with Server**: Optionally sync snippets with a headless Python backend using SSH keys for authentication (no user login required).

## Architecture

### **Client (Electron)**  
- Frontend built with Electron.  
- Local storage with NeDB for offline operation.  
- Syncs snippets with the server via SSH keys, no user binding required.  
- Clipboard monitoring for automatic snippet capture.  

### **Server (Python - FastAPI)**  
- Headless Python backend running FastAPI.  
- NeDB for storing snippets and managing synchronization.  
- Syncing mechanism that pulls/pushes data from clients using SSH key-based authentication.  
- No user management in the MVP; synchronization works via SSH key.

## Tech Stack

- **Frontend**: Electron  
- **Backend**: Python, FastAPI  
- **Database**: NeDB  
- **Sync**: SSH key-based synchronization  
- **Clipboard Monitoring**: Electron clipboard APIs  
- **Issue Tracking**: GitHub/Jira integration

## Installation

### Prerequisites

- Python 3.7+  
- Node.js (for Electron)  
- NeDB for local storage  

### Setting up the Backend

1. Clone the repository.
2. Install required Python dependencies:
   ```bash
   pip install fastapi uvicorn pynedb
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn server:app --reload
   ```

### Setting up the Client

1. Clone the repository.
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Start the Electron client:
   ```bash
   npm start
   ```

## Synchronization

- **SSH Key Authentication**: Clients will authenticate via SSH keys, ensuring secure data synchronization with the server.
- **Push/Pull Mechanism**: Clients can pull and push snippets to/from the server as needed, without requiring user authentication.

## Roadmap

- **User Management**: In a later update, user management and authentication will be added.
- **Enhanced Issue Generation**: Improving the accuracy of generated issues and adding more integrations.

## Contributing

Feel free to fork the project and create pull requests for new features, bug fixes, or improvements.
