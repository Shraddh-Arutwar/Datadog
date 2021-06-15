# Datadog

This repository you can refer to write YAML files for different services and automate monitor creation using Python Scripting. 
In the yaml folder, you can find examples for YAML file creation for different services. For monitoring different services using Datadog agent you have to files at location <datadog_agent_home>/conf.d/. 
In the pythoncode folder, you can find python code to automate monitor creation. Running the script will execute API calls. 
Prerequisites for running pythoncode - 
1. Create Datadog API-key and app-key: Refer https://docs.datadoghq.com/account_management/api-app-keys/ 
2. Install Pip on your machine
3. Install Python on your machine 
4. Install Datadog module (using pip: pip install Datadog, install from source: python setup.py install)
