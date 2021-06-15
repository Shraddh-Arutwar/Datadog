##############################################################
#                     Solr Monitors                    
#                                                      
# It will create 3 minitors which will monitor Solr    
# 1. Solr Total Requests
# 2. Solr Timeout
# 3. Solr errors

# Edit "project:<Project>", "environment:<Env>"] - 4
# Edit project:<project>,environment:<env>} - 4
# Edit name="<Project> - <Application> - <env> - 4
# Edit "Escalation - <Project> - <Application> - <env> - 17
# Edit \n@<DL>", - 6
# Edit \n@<pagerduty-contact>", - 2
##############################################################

from datadog import api,initialize

options = {
    'api_key': '<api_key>',
    'app_key': '<app_key>'
}

initialize(**options)

# Create a new monitor for Solr Total Requests
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_15m):jmx.solr_total_requests{datadog:true,project:<project>,environment:<env>} by {host} > 220",
    name="<Project> - <Application> - <env> - Solr object query total number of Requests is High on {{host.datadog_name}}",
    message="Guideline for Solr Requests is High :\nDescription:  The number of Requests comming on Solr server \nExplanation: The number of Requests comming on Solr server is high \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"no_data_timeframe": 20,
		"require_full_window": True,
		"new_host_delay": 300,
		"notify_no_data": True,
		"renotify_interval": 20,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - Solr object query total number of Requests is High on {{host.datadog_name}} \n@<DL>",
		"thresholds": {
			"critical": 220,
			"warning": 200
    	}
	}
)

# 2. Create a new monitor for Solr Timeout
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_15m):avg:jmx.solr_timeouts{datadog:true,project:<project>,environment:<env>} by {host} > 2",
    name="<Project> - <Application> - <env> - Solr object query Timeout is High on {{host.datadog_name}}",
    message="Guideline for Solr object query Timeout :\nDefinition: Defining the timeout of a query allows to cancel its execution once a certain amount of time has passed since it was started. This helps to protect the database by preventing queries from being stalled. \nExplanation: Define number of query request canceled by solr because of timeout. \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"no_data_timeframe": 20,
		"require_full_window": True,
		"new_host_delay": 300,
		"notify_no_data": True,
		"renotify_interval": 20,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - Solr object query Timeout is High on {{host.datadog_name}} \n@<DL>",
		"thresholds": {
			"critical": 2,
			"warning": 1
    	}
	}
)

# 3. Create a new monitor for Solr errors
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_15m):avg:jmx.solr_errors{datadog:true,project:<project>,environment:<env>} by {host} > 2",
    name="<Project> - <Application> - <env> - Solr object query errors is High on {{host.datadog_name}}",
    message=" \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"no_data_timeframe": 20,
		"require_full_window": True,
		"new_host_delay": 300,
		"notify_no_data": True,
		"renotify_interval": 20,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - Solr object query errors is High on {{host.datadog_name}} \n@<pagerduty-contact>",
		"thresholds": {
			"critical": 2,
			"warning": 1
    	}
	}
)
