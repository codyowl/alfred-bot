import os.path
import sys
import getpass
import json
from termcolor import colored

USER_NAME = getpass.getuser()

try:
	import apiai
except ImportError:
	sys.path.append(
		os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
	)
	import apiai

CLIENT_ACCESS_TOKEN = '<Your Access Token>'


def main():
	while True:
		ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

		request = ai.text_request()

		request.lang = 'de'  # optional, default value equal 'en'

		# request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
		
		user_query = raw_input("You: ")

		print " "

		request.query = user_query

		response = request.getresponse()

		# print (response.read())

		json_loader = json.load(response)

		responder = json_loader['result']['fulfillment']['speech']

		if "installed" in responder:	
			tool = json_loader['result']['parameters']['language']
			command = '%s -version' % (tool)
			command_executer = os.system(command)
			if command_executer !=0:
				print colored("%s is not installed,let me install that for you master %s" % (tool, USER_NAME), 'blue')

		if "Master" or "master" in responder:
			print "Alfred:" , responder + ' ' + USER_NAME + '!'
			print " "

		elif "installed" in responder:
			tool = json_loader['result']['parameters']['language']
			print tool
			command = '%s -version' % (json_loader['result']['fulfillment'])

		else:
			print "Alfred:" , responder
			print " "	


		


		



if __name__ == '__main__':
	main()
