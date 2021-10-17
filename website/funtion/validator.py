import re


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # print ("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        # print ("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        # print ("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip

class Validator:


    def passwordValidator(self, password):
        """
        Declare Min & Max Length of Password 
        to be use to register on the system
        """
        minPassLength = 8
        maxPassLength = 15


        """Check the Strongness of the password"""
        
        regex = ("^(?=.*[a-z])(?=." + "*[A-Z])(?=.*\\d)" + "(?=.*[-+_!@#$%^&*., ?]).+$")
        p = re.compile(regex)
        """Check the length of the password coming"""
        if len(password) >= minPassLength or len(password) <= maxPassLength:

            """Test the password if it's align to regex structure of Variable Character"""

            if (password == None):
                return False

            elif(re.search(p, password)):
                return True
            
            else:
                return False
        else:
            return False