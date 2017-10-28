from urllib.request import urlopen

def read_text():
    text =  open("./movie_text.txt")
    contents_of_file = text.read()
    text.close()
    return contents_of_file

def check_profanity(text_to_check):
    print(urlopen("http://www.wdylike.appspot.com/?q="+text_to_check).info())
    # return has_profanity

check_profanity('shet')
# check_profanity(read_text())
