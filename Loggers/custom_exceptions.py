from loguru import logger


class CustomExecption(Exception):

    def __init__(self, msg="Custom Execption Raised"):
        super().__init__(msg)


def check_custom_execption():
    try:
        res = "Passed"
        raise CustomExecption
    except CustomExecption as err:
        logger.error(err)
        res = "Failed"
    print(res)


if __name__ == "__main__":
    check_custom_execption()
    