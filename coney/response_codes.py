

class ResponseCodes(object):
    SUCCESS = 0

    USER_CODE_START = 1
    USER_CODE_END = 0x7fffffff

    RESERVED_CODE_START = 0x80000000
    MALFORMED_RESPONSE = RESERVED_CODE_START
    MALFORMED_REQUEST = RESERVED_CODE_START + 1
    REQUEST_ENCODING_FAILURE = RESERVED_CODE_START + 2
    REMOTE_UNHANDLED_EXCEPTION = RESERVED_CODE_START + 3
    CALL_REPLY_TIMEOUT = RESERVED_CODE_START + 4
    METHOD_NOT_FOUND = RESERVED_CODE_START + 5
    VERSION_NOT_FOUND = RESERVED_CODE_START + 6
    UNEXPECTED_DISPATCH_EXCEPTION = RESERVED_CODE_START + 7

    RESERVED_CODE_END = 0xffffffff

    _desc = {
        SUCCESS: 'Success',
        MALFORMED_RESPONSE: 'Response message was malformed',
        MALFORMED_REQUEST: 'Request message was malformed',
        REQUEST_ENCODING_FAILURE: 'The data in the request could not be encoded',
        REMOTE_UNHANDLED_EXCEPTION: 'An unhandled exception occurred while processing the remote call',
        CALL_REPLY_TIMEOUT: 'The request did not receive a reply within the call timeout',
        METHOD_NOT_FOUND: 'The requested method is not supported by the server',
        VERSION_NOT_FOUND: 'The requested method version is not supported by the server',
        UNEXPECTED_DISPATCH_EXCEPTION: 'An unexpected exception occurred during message dispatch'
    }

    @staticmethod
    def describe(code):
        try:
            return ResponseCodes._desc[code]
        except KeyError:
            if ResponseCodes.USER_CODE_START >= code <= ResponseCodes.USER_CODE_END:
                return 'RPC endpoint specific error response'
            else:
                return 'Unknown response code'


