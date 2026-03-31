from pyteal import *

def approval_program():
    return Seq(
        Log(Bytes("Hello Algorand")),
        Approve()
    )

def clear_state_program():
    return Approve()

if __name__ == "__main__":
    print(compileTeal(approval_program(), mode=Mode.Application))
