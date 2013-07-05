from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage

flow = flow_from_clientsecrets("client_secrets.json",
                           scope='',
                           redirect_uri='https://prevoz.org/simple/login/success/')

auth_uri = flow.step1_get_authorize_url()
print "Please visit:\n\n\t", auth_uri, '\n'

print """Enter code that you got redirected to, e.g. if code were:
	https://prevoz.org/simple/login/success/?code=abcdfg123456789010

	You would enter: abcdfg123456789010

Code:""",
code = raw_input()

credentials = flow.step2_exchange(code)

storage = Storage('credentials.json')
storage.put(credentials)
