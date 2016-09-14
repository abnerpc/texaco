
class ValidateFileLinesFormatException(Exception):
    def __init__(self, lines):
        message = 'Validation failed for this lines: {}'.format(
            ', '.join([str(l) for l in lines])
        )
        super(ValidateFileLinesFormatException, self).__init__(message)
