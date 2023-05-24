import pyttsx3

Arnold=pyttsx3.init()
Arnold.setProperty("rate", 100)

def say_happy_birthday():
    init_rate = Arnold.getProperty("rate")
    Arnold.say("Happy Birthday to you")
    Arnold.say("Happy Birthday to you")
    Arnold.say("Happy Birthday dear")
    Arnold.setProperty("rate", 50)
    Arnold.say("Michael")
    
    Arnold.setProperty("rate", init_rate)
    Arnold.say("Happy Birthday to you")

    Arnold.runAndWait()

if __name__ == "__main__":
    say_happy_birthday()
