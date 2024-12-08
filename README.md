# Virtual_Voice_Assistant

# Python Virtual Assistant

This Python-based Virtual Assistant, named **Jarvis 1.0**, is a voice-activated assistant capable of performing various tasks such as searching Wikipedia, opening websites, playing music, telling jokes, sending emails, and more. It uses libraries like `speech_recognition`, `pyttsx3`, and `wikipedia` to process voice commands and respond to user queries.

## Features
- **Voice Recognition**: Converts spoken commands into text using Google Speech Recognition.
- **Wikipedia Search**: Provides a brief summary of topics queried on Wikipedia.
- **Web Browsing**: Opens popular websites like YouTube and Google.
- **Music Playback**: Plays music from a specified directory.
- **Time Reporting**: Tells the current time.
- **Email Sending**: Sends emails using SMTP with pre-configured credentials.
- **Joke Telling**: Fetches and speaks random jokes.
- **Customizable Commands**: Add more functionality as needed.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  ```bash
  pip install pyttsx3 speechrecognition wikipedia pyjokes requests ecapture
  pip install twilio clint beautifulsoup4
  ```

## Setup

1. Clone this repository or copy the script.
2. Install the required libraries using `pip` as mentioned above.
3. Configure your email credentials:
   - Set environment variables `EMAIL_USER` and `EMAIL_PASS` for your email address and password.
   - Example:
     ```bash
     export EMAIL_USER="your_email@gmail.com"
     export EMAIL_PASS="your_password"
     ```
4. Update the `music_dir` variable in the script with the path to your music directory.
5. (Optional) Add custom commands or functionality as needed.

## Usage

1. Run the script:
   ```bash
   python virtual_assistant.py
   ```
2. The assistant will greet you and prompt for your name.
3. Use voice commands to interact with the assistant.

### Example Commands
- "Search Wikipedia for Python programming."
- "Open YouTube."
- "Play music."
- "What time is it?"
- "Tell me a joke."
- "Send email to John."
- "Exit."

## Logs
All interactions and errors are logged in `assistant.log`. Review this file for troubleshooting and debugging.

## Customization
You can extend the assistant’s functionality by adding more commands in the `main()` function. For example:

```python
elif 'open github' in query:
    webbrowser.open("https://github.com")
    speak("Opening GitHub")
```

## Known Issues
- Requires a stable internet connection for features like Wikipedia search and email sending.
- May not recognize certain accents or background noise accurately.

## License
This project is licensed under the MIT License. Feel free to use and modify the code as needed.

---

**Enjoy your smart virtual assistant!**

