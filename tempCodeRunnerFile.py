def wishme(): 
    hour=int(datetime.datetime.now().hour)
    
    
    if hour>=0 and hour<12:
        speak("Good morning" +master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" +master)
    else:
        speak("Good Evening" +master)        
