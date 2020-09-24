import shutit


session = shutit.create_session("bash")
session.send("echo Hello World", echo=True)