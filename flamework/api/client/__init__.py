# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import base64
import json
import logging
import requests

from flamework.api.request import encode_multipart_formdata, encode_urlencode

class OAuth2:

    def __init__(self, access_token, **kwargs):

        self.access_token = access_token

        self.hostname = kwargs.get('hostname', None)
        self.endpoint = kwargs.get('endpoint', None)

        if not self.hostname:
            raise Exception, "Missing hostname"

        if not self.endpoint:
            raise Exception, "Missing endpoint"

        logging.debug("setup API to use %s%s" % (self.hostname, self.endpoint))

        self.proxy = kwargs.get('proxy', None)    

        if self.proxy:
            logging.debug("setup API to use proxy %s" % self.proxy)

        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)

    def execute_method(self, method, data, encode=encode_urlencode):

        url, args = self.prepare_request(method, data, encode)

        rsp = requests.post(url, **args)
        return self.parse_response(rsp)

    def prepare_request(self, method, data, encode=encode_urlencode):

        logging.debug("calling %s with args %s" % (method, data))

        data['method'] = method
        data['access_token'] = self.access_token
        
        url = "https://" + self.hostname + self.endpoint + '/'
        logging.debug("calling %s" % url)

        args = encode(data)

        # http://docs.python-requests.org/en/latest/user/advanced/#proxies
        # http://lukasa.co.uk/2013/07/Python_Requests_And_Proxies/

        if self.proxy:
            args["proxies"] = {"https": self.proxy }

        return (url, args)

    def parse_response(self, rsp):

        body = rsp.text
        logging.debug("response is %s" % body)

        try:
            data = json.loads(body)
        except Exception, e:

            logging.error(e)
            logging.debug(body)
            
            error = { 'code': 000, 'message': 'failed to parse JSON', 'details': body }
            data = { 'stat': 'error', 'error': error }

        # check status here...

        return data

    def call (self, method, **kwargs):
        logging.warning("The 'call' method is deprecated. Please use 'execute_method' instead.")
        self.execute_method(method, kwargs)

if __name__ == '__main__':

    import sys
    import pprint
    import time
    import optparse

    parser = optparse.OptionParser(usage="python api.py --access-token <ACCESS TOKEN> --hostname <HOSTNAME> --endpoint <ENDPOINT>")

    # sudo make me read a config file...

    parser.add_option('--access-token', dest='access_token',
                        help='Your (Flamework project) API access token',
                        action='store')

    parser.add_option('--hostname', dest='hostname',
                        help='The (Flamework) API hostname you\'re connecting to',
                        action='store', default=None)

    parser.add_option('--endpoint', dest='endpoint',
                        help='The (Flamework) API endpoint you\'re connecting to',
                        action='store', default=None)

    parser.add_option("-v", "--verbose", dest="verbose",
                      help="enable chatty logging; default is false", 
                      action="store_true", default=False)

    options, args = parser.parse_args()
    
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    args = {}

    if options.hostname:
        args['hostname'] = options.hostname

    if options.endpoint:
        args['endpoint'] = options.endpoint

    api = OAuth2(options.access_token, **args)

    try:
        now = int(time.time())
        args = {'foo': 'bar', 'timestamp': now}

        rsp = api.execute_method('api.test.echo', args)
        print pprint.pformat(rsp)

    except Exception, e:
        print e

    sys.exit()
