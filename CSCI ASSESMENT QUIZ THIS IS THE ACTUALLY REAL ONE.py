score=0
point=5


print("hello")

options = ["a","b","c","d"]
quiz1={"What's Taika Waititi's Most Recent Film? a. Jojo Rabbits  b. Thor Love And Thunder c. Next Goal Wins d. Thor Ragnarok":"c",
       "What Part Of NZ Does Taika Waititi Come From? a. auckland b. Wellington c. Invercargill d. Taupō":"b",
       "If Taika Waittit Was Born In 1975 What Age Would He Be This Year? a. 48  b. 45 c. 50 d. 49.":"d",
       "Which is Taika Waitit’s Current Spouse? a. Chelsea Winstanley b. Rita Ora c. Loren Horsley":"b",
       "Which Film Did Taika Waititi Not Direct? a. Avengers Endgame b. Jojo Rabbit c. What We Do In The Shadows  d. Boy":"a",
       "Which Film Of Taika Waititi’s Had A Main Character With The Name Of Ricky Baker?  a. Hunt For Widerpeople b. Hunt For Wildpeople  c. Hunt For The Wilderpeople d. Hunt For The Crazypeople":"c",
       "How Many Children Does Taika Waititi Have? a. 2 b. 3 c. 1 d. 4":"a"}



for x in quiz1:
 print(x) 
 answer=input("Enter Your Answer").lower().strip()
while answer not in options:
     answer=input("Enter Your Answer").lower().strip()

     if answer==quiz1[x]:
      score+=point
      point+=5
    
      print("correct, your score is",score)

     else:
      print ("incorrect")

if score > 35:
  print("you won")

if score < 35:
  print("you lost")
 
          


