def read_text():
   text =  open("./movie_text.txt")
   contents_of_file = text.read()
   print("text:", contents_of_file)
   text.close()
read_text()
