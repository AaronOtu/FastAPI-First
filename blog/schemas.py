from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str



    def __str__(self):
        return f"{self.title}, {self.body}"
