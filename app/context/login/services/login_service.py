from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import RedirectResponse


class LoginService:
    async def home(self) -> RedirectResponse:
        return RedirectResponse("/login")

    async def login_form(self) -> str:
        return """
        <!DOCTYPE html>
        <html>
           <body>
              <form method="POST"  action="/login">
                 <label for="username">Login:</label><br>
                 <input type="text" id="username" name="username" value=""><br>
                 <label for="password">Password:</label><br>
                 <input type="password" id="password" name="password" value=""><br><br>
                 <input type="submit" value="Submit">
              </form>
           </body>
        </html>
        """

    async def login(self, data: OAuth2PasswordRequestForm = Depends()) -> str:
        login = data.username
        password = data.password
        if login == 'admin' and password == 'admin':
            return """
                    <html>
                        <head>
                            <title>All correct</title>
                        </head>
                        <body>
                            <h1>All correct</h1>
                        </body>
                        <script type="text/JavaScript">
                              setTimeout("location.href = 'http://127.0.0.1:6000/appsec?key=practice_main';",2000);
                         </script>
                    </html>
                    """
        else:
            return """
                    <html>
                        <head>
                            <title>Incorrect</title>
                        </head>
                        <body>
                            <h1>Incorrect</h1>
                        </body>
                    </html>
                    """