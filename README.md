# Python Mini Projects

Welcome to my collection of simple Python projects!  
This repo is meant to track my learning progress, experiment with ideas, and build a solid foundation with Python.

## Projects

### 1. Project 1 – Guess the Number 🎯
A simple Python program where the computer picks a random number and the user tries to guess it.

### 2. Project 2 – Dice Game 🎲
A turn-based dice game for 2 to 4 players.  
Each player takes turns rolling a 6-sided die and tries to reach 50 points.  
- Rolling a 1 ends the player's turn and resets the turn score to 0.  
- Rolling any other number adds to the turn score.  
- Players can choose to continue rolling or hold and keep their score.  
- First player to reach or exceed 50 total points wins.

### 3. Project 3 - Contact Book 📇

A simple terminal-based Contact Book built with Python.  
This project helps you learn the basics of object-oriented programming, modules, and file structure in Python.

#### 🚀 Features
- Add a new contact (name, phone, email)
- View all saved contacts
- Search for a contact by name

### 4. Project 4 Simple Note App

A command-line note-taking app built in Python. Notes are saved as individual `.txt` files in a local folder.  
You can create, read, list, and delete notes — all through a simple interactive menu.

Learned concepts:
- File handling in Python (`open`, `read`, `write`)
- Directory and path management with `os`
- Organizing code using classes and folders

### 5. Project 5 Weather App  
A simple command-line Weather Application using the OpenWeather API.  
It lets users check the current weather by city name.

**Skills learned:**
- Working with external APIs using `requests`
- Using `.env` files and `python-dotenv` for secure API key storage
- Parsing JSON responses
- Modular design using Python classes
- Building user-friendly command-line interfaces

**Features:**
- Search weather by city
- Displays temperature, condition, country, etc.
- Clean output formatting in terminal
- Graceful handling of invalid city names or API issues

**Before you run project 5:**
1. Create a `.env` file in the `weather_app/` folder:
```bash
OPENWEATHER_API_KEY=YOUR_API_KEY
```
## How to Run

Make sure you have Python 3 installed.  
Run any project with:
```bash
python3 project.py
```