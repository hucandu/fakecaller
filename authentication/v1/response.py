

class StandardAuthResponse(object):
    """
    Contains all the standard response structure for auth
    service of this api containing major 3 keys [code, status, errors]
    """

    def __init__(self):
        self.core_response = {"code": "","status": "","errors": []}


    def login_success_response(self, token):
        self.core_response["code"] = 200
        self.core_response["status"] = "success"
        self.core_response["token"] = token
        return self.core_response


    def login_failed_response(self, code, errors):
        self.core_response["code"] = code
        self.core_response["status"] = "failed"
        self.errors = errors
        return self.core_response

    def logout_success_response(self):
        self.core_response["code"] = 200
        self.core_response["status"] = "success"
        return self.core_response
