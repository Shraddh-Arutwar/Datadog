####################################################################################
#                     URL Monitoring 
# 1. AWC URL 
# 2. BGS URL 
# 3. GS URL 
# 4. TCRA URL 
#

# Edit "project:<Project>", "environment:<Env>"] - 5
# Edit name="<Project> - <Application> - <env> - 5
# Edit "Escalation - <Project> - <Application> - <env> - 5
# Edit \n@<DL> - 5
# Edit \n@<pagerduty-contact>", - 9
#
# After Monitor creation for URL, Manually change URL to be Monitored on DD.
#####################################################################################  

from datadog import api,initialize

options = {
    'api_key': '<api_key>',
    'app_key': '<app_key>'
}

initialize(**options)


# Create a new monitor for AWC URL 
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 5
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="service check",
    query="\"http.can_connect\".over(\"instance:<instance_name>\",\"url:<URL>\").by(\"host\",\"instance\",\"url\").last(2).count_by_status()",
    name="<Project> - <Application> - <env> - URL is unreachable!!!",
    message=" \n@<DL>  \n@<pagerduty-contact>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"no_data_timeframe": 5,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": True,
		"no_data_timeframe": 5,
		"renotify_interval": 10,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - URL is unreachable!!! \n@<pagerduty-contact>",
		"thresholds": {
			"warning": 1,
			"ok": 1,
			"critical": 2
    	}
	}
)