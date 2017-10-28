def read_text():
    text =  open("./movie_text.txt")
    contents_of_file = text.read()
    text.close()
    return contents_of_file

def check_profanity(text_to_check):
    has_profanity = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    return has_profanity

read_text()
