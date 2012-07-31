import httplib2
import json

http = httplib2.Http()

KEY = "AIzaSyBBPyJTesgJeCeXqTzOG7TxwAj1zkbVWOI"
CREATEAUTHURL_URI = "https://www.googleapis.com/rpc?key=%s"
VERIFYASSERTION_URI = "https://www.googleapis.com/identitytoolkit/v1/relyingparty/verifyAssertion?key=%s"


def create_auth_url(identifier="gmail.com", continueUrl="http://localhost:8080/cb"):
    params = {"identifier": identifier,
              "uiMode": "redirect",
              "continueUrl": continueUrl}

    data = [{"method": "identitytoolkit.relyingparty.createAuthUrl",
             "id": "identitytoolkit.relyingparty.createAuthUrl",
             "params": params,
             "jsonrpc": "2.0",
             "key": "identitytoolkit.relyingparty.createAuthUrl",
             "apiVersion": "v1"}]

    data = json.dumps(data)

    resp, content = http.request(CREATEAUTHURL_URI % KEY,
                                 method="POST",
                                 body=data)

    return str(json.loads(content)[0]["result"]["authUri"])

def verify_assertion(requestUri, postBody="", returnOauthToken=False):
    # a full request uri -- including all the params.
    assert isinstance(requestUri, str)
    # a string postbody -- or just an empty string if this came from a GET
    assert isinstance(postBody, str)
    assert isinstance(returnOauthToken, bool)

    data = {"requestUri": requestUri, "postBody": postBody, "returnOauthToken": returnOauthToken}
    resp, content = http.request(VERIFYASSERTION_URI % KEY,
                                 method="POST",
                                 body=json.dumps(data))

    return json.loads(content)

