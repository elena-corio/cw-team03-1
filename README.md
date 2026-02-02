# Collaborative Project - Team 03.1 Session 03

## Project Structure

This project follows principles inspired by **Hexagonal Architecture** (Ports and Adapters), focusing on separation of concerns.  
- **src/config.py**: Handles configuration and environment variables.
- **src/adapters/**: Contains code for interacting with external systems (e.g., `send_data.py`).
- **src/application/**: Contains workflow and application logic.
- **src/domain/**: Contains core models and business logic.

This structure improves maintainability and testability.

## Setup

### Prerequisites

- [uv](https://github.com/astral-sh/uv)
- Python 3.8+

### Installation

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd cw_team03.1_session03
   ```

2. **Install dependencies:**
   ```
   pip install uv
   ```
   uv sync
   ```

3. **Set environment variables**  
   (recommended: create a `.env` file in the project root):
   ```
   WORKSPACE_ID=your_workspace_id
   PROJECT_ID=your_project_id
   SOURCE_MODEL=your_source_model
   TARGET_MODEL=your_target_model
   MODEL_NAME=your_model_name
   ```

### Running the Project

To run the main script:
```
uv python src/main.py
```
Replace `src/main.py` with your actual entry point if different.

## Example Folder Structure

```
cw_team03.1_session03/
├── src/
│   ├── config.py
│   ├── adapters/
│   │   └── send_data.py
│   ├── application/
│   │   └── workflow.py
│   ├── domain/
│   │   └── models.py
│   └── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
