# 32bit_a3x_converter 
This script is designed to convert 64-bit a3x files to 32-bit to allow older decompilation tools to work.

## Description
A lot of the freely available tools to decompile, analyse and reverse AutoIT related scripts do not support 64 bit. This tool will convert 64 bit a3x compiled scripts into 32 bit.

## Prerequisites
You should have the AutoItSC.bin file. It can be obtained from: https://www.autoitscript.com/autoit3/files/archive/autoit
Once you've downloaded the ZIP, you can find the required file in the path: Aut2Exe\AutoItSC.bin.

## Usage
```bash
python <script_name> <path_to_AutoItSC.bin> <a3x_file_to_convert>
```
### For example
```bash
python converter_script.py C:\path\to\AutoItSC.bin C:\path\to\file.a3x
```
### To display the help message
```bash
python <script_name> -h
```
or
```bash
python <script_name> --help
```

##How it works
AutoItSC.bin contains necessary 32-bit headers and components. By splicing out the code section of the a3x script that we wish to convert and appending it onto the end of AutoItSC.bin, we create a 32-bit version of the script.
