import requests
import json

base_url = "https://10.215.26.122/api/v1"
def ticket():
  url = base_url + '/ticket'
  header = {
    "Content_Type":"application/json"
  }

  body ={
      "username": "admin",
      "password": "vnpro@149"
  }
  json_body = json.dumps(body)

  Response = requests.post(url, headers=header, data=json_body, verify=False)
  print(Response.text)
  print(Response.json())
  my_ticket = response.json()["response"]["serviceTicket"]
  return my_ticket

def net_network_device():
  url = base_url + '/network-device'
  header = {
    "Content_Type": "application/json"
    "x-Auth-Token": ticket()
  }
  response = requests.get(url, headers=header, verify=False)
  data = response.json()
  print(json.dumps(data_dict, indent=4))


if __name__ == "__main__":
  ticket()
  net_network_device()


