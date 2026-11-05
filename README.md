# AI-Powered Task Manager

A simple Python command-line application for managing daily tasks efficiently. It allows users to create tasks, mark them as completed, delete them, and generate smaller actionable subtasks from a larger, more complex request using an AI-powered workflow.

## Overview

This project was built as a practical task management tool with a lightweight user interface and persistent storage. Tasks are saved in a local JSON file, which means they remain available between runs without needing a database or external service.

The project combines:
- a classic task manager workflow,
- file-based persistence,
- AI-assisted task decomposition for complex tasks,
- a simple interactive menu in the terminal.

## Features

- Add new tasks manually
- List all existing tasks
- Mark a task as completed
- Delete tasks
- Split complex tasks into simpler steps with Gemini AI
- Persist task data locally in JSON format
- Keep the interface simple and fast for terminal use

## How it works

The app provides a console menu with the following options:

1. Add task
2. Add complex task (with AI)
3. List tasks
4. Complete task
5. Delete task
6. Quit

When a complex task is entered, the system sends the description to the AI service, which returns a list of smaller subtasks. Those subtasks are then added to the task manager as individual tasks.

## Project structure

- `main.py` — entry point for the CLI menu and user interaction
- `task_manager.py` — core task logic, storage, and task lifecycle methods
- `ai_service.py` — Gemini API integration for task breakdown generation
- `tasks.json` — local storage file for active tasks
- `tests/test_task_manager.py` — automated tests for task creation, completion, deletion, and loading
- `requirements.txt` — Python dependencies

## Requirements

- Python 3.10+
- A Gemini API key
- Access to the internet for the AI service call

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TomasJose05/taskManager.git
   cd taskManager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment variable for the AI service. Create a `.env` file in the project root with:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the application

Start the CLI app with:

```bash
python main.py
```

## Usage example

After launching the app, you can:

- add a simple task such as: `Write project report`
- add a complex task such as: `Plan the launch of a new feature for the app`
- let the AI break it into smaller actionable tasks
- list the tasks and mark one as complete when finished

## Data storage

The application stores tasks in a JSON file named `tasks.json`.

Example structure:

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "completed": false
    }
]
```

This keeps the project simple and dependency-free while still preserving task data across sessions.

## AI integration

The AI service is implemented in `ai_service.py` and uses the Gemini API through an OpenAI-compatible endpoint. The purpose is to transform a broad or complicated task into a short list of clear subtasks that are easier to complete.

## Testing

The repository includes a test suite that verifies:
- task creation and persistence,
- completion behavior,
- deletion behavior,
- restoration of saved tasks when the app starts again.

Run tests with:

```bash
pytest
```

## Notes

This project demonstrates a lightweight Python task manager with practical CLI behavior and a simple AI integration. It is ideal for learning, prototyping, and extending with additional features such as priorities, categories, deadlines, or a graphical interface.
