from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class AuthenticationFailed(APIException):
    status_code = 401
    default_detail = 'Authentication fail, try again later.'
    default_code = 'Authentication failure'
    
class PermissionDenied(APIException):
    status_code = 403
    default_detail = 'Permission denied,please try again later.'
    default_code = 'Permission denied'  

class ItemNotFound(APIException):
    status_code = 404
    default_detail = 'Item not found, please try again later.'
    default_code = 'Item not found'  
    
