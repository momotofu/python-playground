def read_text():
   text =  open("./movie_text.txt")
   contents_of_file = text.read()
   print("text:", contents_of_file)
   text.close()

def check_profanity(text_to_check):
    has_profanity = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)

read_text()
