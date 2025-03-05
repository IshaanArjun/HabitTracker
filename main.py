# Import necessary libraries
import requests
from datetime import datetime


# Define constants for Pixela API
USERNAME = "[PROVIDE_NAME]"
TOKEN = "[API_TOKEN_FROM_PIXELA]"
GRAPH_ID = "[PROVIDE_NAME_OF_GRAPH]"


# Set endpoint for creating a new user
pixela_endpoint = "https://pixe.la/v1/users"


# Define parameters for creating a new user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# Create a new user (uncomment to run)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Set endpoint for creating a new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


# Define parameters for creating a new graph
graph_params = {
    "id": GRAPH_ID,
    "name": "[PROVIDE_NAME]",
    "unit": "minutes",
    "type": "float",
    "color": "momiji"
}


# Define header with authentication token
header = {
    "X-USER-TOKEN": TOKEN
}


# Create a new graph (uncomment to run)
# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)


# Get today's date
today = datetime.now()


# Set endpoint for adding a new value to the graph
add_value_to_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"


# Define parameters for adding a new value to the graph
add_value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you spend today? Give in number: ")
}


# Add a new value to the graph
response = requests.post(url=add_value_to_graph_endpoint, json=add_value_params, headers=header)


# Check if the request was successful
if response.status_code == 200:
    print("Habit logged successfully! 📝💪\nKeep up the good work! 👍")
elif response.status_code == 400:
    print("Error: Invalid request. Please try again. 🤔")
else:
    print("Error: Failed to log habit. Please try again. 😞")


# Set endpoint for updating a value in the graph
update_value_endpoint = f'{add_value_to_graph_endpoint}/{today.strftime("%Y%m%d")}'


# Define parameters for updating a value in the graph (uncomment to run)
# update_value_params = {
#     "quantity": input("How many minutes did you spend today? Give in number: ")
# }


# Update a value in the graph (uncomment to run)
# response = requests.put(url=update_value_endpoint, json=update_value_params, headers=header)


# Check if the request was successful (uncomment to run)
# if response.status_code == 200:
#     print("Habit updated successfully! 📝🔄\nKeep up the good work! 👍")
# elif response.status_code == 400:
#     print("Error: Invalid request. Please try again. 🤔")
# else:
#     print("Error: Failed to update habit. Please try again. 😞")


# Set endpoint for deleting a value from the graph
delete_value_endpoint = f"{add_value_to_graph_endpoint}/{today.strftime('%Y%m%d')}"


# Delete a value from the graph (uncomment to run)
# response = requests.delete(url=delete_value_endpoint, headers=header)


# Check if the request was successful (uncomment to run)
# if response.status_code == 200:
#     print("Habit deleted successfully! 📝🚮\nYou can start fresh! 🌟")
# elif response.status_code == 400:
#     print("Error: Invalid request. Please try again. 🤔")
# else:
#     print("Error: Failed to delete habit. Please try again. 😞")


# Print a message with a link to view the graph
print(f"Visit https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html to view your graph. 📈")
