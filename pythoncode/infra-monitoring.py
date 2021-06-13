####################################################
#            Datadog Infra Monitors Creation       #
####################################################

# This Script Contains infrastructure monitoring:
# 1. EC2 Host status check
# 2. EC2 Status Check
# 3. System Memory usage - system
# 4. Instanceresources Memory Utilization - aws
# 5. Disk utilization 
# 6. CPU Load
# 7. Application Load Balancer 503 Error Count
# 8. SSL Certification is about to get Expired 
# 9. RDS CPU Utilization 
# 10. RDS Connections 
# 11. RDS Disk Queue Depth
# 12. RDS Free Storage Space
# 13. RDS Read IOPS
# 14. RDS Write IOPS 

# Edit "project:<Project>", "environment:<Env>"] - 15
# Edit project:<project>,environment:<env>} - 17
# Edit name="<Project> - <Application> - <env> - 15
# Edit "Escalation - <Project> - <Application> - <env> - 15
# Edit \n@<DL>", - 26
# Edit \n@<pagerduty-contact>", - 4 
###################################################################### 

from datadog import api,initialize

options = {
    'api_key': '<api_key>',
    'app_key': '<app_key>'
}

initialize(**options)

# 1. Create a new monitor for EC2 Host Status
monitor_options = {
    "notify_no_data": False
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="min(last_30m):avg:aws.ec2.host_ok{datadog:true,project:<project>,environment:<env>}  by {host} < 1",
    name="<Project> - <Application> - <env> - EC2 Host status not OK on {{host.datadog_name}}",
    message="aws.ec2.host_ok: This matric checkes if the instance's system status is ok.  \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 10,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - EC2 Host status not OK on {{host.datadog_name}}  \n@<pagerduty-contact>",
		"thresholds": {
			"critical": 1
    	}
	}
)

# 2. Create a new monitor for EC2 Status
monitor_options = {
    "notify_no_data": False
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="max(last_30m):avg:aws.ec2.status_check_failed{datadog:true,project:<project>,environment:<env>} by {host} > 1",
    name="<Project> - <Application> - <env> - EC2 Status Check Failed on {{host.datadog_name}}",
    message="aws.ec2.status_check_failed: This matric check if the instance has passed the EC2 instance status check. \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 10,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - EC2 Status Check Failed on {{host.datadog_name}}  \n@<pagerduty-contact>",
		"thresholds": {
			"critical": 1
    	}
	}
)

# 3. Create a new monitor for System Memory Utilization
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="avg(last_15m):( avg:system.mem.used{datadog:true,project:<project>,environment:<env>} by {host} - avg:system.mem.cached{datadog:true,project:<project>,environment:<env>} by {host} ) / avg:system.mem.total{datadog:true,project:<project>,environment:<env>} by {host} * 100 >= 95",
    name="<Project> - Teamcenter - <env> - System Memory Usage is very high on {{host.datadog_name}}",
    message=" Memory Usage Is High.\nLinux - free -m(Check the available memory)\nWindows - Check in Task Manager  \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"no_data_timeframe": 30,
		"require_full_window": True,
		"new_host_delay": 300,
		"notify_no_data": True,
		"renotify_interval": 20,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - System Memory Usage is very high on {{host.datadog_name}}  \n@<DL>",
		"thresholds": {
			"critical": 95,
			"warning": 85
    	}
	}
)

# 4. Create a new monitor for  (aws) Memory Utilization
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="avg(last_15m):avg:instanceresources.MemoryUtilization{datadog:true,project:<project>,environment:<env>} by {host} > 95",
    name="<Project> - <Application> - <env> - Instanceresources Memory Utilization is very high on {{host.datadog_name}}",
    message=" Memory Usage Is High.\nLinux - free -m(Check the available memory)\nWindows - Check in Task Manager  \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"no_data_timeframe": 30,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": True,
		"renotify_interval": 20,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - Instanceresources Memory Utilization is very high on {{host.datadog_name}}  \n@<DL>",
		"thresholds": {
			"critical": 95,
			"warning": 85
    	}
	}
)

# 5. Create a new monitor for Disk Utilization
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="min(last_15m):avg:system.disk.in_use{datadog:true,project:<project>,environment:<env>} by {host,device} * 100 >= 95",
    name="<Project> - <Application> - <env> - Disk Space is Low on host {{host.datadog_name}}",
    message=" {{#is_alert}}Disk Space is Critical on Drive {{device}} {{/is_alert}}\n{{#is_warning}}Disk Space is warning on Drive {{device}} {{/is_warning}}\n \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"no_data_timeframe": 30,
		"require_full_window": True,
		"new_host_delay": 300,
		"notify_no_data": True,
		"renotify_interval": 20,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - Disk Space is Low on {{host.datadog_name}}\n \n@<DL>",
		"thresholds": {
			"critical": 95,
			"warning": 85
    	}
	}
)

# 6. Create a new monitor for CPU Load
monitor_options = {
    "notify_no_data": False
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_30m):avg:aws.ec2.cpuutilization{datadog:true,project:<project>,environment:<env>} by {host} >= 95",
    name="<Project> - <Application> - <env> - CPU Load is very High on {{host.datadog_name}}",
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
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 10,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - CPU Load is very High on {{host.datadog_name}}  \n@<DL>",
		"thresholds": {
			"critical": 95,
			"warning": 85
    	}
	}
)


