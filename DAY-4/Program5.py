#Shopping cart : add/remove items , display count
Cart = []
while True:
    print("\n-----Sopping Cart Menu-----")
    print("1. add item")
    print("2. Remove item")
    print("3. DisplaY Cart")
    print("4. Display Item Count")
    print("5. Exit")
    choice = input("Enter your choice(1-5) : ")
    if  choice == "1":
       item = input("Enter item to add : ")
       Cart.append(item)
       print((item) , "added to cart.")
    elif choice == "2" :
       item = input("Enter item to remove : ")
       if item in Cart:
        Cart.remove(item)
        print((item) , "removed from cart.") 
       else:
        print("Item not found in cart.")
    elif choice == "3" :
        print("\nItem in Cart : ")
        if len(Cart) == 0 :
         print("Cart is empty.")
        else : 
          for item in Cart :
            print("-", item)
    elif choice =="4" :
      print("Total item in Cart : ", len(Cart))
    elif choice == "5" :
       print("Thankyou for shopping! ")
       break
    else :
       print("Invalid choice. Please try again.")