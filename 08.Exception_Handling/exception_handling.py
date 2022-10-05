"""
1. Exceptions vs Errors
Errors:
- Program will not execute
- The whole system stops
- Need to be fixed

Exceptions:
- Disturbed flow of the program
- Run-time detected
- Can be handled without stopping the system
- Easier to predict
- Django has exception handler (raise ValidationError), named for information



2. Django Exceptions
Types of Django Exceptions:
- Django core exception
- Django URL resolver exception (ViewDoesNotExist)
- Django Database exception (get => DoesNotExist, MultipleObjectsReturned)

3. Handling Exceptions
- Through middleware :

def handle_exception(get_response)
    def middleware(request):
        response = get_response(request):
        if response.status_code >= 500:
            logging.error("INTERNAL ERROR CUSTOM MSG")
            logging.info()
            logging.critical()
            logging.debug()
            logging.warning()
            return internal_error_view(request) // InternalErrorView.as_view()(request)
    return middleware
4. Django Logger
- Logging the Exceptions (dev information for user behavior, bug fixing)
- Easier troubleshooting
- Django system -> LOGGING = {}
- Local -> Debug and up
- Testing -> Info and up
- Production -> Warning and up

Handlers:
- StreamHandler / FileHandler / AdminEmailHandler(Error or critical)
- Log systems (Graylog)
"""