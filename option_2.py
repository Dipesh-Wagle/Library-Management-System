#Creating a function for borrowing books
def borrows(book_id, list1):
    b_temp=[]
    for items in list1:
        if items[0]==book_id:
            #Adding in the cart
            for values in items:
                b_temp.append(values)
            #Decreasing the stock value by one
            items[-2]=str(int(items[-2])-1)

    return b_temp
