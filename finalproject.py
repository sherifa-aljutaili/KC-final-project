

password = "welcom"

business_owners = ["asmaa mal allah", "sherifa aljutaili", "mohammad saleh"]
all_business = ["asmaa`s caffee", "shosho potata", "M toys"]



asmaas_caffee = ["croissant", "Latte", "Espresso", "Mocha", "cookies"]
shosho_potata = ["roasted potata", "Mashed potatas", "French fries", "zinger potata", "Hash brown"]
m_toys = ["Barbie dolls", "cars", "play dough", "cooking toys", "Costumes", "Nerf guns", "toddlers toys"]

back = "back"

while back == "back" :
   are_you_a_business_owner = input("* Are you a business owner or a buyer or the app owner?..........")
   if are_you_a_business_owner == "app owner" : 
       print("_______________________________________________")
       password = input("* Enter the password..........")
       if password == "welcom" :
          print("_______________________________________________")
          print("Business owners are:")
          print(business_owners)
          print('Businesses on your site :')
          print(all_business)
       else :
          print("_______________________________________________")
          print(" **wrong password** ")
          password = input("* Enter the right password or type [back] to go back to the Previous page..........")
          if password == "welcom" :
             print("Business owners are:")
             print(business_owners)
             print('Businesses on your site :')
             print(all_business)
          elif password == "back" :
             are_you_a_business_owner = input("* are you a business owner or a buyer or the app owner?..........")
          else :
             print("Error")
             are_you_a_business_owner = input("* Are you a business owner or a buyer or the app owner?..........")
          
        


   elif are_you_a_business_owner == "business owner" :
       business_owner = input("* what is your name?..........")
       business_owners.append(business_owner)
       business_name = input("* what is your business name?..........")
       all_business.append(business_name)
       phone_num = input("enter your phone number..........")
       description = input("* how would you describe your business ? ..........")
       print("_______________________________________________")
       print("* Your business will be reviewed and a response will be sent to the number you left..........")
       print("_______________________________________________")
       back = input("* type [back] to go back to the Previous page..........")

        

   elif are_you_a_business_owner == "buyer" :
       print("_______________________________________________")
       print("* welcom to our small busness world..........")
       print("* What account whould you like to check ? ")
       print(all_business)
       i_want_to_check = input("................")
       print("_______________________________________________")
       if i_want_to_check == "asmaa`s caffee" :
          print("* we have : ")
          print(asmaas_caffee)
          print("* call [1355365] to order")
       elif i_want_to_check == "shosho potata":
          print("* we have : ")
          print(shosho_potata)
          print("* call [7678769] to order")
       elif i_want_to_check == "M toys" :
          print("* we have : ")
          print(m_toys)
          print("* call [3454344] to order")
       else :
          print("Error")
    





   else :
       print("Error")
       are_you_a_business_owner = input("* Are you a business owner or a buyer or the app owner?..........")
































are_you_a_business_owner = input("* Are you a business owner or a buyer or the app owner?..........")

if are_you_a_business_owner == "app owner" :
    print("_______________________________________________")
    password = input("* Enter the password..........")
    if password == "welcom" :
       print("_______________________________________________")
       print("Business owners are:")
       print(business_owners)
       print('Businesses on your site :')
       print(all_business)
       back = input("* type [back] to go back to the Previous page..........")
    else :
       print("_______________________________________________")
       print(" **wrong password** ")
       password = input("* Enter the right password or type [back] to go back to the Previous page..........")
       if password == "welcom" :
          print("_______________________________________________")
          print("Business owners are:")
          print(business_owners)
          print('Businesses on your site :')
          print(all_business)
       elif password == "back" :
          back = input("* type [back] to go back to the Previous page..........")
       else :
          print("Error")
          back = input("* type [back] to go back to the Previous page..........")
          
        


elif are_you_a_business_owner == "business owner" :
    business_owner = input("* what is your name?..........")
    business_name = input("* what is your business name?..........")
    description = input("* how would you describe your business ? ..........")
    print("_______________________________________________")
    print("* Your business will be reviewed and a response will be sent to the number you left..........")
    business_owners.append(business_owner)
    all_business.append(business_name)
    print("_______________________________________________")
    back = input("* type [back] to go back to the Previous page..........")

elif are_you_a_business_owner == "buyer" :
   print("_______________________________________________")
   print("* welcom to our small busness world..........")
   print("* What account whould you like to check ? ")
   print(all_business)
   i_want_to_check = input("................")
   back = input("* type [back] to go back to the Previous page..........")
   print("_______________________________________________")
   if i_want_to_check == "asmaa`s caffee" :
      print("* we have : ")
      print(asmaas_caffee)
      print("* call [1355365] to order")
      back = input("* type [back] to go back to the Previous page..........")
   elif i_want_to_check == "shosho potata":
      print("* we have : ")
      print(shosho_potata)
      print("* call [7678769] to order")
      back = input("* type [back] to go back to the Previous page..........")
   elif i_want_to_check == "M toys" :
      print("* we have : ")
      print(m_toys)
      print("* call [3454344] to order")
      back = input("* type [back] to go back to the Previous page..........")
   else :
      print("Error")
      back = input("* type [back] to go back to the Previous page..........")
    





else :
   print("Error")
   back = input("* type [back] to go back to the Previous page..........")
