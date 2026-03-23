# API Test Automation Script
# Author: Raghavendra HK
# Purpose: Automatically test API endpoints and report results

# import required libraries for API testing
import requests
import json
import time

# base URL for JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

# function to test if API endpoint returns status 200
def test_api_endpoint(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Test Passed: {endpoint} returned status 200")
    else:
        print(f"Test Failed: {endpoint} returned status {response.status_code}")
        # function to test if response contains expected data fields
def test_api_response_fields(endpoint, expected_fields):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            data = data[0]  # check the first item in the list
        missing_fields = [field for field in expected_fields if field not in data]
        if not missing_fields:
            print(f"Test Passed: {endpoint} contains all expected fields")
        else:
            print(f"Test Failed: {endpoint} is missing fields: {missing_fields}")
    else:
        print(f"Test Failed: {endpoint} returned status {response.status_code}")

        # function to test response time is under 2 seconds
def test_api_response_time(endpoint, max_time=2):
    url = f"{BASE_URL}/{endpoint}"
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = end_time - start_time
    if response_time < max_time:
        print(f"Test Passed: {endpoint} has response time {response_time:.2f} seconds")
    else:
        print(f"Test Failed: {endpoint} has response time {response_time:.2f} seconds")

        # function to test if invalid endpoint returns 404
def test_invalid_endpoint(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 404:
        print(f"Test Passed: {endpoint} returned status 404 for invalid endpoint")
    else:
        print(f"Test Failed: {endpoint} returned status {response.status_code} for invalid endpoint")

# function to run all tests and print a summary report
def run_all_tests():
    print("Running API Tests...")
    test_api_endpoint("posts")
    test_api_response_fields("posts", ["id", "title", "body"])
    test_api_response_time("posts")
    test_invalid_endpoint("invalid-endpoint")
    print("API Tests completed.")
if __name__ == "__main__":
    run_all_tests()

    

