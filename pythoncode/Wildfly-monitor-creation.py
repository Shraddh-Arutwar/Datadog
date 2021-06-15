###########################################################
#                     WildFly Monitors                    #
#                                                         #
#  It will create 6 minitors which will monitor WildFliy  #
# 
# 1. Abandoned servers
# 2. Failed Login attempts
# 3. LongRunningRequests
# 4. No Server Available
# 5. Server Common failure
# 6. Number of Pending Requests
###########################################################

from datadog import api,initialize

options = {
    'api_key': '<api_key>',
    'app_key': '<app_key>'
}

initialize(**options)

# Create a new monitor for Abandoned Server 
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_10m):avg:jmx.jboss_abandoned_servers{datadog:true,project:<project>,environment:<env>} by {host} > 5",
    name="<Project> - <Application> - <env> - WildFly number of Abandoned servers is High on {{host.datadog_name}}",
    message="Guideline for Abandoned servers :\nDescription: The web tier was unable to connect to the TCServer that the tree cache indicates is assigned to the session. Alert if number of abandoned servers exceeds this limit for time period (Default: 600 seconds).\nExplanation : The user lost their TCServer process for some reason. When this happens a new TCServer process must be started or simply assigned to the users session.  This can cause performance issues. \nUsage: If this occurs frequently it is an indicator of a bigger issue and root cause analysis should be performed. \n@<DL>",
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
		"renotify_interval": 10,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - WildFly number of Abandoned servers is High on {{host.datadog_name}} \n@<DL>",
		"thresholds": {
			"critical": 5,
			"warning": 3
    	}
	}
)

# Create a new monitor for Failed Login Attempts 
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_10m):avg:jmx.jboss_failed_login_attempts{datadog:true,project:<project>,environment:<env>} by {host} > 10",
    name="<Project> - <Application> - <env> - WildFly Failed Login attempts is High on {{host.datadog_name}}",
    message="Guideline for Failed Login attempts :\nDescription: Excessive failed login attempts have been detected. Alert if number of failed login attempts exceeds this limit during time period (Default: 600 seconds).\nExplanation : Users are unable to login through this web application server.  If this occurs frequently it is an indicator of a bigger issue. \nUsage: Could indicate attempt to infiltrate system via password guesses or stolen SSO Token if number jumps above baseline. \n@<DL>",
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
		"renotify_interval": 10,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - WildFly Failed Login attempts is High on {{host.datadog_name}}. \n@<DL>",
		"thresholds": {
			"critical": 10,
			"warning": 7
    	}
	}
)

# Create a new monitor for Long Running Requests  
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_10m):avg:jmx.jboss_long_running_requests{datadog:true,project:<project>,environment:<env>} by {host} > 10",
    name="<Project> - <Application> - <env> - WildFly number of long running requests is High on {{host.datadog_name}}",
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
		"renotify_interval": 10,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - WildFly number of long running requests is High on {{host.datadog_name}}. \n@<DL>",
		"thresholds": {
			"critical": 10,
			"warning": 7
    	}
	}
)

# Create a new monitor for No Server Available
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_10m):avg:jmx.jboss_no_server_available{datadog:true,project:<project>,environment:<env>} by {host} > 5",
    name="<Project> - <Application> - <env> - WildFly No Server Available is High on {{host.datadog_name}}",
    message="Guideline for Failed Login attempts :\nDescription: The server pool was unable to assign a TCServer. Alert if number exceeds this limit during time period (Default: 600 seconds).\nExplanation : This could point to a communication breakdown between web app server and the pool manager.  It could also indicate that the pool manager is at capacity. \nUsage: Investigate non-zero values May be an infrastructure or capacity issue. \n@<DL>",
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
		"renotify_interval": 10,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - WildFly No Server Available is High on {{host.datadog_name}}. \n@<DL>",
		"thresholds": {
			"critical": 5,
			"warning": 1
    	}
	}
)

# Create a new monitor for Server Common Failure
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_10m):avg:jmx.jboss_server_comm_failure{datadog:true,project:<project>,environment:<env>} by {host} > 5",
    name="<Project> - <Application> - <env> - WildFly Server Common failure is High on {{host.datadog_name}}",
    message="Guideline for Server Common failure :\nDescription: A TCServer has closed a connection without providing a response to the web tier. Alert if number of server COMM_FAILUREs exceeds this limit during time period (Default: 600 seconds).\nExplanation : This could point to a communication breakdown between web app server and the pool manager. \nUsage: Indicates that there is an issue that needs to be investigated if consistently non-zero. \n@<DL>",
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
		"renotify_interval": 10,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - WildFly Server Common failure is High on {{host.datadog_name}}. \n@<DL>",
		"thresholds": {
			"critical": 5,
			"warning": 3
    	}
	}
)

# Create a new monitor for Number of Pending Requests
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_10m):avg:jmx.jboss_number_Pending_requests{datadog:true,project:<project>,environment:<env>} by {host} > 5",
    name="<Project> - <Application> - <env> - WildFly number of Pending requests is High on {{host.datadog_name}}",
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
		"renotify_interval": 10,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - WildFly number of Pending requests is High on {{host.datadog_name}} \n@<DL>",
		"thresholds": {
			"critical": 5,
			"warning": 3
    	}
	}
)

