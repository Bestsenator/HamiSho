
def verifyPhone(phone):
    if len(phone) != 11:
        return False
    if not phone.startswith('09'):
        return False
    return True
