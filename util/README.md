Okay, we have to note this down: Packaging. We are not done with it yet but yeah, let's just look at the basics

We have created a utility here where temporal has all the juice, the setup.py is the real handler.

You have to fill setup.py with context and then go `pip install -e .` to make it actually work.
Talked about in more detail in the relevant DanteMap version. Oh, and -e is for editable- so when you edit things in the util, it canges real time in the usecase.