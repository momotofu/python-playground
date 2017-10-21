#comments
#count time
import time
import webbrowser


url='https://www.google.co.jp/search?q=cute+pomeranian&safe=active&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiWzIXK8f7WAhUMwrwKHUhsBhoQ_AUICigB&biw=1440&bih=777'

# repeat open a window every one hour ten times
pie=5


while pie > 0:
    webbrowser.open(url)
    time.sleep(60*60)
    pie = pie - 1
    print("pie: " + str(pie))

#open a window
