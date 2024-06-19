
def score_server():
    try:
        with open("/scores.txt", "a") as file:
            pass
        with open("/scores.txt", "r") as file:
            return f"""
                   <html>
                   <head>
                   <title>Scores Game</title>
                   </head>
                   <body>
                   <h1><div id="score" style="color:red">The score is: {file.read().strip()}</div></h1>
                   </body>
                   </html>
                   """
    except FileNotFoundError as e:
        pass
    except BaseException as e:
        return f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score">{e}</div></h1>
        </body>
        </html>
        """
