# bib2yml
Simple Python3 code to convert .bib files to .yml.

## Requirements
 - Python3
 - LatexAccents.py by [Hayk Aleksanyan](https://github.com/hayk314), included in the `libs` folder
 - [pybtex](https://pybtex.org/) library

## Usage
### Converting a single file
You can convert any number of bibtex .bib files into .yml by using the command

    python3 bib2yml.py -i inputfile.bib
    
This will create a simple .yml file named `inputfile1.yml`. Each entry in the .bib file will be identified as an item, with fields being key/value pairs. For example, the bibtex entry

```bibtex
@article{entry01,
 author={Seinfeld, Jerry},
 title={Seinfeld: a paper about nothing},
 year={1989}
 journal={National Broadcast Channel}
}
```
will be converted to

```yaml
- id: entry01
  authors:
    - names: Jerry
      surnames: Seinfeld
  title: Seinfeld: a paper about nothing
  year: 1989
  journal: National Broadcast Channel
```

If you want to specify the name of the output file, you can write

    python3 bib2yml.py -i inputfile.bib -o outputfile.yml

In both cases, the extensions of the files should be given.

### Converting multiple files

If you want to convert multiple .bib files into different .yml files, you can use the command 

    python3 bib2yml.py -i inputfile1.bib inputfile2.bib

This will create two separate output files named `inputfile1.yml` and `inputfile2.yml`. You can also specify the names of the output files:

    python3 bib2yml.py -i inputfile1.bib inputfile2.bib -o outputfile1.bib outputfile2.bib

If you want to combine multiple .bib files into a single .yml file, you can use the command

    python3 bib2yml.py -i inputfile1.bib inputfile2.bib -o outputfile.bib

