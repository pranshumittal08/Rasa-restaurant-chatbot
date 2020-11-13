
## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- ty
- thankyou


## intent:goodbye
- good afternoon
- cu
- good by
- cee you later
- good night
- bye
- goodbye
- have a nice day
- see you around
- bye bye
- see you later


## intent:greet
- hey
- hello
- hi
- hello there
- hi there
- good morning
- good evening
- wassup
- hey there
- ssup
- hey dude
- morning
- hola
- evening
- good afternoon
- whats up

## intent:restaurant_search

- i am looking for some restaurants
- i looking for some restaurants nearby
- i am looking for some good restaurants
- i looking for some decent restaurants
- I am looking for some restaurants in [Bangalore](location)
- i am looking for an [north indian](cuisine) restaurant
- I’m hungry. Looking out for some good restaurants
- I am looking for [chinese](cuisine) restaurants in [jaipur](location)
- I am looking for some restaurants in [Delhi](location).
- I am looking a restaurant in south [delhi](location:Delhi)
- I am looking for [mexican](cuisine) food joints 
- I am looking for a good restaurant to eat
- I am looking for some [american](cuisine) restaurants
- i am looking for some restaurants that serve [italian](cuisine) cuisine
- i am looking for some good restaurants in [amritsar](location) 
- show me [chinese](cuisine) restaurants 
- show me some [chines](cuisine:chinese) restaurants in [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in [surat](location) 
- please find me [chinese](cuisine) restaurant in [delhi](location)
- Please find me a restaurantin [bangalore](location)
- can you find me a cheap [chinese](cuisine) restaurant 
- please help me to find restaurants in [pune](location)
- please find me a restaurant in [ahmedabad](location) that is not too expensive
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- Help me find a good restaurant to eat.
- suggest me some restaurants
- suggest me some restaurants in [new delhi](location:Delhi)
- suggest me some good [chinese](cuisine) restaurants
- can you show me some restaurants in [meerut](location)
- can you suggest me some good [north indian] restaurants in [kanpur](location)
- I want some restaurant suggestions in [ranchi](location)
- I want some restaurant suggestions in [bombay](location:Mumbai)
- I need you to suggest me some good [north indian](cuisine) restaurants nearby 
- I am searching for a diner spot in [dilli](location:Delhi)
- I wanna grab dinner. can you suggest me some good [south indian](cuisine) places to eat
- I am famished. Find me some nice place to eat in [raipur](location)
- Give me some decent recommendations for [mexican](cuisine) restaurants in [patna](cuisine)
- I am in [varanasi](location). Can you suggest me some good [north indian](cuisine) 
- Recommend me some luxury dinings in [bangalore](location)
- recommend me some good [chnese](cuisine:chinese) restaurants for [chennai](location) location
- Fine dining for two in [cochin](location) location
- I am hungry. show me some good [mexican] restaurants in [jodhpur](location)
- I am hungry. Looking for some good restaurants.
- anywhere in the [west](location)
- anywhere in [patiala](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- [central](location) [indian](cuisine) restaurant
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [madras](location:Chennai)
- [puna](location:Pune)
- [baroda](location:Vadodra)
- [ooty](location:Cochin)
- [Italian](cuisine)
- [delhi](location)
- I'd prefer [italian](cuisine)
- i want [chinese](cuisine)
- i want to have [north indian](cuisine)
- Okay. Show me some in [Allahabad](location)
- what about in [dehradun](location)
- and what about in [agra](location)
- okay no problem. show me in [ludhiana](location)


## intent:price_range
- [500](budget_min) to [600](budget_max)
- between [400](budget_min) and [500](budget_max)
- more than [300](budget_min)
- >[700](budget_min)
- > [300](budget_min)
- <[300](budget_max)
- < [700](budeget_max)
- in the range [300](budget_min) to [700](budget_max)
- between [700](budget_min) and [1000](budget_max)
- i'd prefer below [300](budget_max)
- under [700](budget_max)
- below [300](budget_max)
- above [300](budget_min)
- over [700](budget_min)
- Less than Rs. [300](budget_max)
- less than [300](budget_max)
- less than [500](budget_max) rs.
- less than rs. [700](budget_max)
- lessthan [300](budget_max)
- lesser than rs. [1000](budget_max)
- lesser than Rs. [100](budget_max)
- lesser than Rs. [599](budget_max)
- lesser than [700](budget_max)
- Rs. [300](budget_min) to [700](budget_max)
- More than Rs. [700](budget_min)
- more than [1000](budget_min) rs.
- more then [300](budget_min) bucks
- morethan [700](budget_min) rs.
- more than rs. [400](budget_min)
- more than rs. [1000](budget_min)

## intent:inform_email
- my email id is [abcd.xyz@gmail.com](email)
- yeah sure! mail me at [rachit_kalra32@gmail.com](email)
- [crazy_beam31@yahoo.co.in](email) is my email
- email me at [duddly_moore786@live.com](email)
- yeah! send me at [dark_knight45@gmail.com](email)
- here is my email address [iron_man3000@yahoo.com](email)
- this is my email [dark_knight45@gmail.com](email)
- mail me at [dark_knight45@gmail.com](email)
- [dark_knight45@gmail.com](email)
- [retro_night34might@yulu.com](email)
- [welltrodden_removeleft98@nedc.nic.in](email)
- [ramir%43@zuul@co.uk](email)

## intent:no_email
- no thanks
- no thats fine
- no, that won't be necessary
- no that is not required
- not required
- not needed
- no do not send a mail
- i dont need them over mail
- please dont send any mail
- dont send any mail
- i don't need any mail
- no i am good
- no

## regex:email
- [A-z0-9.\_%+-]+@[A-z0-9.-]+\\.[A-z.]{2,4}

## regex:cuisine
- an$
-[A-z]+i$


## synonym:4
- four

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## regex:greet
- hey[^\s]*

## synonym:Delhi
- New Delhi
- dilli
- new deli 

## synonym:Bangalore
- Bengaluru

## synonym:Gurgaon
- Gurugram

## synonym:Chennai
- Madras
- chenai
- chenni

## synonym:Mumbai
- Bombai
- bombay
- bumbai

## synonym:vegetarian
- veggie
- veg 
- vegg 

## synonym:non-vegetarian
- non-veg 
- non veg 
- nonveg

## lookup:cuisine
- italian
- mexican
- chinese
- north indian
- south indian
- mediterranean
- dessert
- japanese
- american
