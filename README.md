# py-flamework-api

Base class for flamework-api derived API classes

## Example

### Simple

```
from flamework.api.client import OAuth2

HOSTNAME='api.collection.cooperhewitt.org'
ENDPOINT='/rest'

TOKEN='S33KR3T'

api = OAuth2(ACCESS_TOKEN, hostname=HOSTNAME, endpoint=ENDPOINT)

method = 'cooperhewitt.labs.whatWouldMicahSay'
args = {}

rsp = api.execute_method(method, args)
print rsp
```

### Subclassing

```
import flamework.api.client

class oauth2_client(flamework.api.client.OAuth2):

      	def __init__(self, token, **kwargs):
		kwargs['hostname'] = 'example.com'
		kwargs['endpoint'] = '/rest'
		flamework.api.client.OAuth2.__init__(self, token, **kwargs)
```

That's it.

## See also

* https://github.com/cooperhewitt/flamework-api
* https://github.com/cooperhewitt/flamework
