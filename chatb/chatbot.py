import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import requests
import pyjokes  # Library for fetching programming jokes
import wolframalpha  # Library for computational knowledge 
import winreg


def speak(audio):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir. how may I help you.")


# Function to take voice input from the user
def takeCommand():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def generateRandomNumber():
    speak("Please specify the range for the random number.")
    speak("Enter the minimum value.")
    min_val = int(input("Enter the minimum value: "))
    speak("Enter the maximum value.")
    max_val = int(input("Enter the maximum value: "))
    
    if min_val >= max_val:
        speak("The minimum value should be less than the maximum value.")
        return
    
    random_number = random.randint(min_val, max_val)
    speak(f"The random number between {min_val} and {max_val} is {random_number}.")

def isAppInstalled(app_name):
    try:
        # Check if the application is installed
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\\" + app_name)
        installed_path = winreg.QueryValueEx(key, "Path")[0]
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        return False

# Function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    server.sendmail('your-email@gmail.com', to, content)
    server.close()

# Function to get weather information
def getWeather(city):
    api_key = "b1fe45524c586d7c7cf6cc3b6a2011f5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 2)
        speak(f"The weather in {city} is currently {weather} with a temperature of {temperature} degrees Celsius.")
    else:
        speak(f"Sorry, I could not find the weather for {city}.")

# Function to tell a joke
def tellJoke():
    joke = pyjokes.get_joke(language="en", category="all")
    speak(joke)

# Function to handle computational knowledge queries
def computeQuery(query):
    try:
        app_id = "YOUR_WOLFRAM_ALPHA_APP_ID"
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        speak(f"The answer is: {answer}")
    except:
        speak("Sorry, I could not find the answer for your query.")

# Function to automate WhatsApp messaging
def sendWhatsAppMessage(number1, message):
    import pyautogui
    import time
    import subprocess
    import re

    number=re.sub(r'\s+', '', number1)
    phnumber =f"+91{number}"
    url = "whatsapp://send?phone="+phnumber
    subprocess.Popen(["cmd", "/C", "start", url], shell=True)
    time.sleep(5)

    pyautogui.typewrite(number)
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    # Wait for some time to load the user
    time.sleep(3)

    # Type the message
    pyautogui.typewrite(message)
    time.sleep(1)
    pyautogui.press('enter')

# Function to play a video on YouTube
def playYouTubeVideo(video):
    import pywhatkit
    pywhatkit.playonyt(video)
    speak(f"Playing {video} on YouTube.")

