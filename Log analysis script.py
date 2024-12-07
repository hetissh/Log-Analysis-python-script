import re
import pandas as pd
from collections import Counter, defaultdict

# Configurable threshold for failed login attempts
FAILED_LOGIN_THRESHOLD = 10

# Function to parse log file
def parse_log(file_path):
    ip_request_count = Counter()
    endpoint_count = Counter()
    failed_logins = defaultdict(int)

    with open(file_path, 'r') as log_file:
        for line in log_file:
            # Extract IP addresses
            ip_match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
            if ip_match:
                ip_address = ip_match.group()
                ip_request_count[ip_address] += 1

            # Extract endpoints (assumes logs have "GET /endpoint HTTP" format)
            endpoint_match = re.search(r'GET (\S+) HTTP', line)
            if endpoint_match:
                endpoint = endpoint_match.group(1)
                endpoint_count[endpoint] += 1

            # Detect failed logins (e.g., status code 401 or "Invalid credentials")
            if '401' in line or 'Invalid credentials' in line:
                if ip_match:
                    failed_logins[ip_address] += 1

    return ip_request_count, endpoint_count, failed_logins

# Function to output results
def save_results(ip_requests, endpoints, failed_logins, output_path):
    # Prepare data for each category
    ip_df = pd.DataFrame(ip_requests.items(), columns=['IP Address', 'Request Count']).sort_values(
        by='Request Count', ascending=False
    )

    most_accessed_endpoint = endpoints.most_common(1)[0]
    endpoint_df = pd.DataFrame(
        {'Endpoint': [most_accessed_endpoint[0]], 'Access Count': [most_accessed_endpoint[1]]}
    )

    suspicious_activity = {ip: count for ip, count in failed_logins.items() if count > FAILED_LOGIN_THRESHOLD}
    suspicious_df = pd.DataFrame(
        suspicious_activity.items(), columns=['IP Address', 'Failed Login Count']
    )

    # Save each category to the same CSV file, separated by blank lines
    with open(output_path, 'w', newline='') as f:
        f.write("Requests per IP\n")
        ip_df.to_csv(f, index=False)
        f.write("\n\nMost Accessed Endpoint\n")
        endpoint_df.to_csv(f, index=False)
        f.write("\n\nSuspicious Activity\n")
        suspicious_df.to_csv(f, index=False)

# Main function
if __name__ == "__main__":
    log_file_path = 'sample.log'  # Replace with your log file path
    output_csv_path = 'log_analysis_results.csv'

    ip_requests, endpoints, failed_logins = parse_log(log_file_path)
    save_results(ip_requests, endpoints, failed_logins, output_csv_path)

    print(f"Log analysis results saved to {output_csv_path}")
