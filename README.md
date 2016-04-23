# Betarepo

A periodic poke at collecting some classic data structures and algorithm implementations.
Also, an exercise in creating a [Pants](https://github.com/pantsbuild/pants)-style
monorepo.

#### Motivation
I often find that a problem I am working on has a well-known solution - or perhaps a preferred structure for its data.
I then implement that solution for the problem at hand but then the resulting code just sits on my file system - 
often never read again.

The general idea is that if and when I need to implement a classic algorithm or data structure -
I want to try and remember to dump the code here.
The code is in Python and will use the Python library for the Primitive and most Composite types.

#### Run the code
Who knows? There isn't really any code yet and there probably never will be.
If you do find some code you want to run, you can get a repl with all the classes loaded by runnng:

      ./pants repl src/python::
You can run all the tests with:

      ./pants test test::
If you are totally new to Pants - there is a link to the docs at the top.

#### Copyright and license
Copyright 2016 mateor.
Code released under [The MIT License (MIT)](https://github.com/mateor/betarepo/blob/master/MIT-LICENSE.txt).
