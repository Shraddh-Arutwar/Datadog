#############################################################
#            Datadog Teamcenter Log Monitors Creation       #
#############################################################

# This Script Contains monitor Creation for:
# 1. FSC log Monitoring 
# 2. Web log Monitoring
# 3. Pool log Monitoring 
############################################################# 

from datadog import api,initialize

options = {
    'api_key': '<api_key>',
    'app_key': '<app_key>'
}

initialize(**options)

# Create a new monitor
monitor_options = {
    "notify_no_data": False
}
tags = ["datadog:True", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="log alert",
    query="logs(\"source:java service:<service_name> status:(error OR warn OR critical)\").index(\"*\").rollup(\"count\").last(\"15m\") >= 2",
    name="<Project> - <Application> - <env> - Warning/Error/Critical  Message detected in the <Service> Logs!!!",
    message="  \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"thresholds": {
			"critical": 2,
			"warning": 1
		},
		"new_host_delay": 300,
		"queryConfig": {
			"logset": {
				"name": "*"
			},
			"track": "logs",
			"timeRange": {
				"to": 1594146980936,
				"live": True,
				"from": 1594101980936
			},
			"queryString": "source:java service:<service> status:(error OR warn OR critical)",
			"indexes": [
				"*"
			],
			"queryIsFailed": False
		},
		"notify_no_data": False,
		"renotify_interval": 0,
		"groupby_simple_monitor": False,
		"enable_logs_sample": True,
		"aggregation": {
			"metric": "count",
			"type": "count",
			"groupBy": ""
		}
	}
)
