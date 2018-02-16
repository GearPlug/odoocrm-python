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

Search partner
```
response = client.search_partner([[['is_company', '=', True], ['customer', '=', True]]], {'offset': 10, 'limit': 5})
```

Read partner
```
response = client.read_partner([1, 2], {'fields': ['name', 'country_id', 'comment']})
```

Create partner
```
response = client.create_partner([{'name': "John doe",}])
```

## Requirements
- requests

## Tests
```
python tests/test_client.py
```
