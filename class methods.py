class PasswordUtils:
    @staticmethod
    def is_strong(password):
        if len(password)>=8:
            return True
    def generate_hint(self):