#!/usr/bin/env python
# -*- coding: utf-8 -*-

def run_scripts():
    """
    Connpass's tweet button format converts my blog format
    it's convert example
    ```
    content url hashtag
    ```
    -> 
    ```
    ## content
    
    url
    ```
    """


    fragments = input().split()
    # for tweet base, last elememnt is utl pattern
    # FIXME: fxxx include space pattern, I found. it's `#somthing two`
    while "#" in fragments[-1]:
        fragments = fragments[:-1]
    
    blog_format = """
## {content}


{url}


"""
    print(blog_format.format(content="".join(fragments[:-1]),
        url=fragments[-1]))

if __name__=="__main__":
    run_scripts()
