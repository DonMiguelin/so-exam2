import psutil
import cli.app
import os
from flask import Flask, request
from slackclient import SlackClient

@cli.app.CommandLineApp
def consumo(app):
    slack_token="xoxp-302533441954-302533442194-351986247988-06cf1a3cf36f2e23a05a5c7d952fb8a0"
    sc=SlackClient(slack_token)
    sc.api_call(
	"chat.postMessage",
	channel="#resultadoalgoritmo",
        text="CPU_Percentage: "+str(psutil.cpu_percent(interval=1, percpu=True))+"\n"+"Virtual Memory: "+str(psutil.virtual_memory())+"\n"+"Swap Memory: "+str(psutil.swap_memory())+"\n"+"Disk Percentage: "+str(psutil.disk_usage('/'))
	)
if __name__ == "__main__":
    consumo.run()
