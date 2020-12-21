from masterImports import * 

#Recording our audio and returning it as a string
def recordAudio():
    #recording the audio
    r= sr.Recognizer() #creating a recognizer object
    #opening mic, and recording
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
    #Utilize google speech recognition software
    data = ' '
    try:
        data = r.recognize_google(audio)
        #print(f'you said {data}')
    except sr.UnknownValueError:
    #Check for unknown errors
        print('Google Speech Recognition could not understand the audio or there was an unknown error')
        pass
    except sr.RequestError as e:
        print(f'Requests results from Google Speech Recognition service error: {e}')
    return data

print(recordAudio())