import webbrowser
import time

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=WjZ01FcK0yk")
    break_count++
