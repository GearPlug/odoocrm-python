# odoocrm-python

odoocrm is an API wrapper for Odoo CRM written in Python

## Installing
```
pip install git+git://github.com/GearPlug/odoocrm-python.git
```

## Usage
```
from odoocrm.client import Client

client = Client('URL', 'DATABASE', 'USERNAME', 'PASSWORD')
```

Search partner
```
url = client.search_partner([[['is_company', '=', True], ['customer', '=', True]]], {'offset': 10, 'limit': 5})
```

Read partner
```
url = client.read_partner(['1', '2'], {'fields': ['name', 'country_id', 'comment']})
```

## Requirements
- requests

## Tests
```
python tests/test_client.py
```
