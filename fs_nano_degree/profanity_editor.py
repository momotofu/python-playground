from urllib.request import urlopen
from urllib.parse import urlencode

def read_text():
    text =  open("./movie_text.txt")
    contents_of_file = text.read()
    text.close()
    return contents_of_file

def check_profanity(text_to_check):
    is_profane = False
    params = urlencode({'q': text_to_check})
    connection = urlopen("http://www.wdylike.appspot.com/?q="+params);
    is_profane = connection.read().decode("utf-8") == 'true'
    connection.close()
    return is_profane

def print_response(input):
    if input:
        print("Oh no! There is something profane in your text!")
    else:
        print("All clear. Nothing profane!")
content = read_text()
print_response(check_profanity(content))
# check_profanity(read_text())
