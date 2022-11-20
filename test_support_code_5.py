import json


# RULE: name all json objects with json_ prefix
json_data_of_login =  """
{ 
    "User_id":"g2tech", 
    "Password":"password"
}"""

#client_socket.send(json_data_of_login)

# parse json data---> this will be used at server side to decode(de-jsonify) message:
parsed_login_data = json.loads(json_data_of_login)

# the result is a Python dictionary:
print(parsed_login_data["User_id"])
print(parsed_login_data["Password"])