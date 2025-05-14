from datetime import datetime

class BasicUserModel:
    def __init__(
        self,
        id: int = int(datetime.now().strftime("%Y%m%d%H%M%S")),
        name: str = f"user{int(datetime.now().strftime("%Y%m%d%H%M%S"))}",
        email: str = "",
        username: str = f"user{int(datetime.now().strftime("%Y%m%d%H%M%S"))}",
        password: str = "user",
    ):
        self.id: int = id
        self.name: str = name
        self.email: str = email
        self.username: str = username
        self.password: str = password