# Function to automate screen operations
def automateScreen():
    import pyautogui # Library for automation and screen control
    speak("I can perform the following screen operations: type text, move cursor, click mouse, and take screenshot.")
    choice = takeCommand().lower()
    if "type" in choice:
        speak("What text would you like me to type?")
        text = takeCommand()
        pyautogui.typewrite(text)
        speak(f"I have typed: {text}")
    elif "move cursor" in choice:
        speak("I will move the cursor to the center of the screen.")
        width, height = pyautogui.size()
        pyautogui.moveTo(width // 2, height // 2)
        speak("Cursor has been moved.")
    elif "click" in choice:
        speak("I will click the mouse at the current cursor position.")
        pyautogui.click()
        speak("Mouse has been clicked.")
    elif "screenshot" in choice:
        speak("I will take a screenshot and save it to your desktop.")
        screenshot = pyautogui.screenshot()
        screenshot.save(r"C:\Users\deves\OneDrive\Pictures\Screenshots\screenshot.png")
        speak("Screenshot has been saved to your desktop.")
    else:
        speak("Sorry, I could not understand your request.")

# Function to display the menu
def showMenu():
    print("Here are the available options:")
    print("1. Train Status")
    print("2. Ticket Booking")
    print("3. Weather Information")
    print("4. Tell a Joke")
    print("5. Send WhatsApp Message")
    print("6. Play YouTube Video")
    print("7. Automate Screen")
    print("8. Search Wikipedia")
    print("9. Perform Web Search")
    print("10. Get System Information")
    print("11. Exit")

# Function to handle menu options
def handleMenuOption(option):
    if option == 1:
        webbrowser.open("https://www.railyatri.in/live-train-status")
    elif option == 2:
        webbrowser.open("https://www.railyatri.in/train-ticket?utm_source=lts_search_dweb_header_ttb&device_type_id=61")
    elif option == 3:
        speak("Which city would you like to get the weather for?")
        city = takeCommand().lower()
        getWeather(city)
    elif option == 4:
        tellJoke()
    elif option == 5:
        speak("Please enter the phone number you want to send the message to.")
        number = takeCommand()
        speak("What message would you like to send?")
        message = takeCommand()
        sendWhatsAppMessage(number, message)
    elif option == 6:
        speak("What video would you like me to play?")
        video = takeCommand()
        playYouTubeVideo(video)
    elif option == 7:
        automateScreen()
    elif option == 8:
        speak("What would you like to search on Wikipedia?")
        search_query = takeCommand()
        try:
            summary = wikipedia.summary(search_query, sentences=2)
            speak("According to Wikipedia:")
            print(summary)
            speak(summary)
        except wikipedia.exceptions.PageError:
            speak("Sorry, I could not find any relevant information on Wikipedia.")
        except wikipedia.exceptions.DisambiguationError as e:
            speak("The search term is ambiguous. Please be more specific.")
            print(e.options)
    elif option == 9:
        speak("What would you like to search for?")
        search_query = takeCommand()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {search_query}")
    elif option == 10:
        import platform
        system = platform.system()
        architecture = platform.architecture()[0]
        machine = platform.machine()
        speak(f"Your system is running {system} {architecture} on {machine} architecture.")
    elif option == 11:
        speak("Goodbye!")
        exit()
    else:
        speak("Invalid option. Please try again.")


def process_command(query):
    print("Inside process_command")
    wishMe()
    query = takeCommand().lower()

    # Show menu
    if 'menu' in query:
        showMenu()
        speak("Please select an option from the menu.")
        option = int(input())
        handleMenuOption(option)
        return "Menu option handled."

    # Wikipedia search
    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        return "Wikipedia search completed."

    elif 'is installed' in query:
        speak("What application would you like to check for?")
        app_name = takeCommand().lower()
        if isAppInstalled(app_name + ".exe"):
            speak(f"{app_name} is installed on your system.")
            return f"{app_name} is installed on your system."
        else:
            speak(f"{app_name} is not installed on your system.")
            return f"{app_name} is not installed on your system."

    # Open websites
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")
        return "Opening YouTube."

    elif 'open google' in query:
        webbrowser.open("https://www.google.com/")
        return "Opening Google."

    elif 'open gpt' in query.lower():
        webbrowser.open("https://chat.openai.com")
        return "Opening GPT website."

    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")
        return "Opening Stack Overflow."

    # Play music
    elif 'play music' in query:
        music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        return "Playing music."

    # Get time
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        return f"The current time is {strTime}."

    # Wish user
    elif 'wish me' in query:
        wishMe()
        return "Wishing you."

    # Open applications
    elif 'open code' in query:
        codePath = r"C:\Users\deves\OneDrive\Desktop\c tutorials\DSA"
        os.startfile(codePath)
        return "Opening code editor."

    elif 'open spotify' in query.lower():
        codePath = r"C:\Users\deves\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0/Spotify"
        os.startfile(codePath)
        return "Opening Spotify."

    # Send email
    elif 'send email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "deveshchandak4002@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent.")
            return "Email sent successfully."
        except Exception as e:
            print(e)
            speak("Sorry, I could not send the email.")
            return "Failed to send email."

    # Get weather information
    elif 'weather' in query or 'vedar' in query:
        speak("Which city would you like to get the weather for?")
        city = takeCommand().lower()
        getWeather(city)
        return "Fetching weather information."

    # Tell a joke
    elif 'tell me a joke' in query:
        tellJoke()
        return "Telling a joke."

    # Computational knowledge query
    elif 'calculate' in query or 'what is' in query or 'how much' in query:
        computeQuery(query)
        return "Performing computational query."

    # WhatsApp automation
    elif 'send whatsapp message' in query:
        speak("Please enter the phone number you want to send the message to.")
        number = takeCommand()
        speak("What message would you like to send?")
        message = takeCommand()
        sendWhatsAppMessage(number, message)
        return "Sending WhatsApp message."

    # YouTube video playback
    elif 'play youtube' in query:
        speak("What video would you like me to play?")
        video = takeCommand()
        playYouTubeVideo(video)
        return "Playing YouTube video."

    # Screen automation
    elif 'automate screen' in query:
        automateScreen()
        return "Performing screen automation."

    # Wikipedia search with voice output
    elif 'search wikipedia' in query:
        speak("What would you like to search on Wikipedia?")
        search_query = takeCommand()
        try:
            summary = wikipedia.summary(search_query, sentences=2)
            speak("According to Wikipedia:")
            print(summary)
            speak(summary)
            return "Wikipedia search completed."
        except wikipedia.exceptions.PageError:
            speak("Sorry, I could not find any relevant information on Wikipedia.")
            return "No Wikipedia search results found."
        except wikipedia.exceptions.DisambiguationError as e:
            speak("The search term is ambiguous. Please be more specific.")
            print(e.options)
            return "Wikipedia search term ambiguous."

    # Perform web search
    elif 'search' in query:
        speak("What would you like to search for?")
        search_query = takeCommand()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {search_query}")
        return "Performing web search."

    # Get system information
    elif 'system information' in query:
        import platform
        system = platform.system()
        architecture = platform.architecture()[0]
        machine = platform.machine()
        speak(f"Your system is running {system} {architecture} on {machine} architecture.")
        return f"System information: {system} {architecture} on {machine} architecture."

    elif 'random number' in query:
        generateRandomNumber()
        return "Generating a random number."

    # Exit the program
    elif 'exit' in query:
        speak("Goodbye!")
        return "Exiting program."

    else:
        return "Sorry, I couldn't understand your command."
