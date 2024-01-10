import yaml
import requests
import time
from collections import defaultdict

def parse_config(file_path):

    # Parse the YAML configuration file and return the list of HTTP endpoints.
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def perform_health_check(endpoint):

    #Perform health check for a given HTTP endpoint. Returns True if the endpoint is UP, False otherwise.
    try:
        response = requests.request(
            method=endpoint.get('method', 'GET'),
            url=endpoint['url'],
            headers=endpoint.get('headers', {}),
            data=endpoint.get('body', '')
        )
        latency = response.elapsed.total_seconds() * 1000  # Convert to milliseconds
        return response.status_code // 100 == 2 and latency < 500
    except requests.RequestException:
        return False

def log_availability_percentages(availability, cycle_count):
  
    #Log the availability percentages for each domain after each test cycle.
    print(f"Test cycle #{cycle_count} begins at time = {cycle_count*15} seconds")
    for domain, results in availability.items():
        total_checks = len(results)
        up_checks = sum(results)
        percentage = (up_checks / total_checks) * 100 if total_checks > 0 else 0
        print(f"{domain} has {round(percentage)}% availability percentage")

def main(file_path):

    #Main function to run the health check program.
    config = parse_config(file_path)
    availability = defaultdict(list)
    cycle_count = 1
    try:
        while True:
            for endpoint in config:
                domain = endpoint['url'].split('//')[1].split('/')[0]
                result = perform_health_check(endpoint)
                availability[domain].append(result)

            log_availability_percentages(availability, cycle_count)
            cycle_count+=1
            time.sleep(15)
            availability.clear()

    except KeyboardInterrupt:
        print("\nProgram exited by the user.")

if __name__ == "__main__":
    file_path = input("Enter the path to the YAML configuration file: ")
    main(file_path)
