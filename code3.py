from code2 import take_command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
    song = command.replace('play','')
    talk('playing' + song)
    pywhatkit.playonyt(song)
elif 'time' in command:
    time = datetime.datetime.now().strftime('XI:%M %p')
    talk('Current time is '+ time)
elif 'who the heck is' in command:
    person = command.replace('who the heck is', '')
    info
elif 'date' in command:
    talk('sorry, I have a headache')
elif 'are you single' in command:
    talk('I am in a relationship with wifi')
elif 'joke' in command:
    talk(pyjokes.get_joke())
else:
    talk('Please say the command again.')


while True:
    run_alexa()