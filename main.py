from os import path

import nonebot
import os
import cof

if __name__ == '__main__':
    nonebot.init(cof)
    os.chdir("pul")
    print(os.getcwd())
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'pul'),
        'pul'
    )
    nonebot.run()
    