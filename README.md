##A simple Pythonic API for Google Identity Toolkit.  No Javascript, No Fluff, No Options -- just Authentication.

Author: Richie Foreman <richie.foreman@gmail.com>

##Usage (psuedo-code):

    # Login Handler

    import git_silent

    git_silent.KEY = "MYAPIKEY"
    auth_url = git_silent.create_auth_url()
    redirect(auth_url)

    # Callback Handler

    uri = request_uri (get this from somewhere in your framework... self.request.uri, or similar)

    assertion = git_silent.verify_assertion(requestUri=url)
    print "Hello, %s %s (%s)" % (assertion["firstName"], assertion["lastName"], assertion["email"])
