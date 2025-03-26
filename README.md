# DevClip

DevClip is an intelligent clipboard manager and automatic issue generator for developers. It captures copied code snippets, recognizes programming languages and stack traces, and allows seamless integration with GitHub and Jira.

## Features (MVP)

- **Clipboard Monitoring**: Automatically saves copied content.
- **Snippet Categorization**: Detects programming languages, stack traces, and logs.
- **Search & Filter**: Retrieve saved snippets by tags or content.
- **Issue Generator**: Converts stack traces into structured GitHub/Jira issues.
- **Electron GUI**: Simple interface for managing snippets.
- **Hotkeys**: Quick access to snippets and issue creation.

## Tech Stack

- **Frontend**: Electron with JavaScript
- **Database**: NeDB (lightweight NoSQL database)
- **Clipboard Handling**: `electron-clipboard` or `clipboardy`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/devclip.git
   cd devclip
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Run the application:
   ```sh
   npm start
   ```

## Roadmap

- [ ] Advanced snippet categorization with AI detection
- [ ] API for integration with other tools
- [ ] Cloud synchronization for snippets
- [ ] Multi-platform support (Windows, macOS, Linux)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT License

