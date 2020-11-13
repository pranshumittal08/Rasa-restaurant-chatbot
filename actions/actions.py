from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import zomatopy
import json
from email.message import EmailMessage
import requests
import smtplib
email_res = []

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
		config= {"user_key":"c021e17456f14a6acfad27e5019aee36"}

		zomato = zomatopy.initialize_app(config)

		#Getting the location, cuisine and budget from the tracker
		loc = tracker.get_slot('location').lower()
		cuisine = tracker.get_slot('cuisine').lower()
		budget_min = int(tracker.get_slot('budget_min'))
		budget_max = int(tracker.get_slot("budget_max"))

		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		
		lat=d1["location_suggestions"][0]["latitude"] #latittude
		lon=d1["location_suggestions"][0]["longitude"] #longitude
		
		cuisines_dict={'american': 1, 'chinese': 25, 'italian': 55, 'mexican': 73,'north indian':50,'south indian':85}
		
		#getting the restaurants as per the preferences
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
		d = json.loads(results)
		response=""

		if d['results_found'] == 0:
			dispatcher.utter_message("Sorry! I could not find any suitable restaurants as per your preferences.\n")

		else:

			price_range = [1] #Setting the price range
			if budget_min == 300 and budget_max == 700:
				price_range = [2]
			elif budget_min == 10000:
				price_range = [3,4]

			#Filtering the list of restaurants based on the price range and storing in a list	
			res_recom =	[res for res in d['restaurants'] if res['restaurant']['price_range'] in price_range] 

			#sorting the restaurants based on the user ratings
			res_recom_sorted = sorted(res_recom, key = lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse = True)

			global email_res				

			res_response = [res for index, res in enumerate(res_recom_sorted) if index <= 4] #List of restaurants to display

			email_res = [res for index, res in enumerate(res_recom_sorted) if index < 10] #List of restaurants to send over email

			#Getting the response in a string
			for index, restaurant in enumerate(res_response):

				response= response + str(index) + ". " + restaurant['restaurant']['name']+ " at "+ \
				restaurant['restaurant']['location']['address'] + " has been rated " +\
				str(restaurant["restaurant"]['user_rating']['aggregate_rating']) + "\n\n"
		
			dispatcher.utter_message("------Here are some recommendations for you!------\n"+response)
		return [SlotSet('location',loc)]

# Class to verify the location
class ActionVerifyLocation(Action):

	#def __init__(self):
    	
	

	def name(self):
		
		return 'action_verify_location'

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain):

		tier_1 = ['ahmedabad','bangalore','chennai','delhi','hyderabad','kolkata','mumbai','pune']
		tier_2 = ['agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 
        'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 
        'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati', 
        'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 
        'kanpur', 'kakinada', 'kochi', 'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 'malappuram', 
        'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 
        'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar', 'sultanpur', 
        'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 
        'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal']

		loc = tracker.get_slot('location')

		if (loc.lower() not in tier_1) and (loc.lower() not in tier_2):
			dispatcher.utter_message("Sorry! We do not serve in this location at present, please try some other region!"+ "\n")
			return [SlotSet("location", None),SlotSet("location_ok", False)]
		else:
			return [SlotSet("location", loc), SlotSet("location_ok", True)]
		

## Class to verify cuisine
class ActionVerifyCuisine(Action):
		
	def name(self):
		return 'action_verify_cuisine'

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
		
		cuisines = ['american', 'chinese', 'italian', 'mexican', 'north indian','south indian']

		cuisine_selected = tracker.get_slot('cuisine')
		if cuisine_selected.lower() in cuisines:
			return [SlotSet('cuisine', cuisine_selected), SlotSet('cuisine_ok', True)]
		else:
			dispatcher.utter_message("Sorry! Please provide a valid cuisine option."+"\n")
			return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]

# Class to verify budget
class ActionVerifyBudget(Action):

	def name(self):
		return 'action_verify_budget'

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

		cost_min = None
		cost_max = None

		try:
			cost_min = int(tracker.get_slot('budget_min'))
			cost_max = int(tracker.get_slot("budget_max"))
		except ValueError:
			dispatcher.utter_message("Sorry! I can not understand. Please re-enter your preferred price range!")
			return [SlotSet('budget_min', None), SlotSet('budget_max', None), SlotSet("budget_ok", False)]			
		
		if cost_max == 300:
			cost_min = 0
			cost_max = 300

		elif cost_max == 700 or cost_min == 300:
			
			cost_min = 300
			cost_max = 700

		elif cost_min == 700:
			cost_min = 700
			cost_max = 10000
		
		else:
			dispatcher.utter_message("Sorry! I can not understand. Please select a price range from the given options!")

		return [SlotSet('budget_min', cost_min), SlotSet('budget_max', cost_max), SlotSet("budget_ok", True)]


# Send email
class ActionSendEmail(Action):

	def name(self):
		return "action_send_email"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
			# Get user's email id
		to_email = tracker.get_slot('email')

        # Get location and cuisines to put in the email
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
        
		global email_res
        
		email_res_count = len(email_res)
        # Construct the email 'subject' and the contents.
		email_subj = "Top " + str(email_res_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
		email_msg = "Hi there! Here are the " + email_subj + "." + "\n" + "\n" +"\n"
		for restaurant in email_res:
		    email_msg = email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" +"\n"

        # Open SMTP connection to our email id.
		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.starttls()
		s.login("rasa.bot.upgrad@gmail.com", "learnrasa")

        # Create the msg object
		msg = EmailMessage()

        # Fill in the message properties
		msg['Subject'] = email_subj
		msg['From'] = "rasa.not.upgrad@gmail.com"

        # Fill in the message content
		msg.set_content(email_msg)
		msg['To'] = to_email

		s.send_message(msg)
		s.quit()
		dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
		return
