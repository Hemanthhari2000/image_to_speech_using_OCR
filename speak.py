import pyttsx3

# initialize the engine
engine = pyttsx3.init()

def speak(words):
	
	# set the voice and the rate to your wish
	voices = engine.getProperty('voices')
	female_voice_id = voices[1].id
	voice_rate = 145

	# set the properties that you like
	engine.setProperty('voice', female_voice_id)
	engine.setProperty('rate', voice_rate)


	engine.say(words)

	engine.runAndWait()

	return 0


def main():
	# Default Text.
	speak("Hello,Nice to meet you.")

if __name__ == '__main__':
	main()