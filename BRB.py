# A simple big red button program
# by Marcin Lawniczak
# version 0.1

import android

droid = android.Android()

droid.dialogCreateAlert('Chcesz zagrac?')
droid.dialogSetPositiveButtonText('Tak')
droid.dialogSetNegativeButtonText('Nie')
droid.dialogShow()
result = droid.dialogGetResponse()
wanna_play = result.result['which'] == 'positive'

if wanna_play:
    x = 100
    while x != 0 :        
        droid.dialogCreateAlert(str(x))
        droid.dialogSetPositiveButtonText("Click me!")       
        droid.dialogShow()
        result = droid.dialogGetResponse()
        clicked = result.result['which'] == 'positive'
        if clicked:
            x = x - 1
    droid.notify('Gra BigRedButton','Dzieki za gre!')
    droid.exit()
else:
    droid.notify('Gra BigRedButton','Jeszcze tu wrocisz!')
    droid.makeToast('Szkoda, ze nie zagrasz!')
    droid.exit()
