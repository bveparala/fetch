# HTTP Endpoint Health Checker

This Python script is designed to check the health of a set of HTTP endpoints specified in a YAML configuration file. It performs periodic health checks, logs the availability percentages for each domain after each test cycle, and continues until the user manually exits the program.

# Dependencies

yaml: For parsing YAML configuration files.
requests: For making HTTP requests.
time: For introducing delays between test cycles.
collections.defaultdict: For efficiently managing the results of health checks.

Install dependencies:
pip install requests 
pip install PyYAML

# Usage

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script: cd health_check
3. Run the script by entering the following command: python health_check.py
4. Enter the path to the YAML configuration file when prompted.
5. The program will start performing health checks every 15 seconds. Press Ctrl+C to exit the program.


# Logging
After each test cycle, the script logs the availability percentages for each domain to the console.
The output includes the test cycle number, domain names, and their corresponding availability percentages.

# Exiting the Program
Press CTRL+C to manually exit the program