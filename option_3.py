#Creating a function for returning borrowed books
def returns(book_id, list1, return_days):
    temporary=[]
    for items in list1:
        if items[0]==book_id:
            #Adding in the return cart
            for values in items:
                temporary.append(values)

            #Calculating the Fine
            if return_days>10:
                Fine= (return_days-10)*(0.10*float(items[-1][1:]))
            else:
                Fine=0

            #Adding the Calculated Fine and Number of days borrowed
            temporary.append(Fine)
            temporary.append(return_days)

            #Increasing the stock value by one
            items[-2]=str(int(items[-2])+1)

    return temporary
