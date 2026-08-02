import secrets
import string


class PasswordGenerator:

    SIMILAR = "O0oIl1|"

    @staticmethod
    def generate(
        length=16,
        uppercase=True,
        lowercase=True,
        numbers=True,
        symbols=True,
        exclude_similar=False
    ):

        pool = ""

        if uppercase:
            pool += string.ascii_uppercase

        if lowercase:
            pool += string.ascii_lowercase

        if numbers:
            pool += string.digits

        if symbols:
            pool += "!@#$%^&*()-_=+[]{}<>?/"

        if exclude_similar:

            for char in PasswordGenerator.SIMILAR:
                pool = pool.replace(char, "")

        if not pool:
            raise ValueError(
                "Select at least one character type."
            )

        return "".join(
            secrets.choice(pool)
            for _ in range(length)
        )