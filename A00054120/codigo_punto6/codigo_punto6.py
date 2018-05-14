from slackclient import SlackClient
import psutil
import cli.app
import os
from flask import Flask, request

@cli.app.CommandLineApp
def slackLauritaMessage(app):

	slack_token = 'xoxp-357995117347-357398188800-359000702374-6032a62f75213d50a5f5f710654deb94'
	sc = SlackClient(slack_token)
	sc.api_call(
	  "chat.postMessage",
	  channel="#lauramensajes",
	  text="REPORT OF AVAILABILITY\n Virtual memory available: "+str(100-psutil.virtual_memory()[2])+"% \n Swap memory available: "+str(100-psutil.swap_memory()[3])+"% \n Disk available: "+str(100-psutil.disk_usage('/')[3])+"% \n CPU percent: "+str(psutil.cpu_percent())+"% \n Quantity of cores: "+str(psutil.cpu_count())
	)
if __name__ == "__main__":
    slackLauritaMessage.run()
