from .api_request import Api
from .twocheckout import Twocheckout


class Company(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def retrieve(cls, params=None):
        if params is None:
            params = dict()
        url = 'acct/detail_company_info'
        response = cls(Api.call(url, params, http_method='GET'))
        return response.vendor_company_info

