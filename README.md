# Desktop Assistant

Desktop Assistant is a versatile Python-based application designed to enhance your desktop experience by streamlining basic operations and providing quick access to a variety of functions. This assistant seamlessly integrates with your desktop environment, allowing you to perform tasks like opening applications, conducting web searches, and taking screenshots. The screenshot feature enables you to capture your screen effortlessly. It also leverages APIs for weather updates and news, making it a valuable addition to your desktop.

## Features

Application Launcher: Launch your favorite applications with a simple voice command or text input. Desktop Assistant provides a convenient way to open programs quickly and effortlessly.

Web Search: Search the web using your default browser. Desktop Assistant helps you find information, websites, and more with ease.

Screenshot Capture: Capture your screen with a single command, making it easy to save and share what's on your desktop.

YouTube Song Player: Enjoy your favorite music from YouTube by instructing the assistant to play specific songs or artists. It's a convenient way to set the mood right from your desktop.

Live Weather Updates: Get real-time weather information for your location. Stay informed about current weather conditions, forecasts, and more.

News Updates: Stay up-to-date with the latest news. Desktop Assistant fetches news from various sources using the NewsAPI, keeping you informed about current events.

Jokes: Everyone loves a good laugh. The assistant can brighten your day with a selection of jokes from the Official Jokes API.

## Technologies

Python: The core of this project is built using Python, a versatile and widely used programming language.

Python Libraries: Various Python libraries and modules are used to enable different features and functionalities. These include but are not limited to requests, json, subprocess, pyttsx3, webbrowser, and more.

API Integration: To provide real-time information such as weather updates, news, and jokes, the project integrates with external APIs. These APIs include OpenWeatherMap, NewsAPI, and the Official Jokes API.

PyCharm IDE: The project is developed and maintained using PyCharm IDE, a popular IDE that provides a rich development environment for Python programming languages.

## Advantages

Efficiency: Desktop Assistant simplifies common desktop tasks, making them quicker and more convenient. It can save you time and effort by automating various operations.

User-Friendly: The user interface is designed to be intuitive, with both voice and text input options, making it accessible to a broad range of users.

Customization: The assistant can be easily customized to add new features or extend its existing capabilities, allowing you to tailor it to your needs.

Screenshot Capture: Easily capture your screen, ideal for sharing information or troubleshooting.

Information at Your Fingertips: With integrated weather, news, and entertainment features, Desktop Assistant keeps you informed and entertained without leaving your desktop.

Open Source: This project is open source, so you can contribute to its development and adapt it to your specific requirements.

## Getting Started

Follow the instructions below to get started with Desktop Assistant.

### Installation

To clone the Desktop Assistant repository into PyCharm IDE and install the required packages to run the project, you can follow these steps:

1. #### Install PyCharm

If you haven't already, download and install PyCharm IDE on your computer. You can get it from the official JetBrains website.

1. #### Clone the Repository

Open PyCharm and follow these steps:

a. Click on "Check out from Version Control" on the welcome screen or from the "File" menu.

b. Select "Git" as the version control system.

c. In the "URL" field, enter the repository URL

```bash
https://github.com/rugwedpatharkar/Desktop_assistant.git

d. Choose a directory where you want to save the project on your local machine.

e. Click the "Clone" button.

1. ### Set Up a Virtual Environment (Optional but recommended):
To keep your project dependencies isolated, you can set up a virtual environment in PyCharm:

a. In PyCharm, go to "File" > "Settings" (or "PyCharm" > "Preferences" on macOS).

b. In the left sidebar, navigate to "Project: DesktopAssistant" > "Python Interpreter."

c. Click the gear icon on the top-right corner and select "Add."

d. Choose "Virtual Environment" and configure it according to your preferences.

e. Click "OK" to create the virtual environment.

4. ### Install Required Packages:
With your project open in PyCharm:

a. Open a terminal within PyCharm by going to "View" > "Tool Windows" > "Terminal."

b. Navigate to your project directory. You should see your project's files in the terminal.

c. Install the required Python libraries using pip:

```bash
pip install -r requirements.txt

5. ### Usage:
Now that you've set up the project, you can run the Desktop Assistant script:

a. Make sure you have your virtual environment activated (if you created one) or use the system Python interpreter.

b. Run the Desktop Assistant script:

```bash
python assistant.py


That's it! You've successfully cloned the Desktop Assistant repository into PyCharm IDE and set up the project for development or usage.

Follow the on-screen instructions and use voice or text commands to interact with the assistant, including taking screenshots when needed.
