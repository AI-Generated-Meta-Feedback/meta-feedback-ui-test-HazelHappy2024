function sortBooks(bookList):
    #bookList is a lits of (shelfNumber, returnOrder)
    for i from 1 to length(bookList) - 1:
      key = bookList[i]
      j  = i - 1
      #compare shelfNumber first, then returnOrder if same shelf 
      while j >= 0 and (
           bookList[j].shelfNumber > key.shelfNumber or 
            (bookList[j].shelfNumber == key.shelfNumber and 
            bookList[j].returnOrder > key.returnOrder)

      ):
        bookList[j + 1] = bookList[j]
        j = j - 1

      bookList[j + 1] = key

   return bookList

