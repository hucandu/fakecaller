

class SpamAuthResponse(object):
    """
    Contains all the standard response structure for auth
    service of this api containing major 3 keys [code, status, errors]
    """

    def __init__(self):
        self.core_response = {"code": "","status": "","errors": []}


    def spam_success_response(self):
        self.core_response["code"] = 200
        self.core_response["status"] = "success"
        return self.core_response


    def spam_failed_response(self):
        self.core_response["code"] = 500
        self.core_response["status"] = "failed"
        self.core_response["errors"] = "number already marked as spam"
        return self.core_response
