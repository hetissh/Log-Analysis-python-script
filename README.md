# Log Analysis Python Script

## Overview

The **Log Analysis Script** is a Python tool designed to process web server log files and extract key information. It provides insights into the traffic and security events recorded in the logs by performing data aggregation and analysis efficiently. The results are output to the terminal and saved as a CSV file.

---

## Features

1. **Count Requests Per IP Address**:
   - Aggregates the total number of requests made by each IP address.
   - Displays results in descending order of request count.

2. **Identify the Most Frequently Accessed Endpoint**:
   - Analyzes the log to find the endpoint (URL or resource path) that was accessed the most.
   - Displays the endpoint name and the number of times it was accessed.

3. **Detect Suspicious Activity**:
   - Identifies IP addresses with failed login attempts exceeding a configurable threshold.
   - Flags potential brute force attacks and displays the failed login count.

4. **Export Results to CSV**:
   - Saves all analyzed data to a CSV file for future reference.

---

## Requirements

Ensure you have the following installed:
- Python 3.7 or later
- Required libraries:
  - `pandas`

You can install the necessary library by running:
```bash
pip install pandas
```

---

## How It Works

1. **Log Parsing**:
   - The script reads the log file line by line.
   - Regular expressions are used to extract IP addresses, endpoints, and HTTP status codes.

2. **Data Aggregation**:
   - Uses Python's `Counter` and `pandas` to count occurrences of IP addresses and endpoints.
   - Detects suspicious activity based on failed login attempts (`401` or "Invalid credentials").

3. **Output**:
   - Displays results in the terminal in a structured format.
   - Saves results to a CSV file (`log_analysis_results.csv`).

---

## Steps to Use the Script

### 1. Clone the Repository

```bash
git clone https://github.com/hetissh/log-analysis-python-script.git
cd log-analysis-python-script
```

### 2. Prepare Your Log File

- Place your web server log file (e.g., `sample.log`) in the script's directory.
- Update the script if your log file has a different name or format.

### 3. Run the Script

Run the script by executing the following command:

```bash
python log analysis script.py
```

### 4. View Results

- **Terminal Output**: Key findings (e.g., requests per IP, most accessed endpoint, suspicious activity) will be displayed.
- **CSV Output**: Results are saved to `log_analysis_results.csv` in the same directory as the script.

---

## Example Output

### Terminal

```plaintext
IP Address           Request Count
192.168.1.1          234
203.0.113.5          187

Most Frequently Accessed Endpoint:
/home (Accessed 403 times)

Suspicious Activity Detected:
IP Address           Failed Login Attempts
192.168.1.100        56
203.0.113.34         12
```

### CSV File

Results saved in `log_analysis_results.csv`:

```csv
Requests per IP
IP Address,Request Count
192.168.1.1,234
203.0.113.5,187

Most Accessed Endpoint
Endpoint,Access Count
/home,403

Suspicious Activity
IP Address,Failed Login Count
192.168.1.100,56
203.0.113.34,12
```

---

## Configuration

- **Failed Login Threshold**:
  Modify the threshold for detecting suspicious activity in the script:
  ```python
  FAILED_LOGIN_THRESHOLD = 10  # Default value
  ```

---

## Contributing

Feel free to submit issues or pull requests if you:
- Encounter any bugs
- Want to enhance the script’s functionality

---

## Author

Developed by Hetissh (https://github.com/hetissh)
