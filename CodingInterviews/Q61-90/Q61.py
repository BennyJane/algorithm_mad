# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""

"""


def Solution(s: str):
    import string
    _count = 0
    uppers = string.ascii_uppercase
    print(uppers)
    for w in s:
        if w in uppers:
            _count += 1
    print(_count)
    return _count


if __name__ == '__main__':
    t = "uViSStsvHePnyfDdROamQtFlUgWlxbolnEZKJsWYtZRZWoICvcnfVaEjGeOgzuTkFDXlkElAEthETzPhXNBHZoiSaYTSzMvkFARUIfbfGaTSjRhBfayLRvmRsqcnTuLxcbJwXwkflewnPeGLkChxToNfJymnGmabIWKFMTnrMBOKgheGhJsDEQayqDfnHmAGfyBsdjdb"
    t = "EaPAaNfzmnCfnEzSUAFKfXDfbWlYorJHkAmSbZltSetyWSLGfkWdzZjCmKIvFcRIRvuxpuASNdCfrXCQCOlmoaVPzvDegpSxAywfLlzZWkpPCFXUWwkugIMIopzKfdvFianTqwjeGSSfBqSMXnuADdBSXDQjVRAdVaiDOOkCoUXAqeCVomEjZieNvsVGgRQxH"
    print(Solution(t))
