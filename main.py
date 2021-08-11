import file
import options
import option_2
import option_3
#welcome Messege
user_name=input("Enter Your name:")
print("Welcome "+user_name+" to Library Management System")
print("****************************************************")
#opening File
file.load
list1=file.load("book.txt","r")

#calling Available Options Function
options.available_option()

#empty Cart
user_cart=[]
user_bcart=[]
option=False
while option==False:
     #Taking available option as input to execute
     option_no=int(input("Enter the option you would like to:"))
     
     #listing the available books
     if(option_no==1):
             print("Book id\t\tBook Name\t\tAuthor\t\t\tPrice")
             for every_item in list1:
                        print(every_item[0]+'\t\t'+every_item[1]+'\t\t'+every_item[2]+'\t\t'+every_item[4])
                        print("---------------------------------------------------------------------------")
             print("****************************************************")  
     elif(option_no==2):
           b_repeat=True
           while b_repeat==True:
                borrow_id=input("Enter the book ID of the book you wish to borrow: ")
                for each_item in list1:
                     if borrow_id==each_item[0]:
                          if int(each_item[3])>0:
                               borrowed_book= option_2.borrows(borrow_id, list1)
                               if len(borrowed_book)>0:
                                             user_bcart.append(borrowed_book)
                                             print("****************************************************")   
                                             print("Book borrowing successful!!")
                               else:
                                    print("sorry!! Invalid Book ID")
                          else:
                              print("Sorry! The requested book is out of stock")
                b_rep_con=input("Would you like to borrow another book(y/n): ")
                if(b_rep_con=="y"):
                     b_repeat=True
                else:
                     b_repeat=False
                     print("The Books borrowed: \n")
                     print(user_bcart)
                     print("****************************************************")
     elif(option_no==3):
             r_repeat=True
             while r_repeat==True:
                  return_id=input("Enter the book ID of the book you wish to return: ")
                  return_days= int(input("Enter the no of days since borrowing the book:"))
                  returned_book= option_3.returns(return_id, list1, return_days)
                  if len(returned_book)>0:
                         user_cart.append(returned_book)
                         print("****************************************************")   
                         print("Book return successful!!")
                  else:
                          print("sorry!! Invalid Book ID")
                  r_rep_con=input("Would you like to borrow another book(y/n): ")
                  if(r_rep_con=="y"):
                     r_repeat=True
                  else:
                     r_repeat=False
                  print("The Books returned: \n")
                  print(user_cart)
                  print("****************************************************")   

     elif(option_no==4):
          file_r= open("Returned note.txt","w+")
          file_r.write("Name: "+user_name+"\n")
          file_r.write("*****************\n")
          file_r.write("Book Name\t\t Author\t\tPrice\t\tDays Borrowed\t\tFine\n")
          total=0
          for et in user_cart:
              total=total+float((et[4][1:]))+(et[5])
              file_r.write(et[1]+"\t\t"+et[2]+"\t\t"+str(et[4])+"\t\t"+str(et[6])+"\t\t"+str(et[5])+"\n")
          file_r.write("\n"+"Total\t\t\t\t\t\t\t\t\t\t"+"$"+str(total))
          file_r.close()


          #note of book borrowed
          file_b= open("Borrowed note.txt","w+")
          file_b.write("Name: "+user_name+"\n")
          file_b.write("*****************\n")
          file_b.write("Book Name\t\t Author\t\t\tPrice\n")
          total=0
          for et in user_bcart:
              total=total+float((et[4][1:]))
              file_b.write(et[1]+"\t\t"+et[2]+"\t\t"+str(et[4])+"\n")
          file_b.write("\n"+"Total\t\t\t\t\t\t\t"+"$"+str(total))
          file_b.close()
          exit()
     else:
          print("****************************************************")
          print("Invalid Input!!")

    
