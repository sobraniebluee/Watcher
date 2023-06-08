class Clrs:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    VIOLET = '\033[95m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BACKGROUND = '\033[40m'

    @classmethod
    def green(cls, string: str) -> str:
        return f"{cls.GREEN}{string}{cls.ENDC}"

    @classmethod
    def blue(cls, string: str) -> str:
        return f"{cls.BLUE}{string}{cls.ENDC}"

    @classmethod
    def cyan(cls, string: str) -> str:
        return f"{cls.CYAN}{string}{cls.ENDC}"

    @classmethod
    def violet(cls, string: str) -> str:
        return f"{cls.VIOLET}{string}{cls.ENDC}"

    @classmethod
    def warn(cls, string: str) -> str:
        return f"{cls.YELLOW}{string}{cls.ENDC}"

    @classmethod
    def fail(cls, string: str) -> str:
        return f"{cls.RED}{string}{cls.ENDC}"

    @classmethod
    def bold(cls, string: str) -> str:
        return f"{cls.BOLD}{string}{cls.ENDC}"

    @classmethod
    def underline(cls, string: str) -> str:
        return f"{cls.UNDERLINE}{string}{cls.ENDC}"

    @classmethod
    def bckg(cls, string: str) -> str:
        return f"{cls.BACKGROUND}{string}{cls.ENDC}"


__all__ = [
    "Clrs"
]
