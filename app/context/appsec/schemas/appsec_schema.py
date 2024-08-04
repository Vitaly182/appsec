from pydantic import BaseModel


class GetAppsecPractice(BaseModel):
    practice: str


class GetAppsec(BaseModel):
    sast: str
    sca: str
    dast: str
    iast: str
    rasp: str