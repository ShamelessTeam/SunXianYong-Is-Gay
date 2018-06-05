from django.utils.deprecation import MiddlewareMixin
class AddHeader(MiddlewareMixin):
    def process_response(self, request,response):
        response['Access-Control-Allow-Origin']='*'
        response["Access-Control-Allow-Headers"]='Origin, X-Requested-With, Content-Type, Accept'
        response["Access-Control-Allow-Methods"]='GET, POST, PUT,DELETE'
        return response

