from io import BytesIO
from synacorvm import SynacorProgram


def test_empty_file():
    bin_fp = BytesIO(b"")
    program = SynacorProgram(bin_fp)
    program.execute()
