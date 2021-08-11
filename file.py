#opening File
def load(filename, mode):
        #Opening a file in read mode 
        book= open(filename, mode)

        #Extracting all the contents as String
        contents= book.read()

        #Closing the file
        book.close()

        #Spliting the contents using '\n' as split points and storing each piece in a book1
        book1= contents.split('\n')
        
        #Now spliting each piece using ',' and appending all pieces in a 2D list named book2
        book2=[]
        for each_item in book1:
                book2.append(each_item.split(","))
        return book2
