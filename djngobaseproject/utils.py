from rest_framework.views import exception_handler
from rest_framework.response import Response

from rest_framework.exceptions import APIException
from django.utils.encoding import force_text
from rest_framework import status
import json
def custom_exception_handler(exc, context):
    
    response = exception_handler(exc, context)
    if response is not None:
        if 'username' in response.data:
            return Response({"message":str(response.data['username'][0])}, status=status.HTTP_400_BAD_REQUEST)
        if 'email' in response.data:
            return Response({"message":str(response.data['email'][0])}, status=status.HTTP_400_BAD_REQUEST)
        if 'password' in response.data:
            return Response({"message":str(response.data['password'][0])}, status=status.HTTP_400_BAD_REQUEST)
        if 'non_field_errors' in response.data:
            return Response({"message":str(response.data['non_field_errors'][0])}, status=status.HTTP_400_BAD_REQUEST)
        if 'detail' in response.data:
            return Response({"message":str(response.data['detail'])}, status=status.HTTP_400_BAD_REQUEST)

    return response

def convertJsonToText(err):
    for error in err.values():
        e = str(error[0])
        return (e)
    


class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail):
        if detail is not None:
            self.status_code = status.HTTP_400_BAD_REQUEST
            self.detail = str(detail)
        else: self.detail = {'message': force_text(self.default_detail)}


def get_group_name(obj):
    arr=[]
    for g in obj.groups.all():
        arr.append(g.name)
    return arr



from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings    
#this is your "password/ENCRYPT_KEY". keep it in settings.py file
#key = Fernet.generate_key() 

def encrypt(txt):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        # log the error if any
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None

    

def decrypt(txt):
    try:
        # base64 decode
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")     
        return decoded_text
    except Exception as e:
        # log the error
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None