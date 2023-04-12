class TestMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.special_object:
            # print("THIS IS SPECIAL REQUEST")
            response["SPECIAL_REQUEST"] = True
        else:
            # print("THIS IS NOT A SPECIAL REQUEST")
            response["SPECIAL_REQUEST"] = False
        return response
