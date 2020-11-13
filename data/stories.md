## general story
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "amritsar"}
    - slot{"location": "amritsar"}
    - action_verify_location
    - slot{"location": "amritsar"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 0, "budget_max": 300}
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - action_verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "amritsar"}
    - utter_want_email
* affirm
    - utter_ask_email
* inform_email{"email": "doctor_banner@gmail.com"}
    - slot{"email": "doctor_banner@gmail.com"}
    - action_send_email
    - utter_goodbye
    - export

## general story 2
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "amritsar"}
    - slot{"location": "amritsar"}
    - action_verify_location
    - slot{"location": "amritsar"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 300, "budget_max": 700}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "amritsar"}
    - utter_want_email
* no_email    
    - utter_goodbye
* goodbye
    - export

## general story 2
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "amritsar"}
    - slot{"location": "amritsar"}
    - action_verify_location
    - slot{"location": "amritsar"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 300, "budget_max": 700}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "amritsar"}
    - utter_want_email
* no_email    
    - utter_goodbye
* goodbye
    - export
    
## location specified
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 300, "budget_max": 700}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_want_email
* affirm    
    - utter_ask_email
* inform_email{"email": "robert_downey21@gmail.com"}
    - slot{"email": "robert_downey21@gmail.com"}
    - action_send_email
    - utter_goodbye
* goodbye
    - export

## location specified 2
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 0, "budget_max": 300}
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - action_verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_want_email
* no_email   
    - utter_goodbye
* goodbye    
    - export



## cuisine specified 1
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 300, "budget_max": 700}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_want_email
* affirm
    - utter_ask_email
* inform_email{"email": "bruce_wayne1990@gmail.com"}
    - slot{"email": "bruce_wayne1990@gmail.com"}
    - action_send_email    
    - utter_goodbye
* goodbye
    - export

## cuisine specified 2
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 700, "budget_max": 0}
    - slot{"budget_min": 700}
    - slot{"budget_max": 0}
    - action_verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_want_email
* no_email    
    - utter_goodbye
* goodbye    
    - export


## cuisine + location specified 1
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "south indian", "location": "bangalore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bangalore"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - action_verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 300, "budget_max": 700}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_want_email
* affirm
    - utter_ask_email
* inform_email{"email": "bruce_wayne1990@gmail.com"}
    - slot{"email": "bruce_wayne1990@gmail.com"}
    - action_send_email    
    - utter_goodbye
* goodbye
    - export

## cuisine specified 2
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "south indian", "location": "bangalore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bangalore"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - action_verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_budget
* price_range{"budget_min": 300, "budget_max": 700}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_want_email
* no_email    
    - utter_goodbye
* goodbye    
    - export


