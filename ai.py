import speech_recognition as sr
import pyttsx3

# Initialize speech recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define Jarvis responses
responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm functioning within normal parameters. Thank you for asking!",
    "goodbye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't quite catch that."
}

def respond(text):
    response = responses.get(text.lower(), responses["default"])
    print("Jarvis:", response)
    engine.say(response)
    engine.runAndWait()

def main():
    with microphone as source:
        print("Jarvis: Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google_cloud(audio)
        print("You:", text)
        respond(text)
    except sr.UnknownValueError:
        print("Jarvis: Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Jarvis: Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    while True:
        main()
