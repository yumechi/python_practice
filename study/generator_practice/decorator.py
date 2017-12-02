#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import traceback

"""
refer: http://www.shuwasystem.co.jp/products/7980html/2655.html
Python入門(2&3) 第12章のデコレータ
"""

def run():
    def decorate(f):
        f.x = 1
        return f
    
    @decorate
    def func():
        pass
    
    print(func.x)

def fail_run():
    """
    存在しないデコレーターを呼ぶ
    """
    try:
        @nai_decorate
        def func():
            pass
        
        print(func.x)
    except Exception as e:
        # ログ出力はこんな感じでやると良い
        # NameErrorの例外が出る模様
        logging.error(traceback.format_exc())
        logging.exception(e)

if __name__ == '__main__':
    run()
    fail_run()
