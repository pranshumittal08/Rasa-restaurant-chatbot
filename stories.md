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
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - action_verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "amritsar"}
    - utter_ask_email
* restaurant_search{"email": "doctor_banner@gmail.com"}
    - slot{"email": "doctor_banner@gmail.com"}
    - action_send_email
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
* restaurant_search{"budget_min": "300", "budget_max": "500"}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "500"}
    - action_verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* restaurant_search{"email": "robert_downey21@gmail.com"}
    - slot{"email": "robert_downey21@gmail.com"}
    - action_send_email
    - export


## cuisine specified
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
* restaurant_search{"budget_min": "1300", "budget_max": "2700"}
    - slot{"budget_min": "1300"}
    - slot{"budget_max": "2700"}
    - action_verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* restaurant_search{"email": "bruce_wayne1990@gmail.com"}
    - slot{"email": "bruce_wayne1990@gmail.com"}
    - action_send_email
    - export


## price range specified
* greet
    - utter_greet
    - utter_ask_howcanhelp
* restaurant_search{"budget_min": "700", "budget_max": "1500"}
    - slot{"budget_min": "700"}
    - slot{"budget_max": "1500"}
    - action_verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* restaurant_search{"emailid": "bruce_wayne1990@gmail.com"}
    - slot{"email": "bruce_wayne1990@gmail.com"}
    - action_send_email
    - export

