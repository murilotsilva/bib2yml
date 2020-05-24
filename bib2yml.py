#!/usr/bin/python3
from pybtex.database.input import bibtex
import libs.LatexAccents as TeXAccents
import argparse
import os

def bib_to_YAML(inputFiles,outputFiles):
    # Open BibTeX file
    parser = bibtex.Parser()

    # Initialize TeX Accent Converter
    converter = TeXAccents.AccentConverter()
    
    if len(outputFiles) == 1:
        inputs = ', '.join(inputFiles)
        print(f"# {outputFiles[0]} - Converted from {inputs} using bib2yml.py", file=open(outputFiles[0],"w"))
        for i in range(len(inputFiles)):
            bibdata = parser.parse_file(inputFiles[i])
            for bibId in bibdata.entries:
                bibEntry = bibdata.entries[bibId].fields
                print(f"- id: {bibId}", file=open(outputFiles[0], "a"))
                for field in bibEntry:
                    # Remove accents and brackets from BibTeX field, and substitute underscores
                    detexed_field = converter.decode_Tex_Accents(bibEntry[field], utf8_or_ascii=1).replace('{\_}','_').replace('{','').replace('}','').replace('--','—')
                    print(f"  {field}: {detexed_field}", file=open(outputFiles[0], "a"))
    else:
        for i in range(len(inputFiles)):
            print(f"# {outputFiles[i]} - Converted from {inputFiles[i]} using bib2yml.py", file=open(outputFiles[i],"w"))
            bibdata = parser.parse_file(inputFiles[i])
            for bibId in bibdata.entries:
                bibEntry = bibdata.entries[bibId].fields
                print(f"- id: {bibId}", file=open(outputFiles[i], "a"))
                for field in bibEntry:
                    # Remove accents and brackets from BibTeX field, and substitute underscores
                    detexed_field = converter.decode_Tex_Accents(bibEntry[field], utf8_or_ascii=1).replace('{\_}','_').replace('{','').replace('}','').replace('--','—')
                    print(f"  {field}: {detexed_field}", file=open(outputFiles[i], "a"))


def main():
    # Initiate the parser
    parser = argparse.ArgumentParser(description='Translate .bib file to YAML.')
    parser.add_argument('-i', '--input', nargs='+', required=True, help="Specify input .bib files")
    parser.add_argument('-o','--output', nargs='+', required=False, help="Specify output .yml files")
    args = parser.parse_args()
    if args.output != None and len(args.input) != len(args.output):
        parser.error('If outputs are specified, the number of inputs and outputs should match!')
    
    for inputFile in args.input:
        if os.path.exists(inputFile) == False:
            parser.error(f"{inputFile}: File not found!")
    
    inputFiles = args.input
    
    if args.output == None:
        outputFiles = []
        for i,inputFile in enumerate(inputFiles):
            outputFiles.append(inputFile.replace('.bib','.yml'))
    else:
        outputFiles = args.output

    bib_to_YAML(inputFiles,outputFiles)

if __name__ == '__main__':
    main()
            

