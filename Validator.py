import locale

class Validator():

    def format_to_int(value):
        try:
            return int(value)
        except Exception:
            return None

    def format_to_float(value):
        value = value.replace(".", "")
        value = value.replace(",", ".")
        try:
            return(float(value))
        except Exception:
            return None

    def format_to_currency(value):
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
        return locale.currency(value, symbol=False, grouping=True)