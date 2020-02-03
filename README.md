# pdf-playground

Please let's forget right away the name of this repository, I did play along with PyPDF2 but the result is a single simple application, a PDF merger.

This program requires you to install PyPDF2:
```terminal
pip3 install PyPDF2
```

Once you cloned this repo, all you need to do is type this in your terminal:
```terminal
python3 pdf.py super.pdf wtr.pdf
```

If you ever need to use this program to truly merge PDF, you just have to delete super.pdf and wtr.pdf and use your own files. The first argument in the command line is the pdf you need to update, the seconde argument is the template that will get merged into the source file you provided as argument #1.

Have a good day :)