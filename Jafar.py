import pyttsx3  # For text-to-speech
import speech_recognition as sr  # For speech recognition
import requests

class Jafar:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.weather_api_key = "fa3dd24a9a6248019da45825231908"
        self.commands = {
            "hello": "Hello! How can I assist you?",
            "how are you": "I'm just a computer program, but I'm functioning well!",
            "whats your name?": "My name is Jafar, My creator gave it to me",
            "goodbye": "Goodbye! Have a great day.",
            "bye":"Bye Bye!",
            "weather": "I'm sorry, I don't have access to real-time weather information."
        }

    def get_weather(self, city_name):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city_name,
            "appid": self.weather_api_key,
            "units": "metric"  # You can use "imperial" for Fahrenheit
        }
        
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"The weather in {city_name} is {description} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldn't fetch the weather information at the moment."


    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            user_input = self.recognizer.recognize_google(audio)
            print("User: " + user_input)
            return user_input.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""

    def respond(self, user_input):
        for command, response in self.commands.items():
            if command == "weather":
                    city_name = input("Which city's weather would you like to know? ")
                    weather_response = self.get_weather(city_name)
                    self.speak(weather_response)
            elif command in user_input:
                self.speak(response)
                return
        self.speak("I'm sorry, I didn't understand that.")

def main():
    jafar = Jafar()
    jafar.speak("Hello! I'm Jaafar, your personal AI. How can I assist you today?")
    
    while True:
        user_input = jafar.listen()
        jafar.respond(user_input)
        if "goodbye" or "bye" in user_input:
            break

if __name__ == "__main__":
    main()