# Setup Instructions

## Installation

- Pull the remote repository with Git
- Open the folder in VSCode
- Ctrl+Shift+P -> 'Python: Create Environment' -> Select Venv Option -> Select Python Version -> Select 'requirements.txt'

## Datababase and Configuration

- Install MySQL Community Edition or Create a Docker Container
- Create a database (the name must be the same as what you enter in the `.env` file)
- Copy the `.env.example` and rename it to `.env`
- Enter in your database credentials into the `.env` file

## Starting the Application

- In VSCode: Press F5 and select 'Python Debugger' and then 'FastAPI'
