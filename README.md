![](https://img.shields.io/badge/version-0.1.2-success) ![](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-4B8BBE?logo=python&logoColor=white)
# odoocrm-python
odoocrm is an API wrapper for Odoo CRM written in Python
## Installing
```
pip install odoocrm-python
```
## Usage
```
from odoocrm.client import Client

client = Client('URL', 'DATABASE', 'USERNAME', 'PASSWORD')
```
#### Search partner
```
response = client.search_partner([[['is_company', '=', True], ['customer', '=', True]]], {'offset': 10, 'limit': 5})
```
#### Read partner
```
response = client.read_partner([1, 2], {'fields': ['name', 'country_id', 'comment']})
```
#### Search and Read partner
```
response = client.search_read_partner([[]], {'fields': ['name', 'country_id', 'comment'], "order": "id asc"})
# Get all fields by not sending 'fields' paramater
```
#### Create partner
```
response = client.create_partner([{'name': "John doe",}])
```
#### List fields Partner
```
response = client.list_fields_partner()
```
## Requirements
- requests
## Tests
```
python tests/test_client.py
```
