from random import * 
user_pass = input("Şifrenizi Giriniz: ")
password = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','_','=','+','?',',','.','/','<','>']

guess = ""
while (guess != user_pass):
  guess = ""
  for letter in range(len(user_pass)):
    guess_letter = password[randint(0, 25)]
    guess = str(guess_letter) + str(guess)
  print(guess)

print("Şifreniz: ", guess)