# 7. Create a new monitor for Application Load Balancer 
monitor_options = {
    "notify_no_data": False
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="sum(last_30m):avg:aws.applicationelb.httpcode_elb_5xx{datadog:true,project:<project>,environment:<env>} by {loadbalancer}.as_count() >= 1",
    name="<Project> - <Application> - <env> - Application Load Balancer 5xx Error Count is High on {{loadbalancer.name}}",
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
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 20,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - Application Load Balancer 5xx Error Count is High on {{loadbalancer.name}}  \n@<pagerduty-contact>",
		"thresholds": {
			"critical": 1,
    	}
	}
)


# 8. Create a new monitor for SSL Monitor
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="metric alert",
    query="avg(last_30m):avg:http.ssl.days_left{datadog:true,project:<project>,environment:<env>} <= 30",
    name="<Project> - <Application> - <env> - SSL Certificate is about to get Expired!!!",
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
		"no_data_timeframe": 30,
		"require_full_window": True,
		"new_host_delay": 300,
		"notify_no_data": True,
		"renotify_interval": 1440,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - SSL Certificate is about to get Expired!!!  \n@<DL>",
		"thresholds": {
			"critical": 30,
			"warning": 60
    	}
	}
)

# 9. Create a new monitor for RDS CPU Utilization
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="max(last_30m):avg:aws.rds.cpuutilization{project:<project>,environment:<env>} by {host} >= 95",
    name="<Project> - <Application> - <env> - RDS CPU Utilization is very High on {{host.dbinstanceidentifier}}",
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
		"no_data_timeframe": 30,
		"require_full_window": True,
		"new_host_delay": 300,
		"notify_no_data": True,
		"renotify_interval": 1440,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - RDS CPU Utilization is very High on {{host.dbinstanceidentifier}}  \n@<DL>",
		"thresholds": {
			"critical": 95,
			"warning": 85
    	}
	}
)

# 10. Create a new monitor for RDS Connections
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="min(last_15m):avg:aws.rds.database_connections{project:<project>,environment:<env>} by {application} >= 220",
    name="<Project> - <Application> - <env> - RDS Connections is very High on {{host.dbinstanceidentifier}}",
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
		"no_data_timeframe": None,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 20,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - RDS Connections is very High on {{host.dbinstanceidentifier}}  \n@<DL>",
		"thresholds": {
			"critical": 220,
			"warning": 200
    	}
	}
)

# 11. Create a new monitor for RDS Disk Queue Depth
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="min(last_30m):avg:aws.rds.disk_queue_depth{project:<project>,environment:<env>} by {application} >= 8",
    name="<Project> - <Application> - <env> - RDS Disk Queue Depth is very High on {{host.dbinstanceidentifier}}",
    message="What is Queue Depth:-\nQueue Depth – The number of I/O requests in the queue waiting to be serviced. These are I/O requests that have been submitted by the application but have not been sent to the device because the device is busy servicing other I/O requests.  \n@<DL>",
    tags=tags,
    options = {
		"notify_audit": False,
		"locked": False,
		"timeout_h": 0,
		"silenced": {
			"*": None
		},
		"include_tags": True,
		"no_data_timeframe": None,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 20,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - RDS Disk Queue Depth is very High on {{host.dbinstanceidentifier}}  \n@<DL>",
		"thresholds": {
			"critical": 8,
			"warning": 6
    	}
	}
)

# 12. Create a new monitor for RDS Free Storage Space
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="max(last_30m):max:aws.rds.free_storage_space{project:<project>,environment:<env>} by {dbinstanceidentifier} <= 10000000000",
    name="<Project> - <Application> - <env> - RDS Free Storage Space is very low on {{dbinstanceidentifier.name}}",
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
		"no_data_timeframe": None,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 20,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - RDS Free Storage Space is very low on {{dbinstanceidentifier.name}}  \n@<DL>",
		"thresholds": {
			"critical": 10000000000,
			"warning": 20000000000
    	}
	}
)

# 13. Create a new monitor for RDS Read IOPS
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="sum(last_30m):avg:aws.rds.read_iops{project:<project>,environment:<env>} by {application}.as_count() >= 3000000",
    name="<Project> - <Application> - <env> - RDS Read IOPS is very High on {{host.dbinstanceidentifier}}",
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
		"no_data_timeframe": None,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 20,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - RDS Read IOPS is very High on {{host.dbinstanceidentifier}}  \n@<DL>",
		"thresholds": {
			"critical": 3000000,
			"warning": 2000000
    	}
	}
)


# 14. Create a new monitor for RDS Write IOPS
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 30
}
tags = ["datadog:true", "project:<Project>", "environment:<Env>"]
api.Monitor.create(
    type="query alert",
    query="sum(last_30m):max:aws.rds.write_iops{project:<project>,environment:<env>} by {application}.as_count() >= 300000",
    name="<Project> - <Application> - <env> - RDS Write IOPS is very High on {{host.dbinstanceidentifier}}",
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
		"no_data_timeframe": None,
		"require_full_window": False,
		"new_host_delay": 300,
		"notify_no_data": False,
		"renotify_interval": 20,
		"evaluation_delay": 900,
		"escalation_message": "Escalation - <Project> - <Application> - <env> - RDS Write IOPS is very High on {{host.dbinstanceidentifier}}  \n@<DL>",
		"thresholds": {
			"critical": 3000000,
			"warning": 2000000
    	}
	}
)






