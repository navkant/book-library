
class SpecialObject:
    def __init__(self, value: int):
        self.value = value


class SpecialRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        print(f"{self.__class__.__name__} processing request...")

    def process_response(self, request, response):
        print(f"{self.__class__.__name__} processing response...")

    def __call__(self, request):
        self.process_request(request)
        if request.META.get("HTTP_RANDOM_HEADER"):
            value = request.META.get("HTTP_RANDOM_HEADER")
            request.special_object = SpecialObject(value)
        else:
            request.special_object = None

        response = self.get_response(request)
        self.process_response(request, response)
        return response
