def check_empty(fn):
    def inner_functon(username, password):
        if username == "" or password == "":
            print("Username or password cannot be empty")
            return
        fn(username, password)
    return inner_functon

@check_empty
def login(username, password):
    if username == "Dan" and password == "7":
        print("Success")
    else:
        print("Failure")

@check_empty
def register(username, password):
    print("Success")

#login("Dan", "")
register("Abc", "")