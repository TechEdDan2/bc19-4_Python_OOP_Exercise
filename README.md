# bc19-4_Python_OOP_Exercise
This is a solution to the Python Unit 

## Table of contents

- [Overview](#overview)
- [The challenge](#the-challenge)

## Overview

### The challenge

The WordFinder class works like this::

- it is instantiated with a path to a file on disk that contains words, one word per line
    - it reads that file, and makes an attribute of a list of those words
    - it prints out “[num-of-words-read] words read”
    
    (it doesn’t need to do all of this directly in the ***__init__*** method; it might be a good idea for the ***__init__*** method to call other functions to do some of this.)
    
- it provides a method, ***random()***, which returns a random word from that list of words
    
    Note: the ***random*** method **should not** re-read the list of words each time; it should work with the already-read-in list of words.