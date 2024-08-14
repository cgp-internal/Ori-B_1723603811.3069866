FastAPI Note Taking App
======================

This is a FastAPI-based note taking application that allows users to create, read, update, and delete notes. It utilizes SQLAlchemy as the ORM, configured using the `app_config` dictionary from `app_config.py` to interact with a PostgreSQL database.

## Technologies Used

* FastAPI for the API framework
* SQLAlchemy for database interactions
* Pydantic for data validation

## Configuration

The application configuration is defined in `app_config.py`, which exposes the `app_config` variable.

## Database

The database connection is set up in `database.py` using SQLAlchemy ORM.

## Models

The `Note` model is defined in `models.py`, which exposes the `Note` variable.

## Schemas

The Pydantic model for Note data validation is defined in `schemas.py`, which exposes the `NoteSchema` variable.

## Routers

The routes for CRUD operations on Notes are defined in `routers/notes.py`, which exposes the `notes_router` variable.

## How to Run
-----------

### 1. Install Requirements

Run `pip install -r requirements.txt` to install the required dependencies.

### 2. Run the Application

Run `python app/main.py` to start the FastAPI server.

### 3. Access the API

Open your web browser and navigate to `http://localhost:8000/docs` to access the API documentation.

### 4. Create a Note

Send a `POST` request to `http://localhost:8000/notes/` with a JSON body containing the note details.

### 5. View Notes

Send a `GET` request to `http://localhost:8000/notes/` to retrieve a list of all notes.

### 6. Update a Note

Send a `PUT` request to `http://localhost:8000/notes/{note_id}` with a JSON body containing the updated note details.

### 7. Delete a Note

Send a `DELETE` request to `http://localhost:8000/notes/{note_id}` to delete a note.

Note: Replace `{note_id}` with the actual ID of the note you want to update or delete.