import random
continue_ = 'y'
score = 0
print ('Hi and welcome to rock paper scissors !')
print ('1-rock\n 2-paper\n 3-scissors')
while continue_ == 'y' :
 
 choice = int(input(':'))
 ai = random.randint(1, 3)
 
 if choice == 1 :
   if ai == 1 :
     print ('draw ,the bot choose rock')
   elif ai == 2 :
     score = score - 1
     print ('you lose the bot choose paper')
   elif ai == 3 :
     score = score + 1
     print ('you win the bot choose scissors')
 elif choice == 2 :
   if ai == 1 :
    score = score + 1
    print ('you win the bot choose rock')
   elif ai == 2 :
    print ('draw the bot choose paper')
   elif ai == 3 :
    score = score - 1
    print ('you lose the bot choose scissors')
 elif choice == 3 :
   if ai == 1 :
     score = score - 1
     print ('you lose the bot choose rock')
   elif ai == 2 :
     score = score + 1
     print ('you win the bot choose paper')
   elif ai == 3 :
     print ('draw the bot choose scissors')
 elif choice == 99 :
  score = 0
  print ('cheat code activated : back to zero point' )
 else :
  print ('wrong number you have to choose 1 , 2 or 3')
 print (score)
 continue_ = input('''Do you want to continue ?\n y-yes\n n-no\n :''').lower()
 
print ('your final score is', score, 'point(s)')
if score < 0 :
 print ('you lose')
else :
 print ('you win')
