sens = None
while sens not in ['low', 'medium', 'high']:
    sens = input('Please choose a sensitivity (low, medium, high): ')


web = None
while type(web) != type(5):
    try:
        web = int(input('Please type which webcam you are using (usually 0 or 1 for front webcam): '))
    except:
        pass

rmode = None
while rmode not in ['read', 'media']:
    rmode = input('Please choose a mode (read or media): ')

settings = open('settings.txt', 'w')
settings.write(sens+"\n"+str(web)+"\n"+rmode)
settings.close()