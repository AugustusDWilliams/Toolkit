import logging


class PackageError(Exception):
    pass
    #def __init__(self, msg):
    #    super().__init__(msg)


class PackageError1(Exception):
    pass

def raise_PhotoaiError(msg):
    logging.error(msg)
    raise PackageError1(msg)

#class PackageError2(PackageError):
class PackageError2(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Demo:
    def __init__(self):
        super().__init__()

    @staticmethod
    def is_valid_value(val: int) -> bool:
        """
        Parameters:
        -----------
        machine_learning_type   Returns
    -----------
    True   Raises
    -----------
    if not known machine_learning_type
    """
        if val:
            return True
        #raise PackageError2("Please Enter a Valid Value")
        raise_PhotoaiError("Enter a Valid Value")

if __name__ == "__main__":
    cls = Demo()
    res = cls.is_valid_value(0)
    print("Res:", res)