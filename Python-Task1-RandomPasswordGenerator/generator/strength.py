import math
import string


class PasswordStrength:

    @staticmethod
    def analyze(password):

        if not password:

            return {
                "strength": "No Password",
                "progress": 0,
                "entropy": 0,
                "crack_time": "-"
            }

        charset = 0

        if any(c.islower() for c in password):
            charset += 26

        if any(c.isupper() for c in password):
            charset += 26

        if any(c.isdigit() for c in password):
            charset += 10

        if any(c in string.punctuation for c in password):
            charset += len(string.punctuation)

        entropy = len(password) * math.log2(max(charset, 1))

        # -----------------------------

        if entropy < 28:

            strength = "Weak"
            progress = 0.25
            crack = "Seconds"

        elif entropy < 50:

            strength = "Medium"
            progress = 0.50
            crack = "Minutes"

        elif entropy < 75:

            strength = "Strong"
            progress = 0.75
            crack = "Years"

        else:

            strength = "Very Strong"
            progress = 1.0
            crack = "Millions of Years"

        return {

            "strength": strength,

            "progress": progress,

            "entropy": round(entropy, 2),

            "crack_time": crack

        }