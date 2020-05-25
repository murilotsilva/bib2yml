#!/usr/bin/python3
from pybtex.database.input import bibtex
import libs.LatexAccents as TeXAccents
import argparse
import os

def YAMLprinter(inputFile,outputFile):
    # Open BibTeX file
    parser = bibtex.Parser()

    # Initialize TeX Accent Converter
    converter = TeXAccents.AccentConverter()

    bibdata = parser.parse_file(inputFile)
    for bibId in bibdata.entries:
        bibEntry = bibdata.entries[bibId].fields
        bibAuthors = bibdata.entries[bibId].persons['author']
        print(f"- id: {bibId}", file=open(outputFile, "a"))
        print(f"- entrytype: {bibdata.entries[bibId].type}", file=open(outputFile, "a"))
        print("  authors:", file=open(outputFile, "a"))
        for author in range(len(bibAuthors)):
            detexed_author = converter.decode_Tex_Accents(str(bibAuthors[author]), utf8_or_ascii=1).replace('{','').replace('}','')
            print(f"    - names: {detexed_author.split(',')[1].lstrip()}", file=open(outputFile, "a"))
            print(f"      surnames: {detexed_author.split(',')[0].lstrip()}", file=open(outputFile, "a"))
        for field in bibEntry:
            # Remove accents and brackets from BibTeX field, and substitute underscores
            detexed_field = converter.decode_Tex_Accents(bibEntry[field], utf8_or_ascii=1).replace('{\_}','_').replace('{','').replace('}','').replace('--','—')
            # Print field
            print(f"  {field}: {detexed_field}", file=open(outputFile, "a"))

def bib_to_YAML(inputFiles,outputFiles):    
    if len(outputFiles) == 1:
        inputs = ', '.join(inputFiles)
        print(f"# {outputFiles[0]} - Converted from {inputs} using bib2yml.py", file=open(outputFiles[0],"w"))
        for i in range(len(inputFiles)):
            YAMLprinter(inputFiles[i],outputFiles[0])
    else:
        for i in range(len(inputFiles)):
            print(f"# {outputFiles[i]} - Converted from {inputFiles[i]} using bib2yml.py", file=open(outputFiles[i],"w"))
            YAMLprinter(inputFiles[i],outputFiles[i])



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
        for inputFile in inputFiles:
            outputFiles.append(inputFile.replace('.bib','.yml'))
    else:
        outputFiles = args.output

    bib_to_YAML(inputFiles,outputFiles)

if __name__ == '__main__':
    main()
            

