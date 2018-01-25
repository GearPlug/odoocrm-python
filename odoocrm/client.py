from xmlrpc import client
from odoocrm.exceptions import AuthenticationError
import re


class Client(object):
    def __init__(self, url, database, username, password):
        self.url = url
        self.database = database
        self.username = username
        self.password = password

        self.common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = self.common.authenticate(database, username, password, {})
        if uid is False:
            raise AuthenticationError
        self.uid = uid

        self.models = client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def search_partner(self, query, params={}):
        """Takes a mandatory domain filter (possibly empty), and returns the database
        identifiers of all records matching the filter.

        Args:
            query: [[['is_company', '=', True], ['customer', '=', True]]]
            params: {'offset': 10, 'limit': 5}

        Returns: A dict.

        """
        response = self.models.execute_kw(self.database, self.uid, self.password, 'res.partner', 'search', query, params)
        return response

    def read_partner(self, query, params={}):
        """Takes a list of ids and optionally a list of fields to fetch. By default,
        it will fetch all the fields the current user can read, which tends to be a huge amount.

        Args:
            query: [1, 2]
            params: {'fields': ['name', 'country_id', 'comment']}

        Returns: A dict.

        """
        response = self.models.execute_kw(self.database, self.uid, self.password, 'res.partner', 'read', query, params)
        clean_response = {}
        for item in response:
            for k, v in item.items():
                if isinstance(v, list):
                    for obj in v:
                        if isinstance(obj, int) or isinstance(obj, float):
                            v.remove(obj)
                clean_response.update({k: self.clean_string(v)})
        result = clean_response
        return result

    def clean_string(self, string):
        if type(string) != str:
            return string
        return self.strip_string_extra_spaces(string).strip()

    def strip_string_extra_spaces(self, string):
        return re.sub("(?:\s)+", ' ', string)

    def list_fields_partner(self):
        """
            Inspects a model's fields and check which ones seem to be of interest.
        Because it returns a large amount of meta-information (it is also used by client programs)
        it should be filtered before printing, the most interesting items for a human user are string
        (the field's label), help (a help text if available) and type (to know which values to expect,
        or to send when updating a record)

        Returns: A dict.
        """
        response = self.models.execute_kw(self.database, self.uid, self.password, 'res.partner', 'fields_get', [],
                                          {'attributes': ['string', 'help', 'type']})
        return response

    def create_partner(self, data):
        """The method will create a single record and return its database identifier
        .create() takes a mapping of fields to values, used to initialize the record.
        For any field which has a default value and is not set through the mapping argument,
        the default value will be used.

        Returns:

        """
        response = self.models.execute_kw(self.database, self.uid, self.password, 'res.partner', 'create', data)
        return response
