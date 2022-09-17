from ast import parse
from sys import hexversion
from django.shortcuts import render
from django.http import HttpResponse

import base64

def Home(request):
    return render(request, 'base/home.html')

def HexToAscii(request):
    context = {}
    if request.method == "POST":
        input = request.POST.get("input")
        input = input.replace(' ', '')
        input = input.replace('/', '')
        input = input.replace('0x', '')
        input = input.replace('\t', '')
        
        output = ""
        for i in range(0, len(input), 2):
            if len(input) == 1:
                try:
                    hexValue = int(input[i], 16)
                    if hexValue >= 0 and hexValue <= 15:
                        output += chr(hexValue)
                        continue
                except ValueError:
                    output += " "
                    context["error"] = "Error - Some data was invalid and was skipped"
                    continue
            else:
                try:
                    hexValue = int(input[i] + input[i + 1], 16)
                    if hexValue <= 127:
                        output += chr(hexValue)
                    else:
                        raise ValueError
                except ValueError:
                    output += " "
                    context["error"] = "Error - Some data was invalid and was skipped"
                    continue
                except IndexError:
                    try:
                        hexValue = int(input[i], 16)
                        if hexValue >= 0 and hexValue <= 15:
                            output += chr(hexValue)
                            continue
                    except ValueError:
                        output += " "
                        context["error"] = "Error - Some data was invalid and was skipped"
                        continue
        context["input"] = request.POST.get("input")
        context["output"] = output
    return render(request, "base/hex_to_ascii.html", context)

def AsciiToHex(request):
    context = {}
    if request.method == "POST":
        input = request.POST.get("input")
        output = ""
        for i in range(0, len(input)):
            output += format(ord(input[i]), '2x')
            output += " "
        context["input"] = request.POST.get("input")
        context["output"] = output
    return render(request, 'base/ascii_to_hex.html', context)

def HexToDecimal(request):
    context = {}
    if request.method == "POST":
        input = request.POST.get("input")
        try:
            input = int(input, 16)
        except:
            context["error"] = "Error - couldn't convert data"
        context["output"] = input
        context["input"] = request.POST.get("input")
    return render(request, 'base/hex_to_decimal.html', context)

def DecimalToHex(request):
    context = {}
    if request.method == "POST":
        input = request.POST.get("input")
        try:
            input = hex(int(input))
        except:
            context["error"] = "Error - couldn't convert data"
        context["output"] = input
        context["input"] = request.POST.get("input")
    return render(request, 'base/decimal_to_hex.html', context)

def Base64Encode(request):
    context = {}
    if request.method == "POST":
        input = request.POST.get("input")
        try:
            input = base64.b64encode(input.encode("utf-8"))
            input = str(input, "utf-8")
        except:
            context["error"] = "Error - couldn't convert data"
        context["output"] = input
        context["input"] = request.POST.get("input")
    return render(request, 'base/base64_encode.html', context)

def Base64Decode(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        input = request.POST.get("input")
        try:
            input = base64.b64decode(input)
            input = str(input, "utf-8")
        except:
            context["error"] = "Error - couldn't convert data"
        context["output"] = input
        context["input"] = request.POST.get("input")
    return render(request, 'base/base64_decode.html', context)

def AsciiTable(request):
    context = {}
    return render(request, 'base/ascii_table.html', context)

def GeneralConversion(request):
    context = {}
    if request.method == "POST":
        input = request.POST.get("input")
        if request.POST.get("Input Type") == "Binary":
            context["output"] = True
            try:
                context["binSelected"] = "selected"
                context["binaryOutput"] = input
                context["hexOutput"] = hex(int(input, 2))
                context["decimalOutput"] = int(input, 2)
                context["asciiOutput"] = chr(int(input, 2))
            except:
                context["error"] = "Error - data was too large or incorrect"
        elif request.POST.get("Input Type") == "Hexadecimal":
            context["output"] = True
            try:
                context["hexSelected"] = "selected"
                context["binaryOutput"] = format(int(input, 16), 'b')
                context["hexOutput"] = input
                context["decimalOutput"] = int(input, 16)
                context["asciiOutput"] = chr(int(input, 16))
            except:
                context["error"] = "Error - data was too large or incorrect"
        elif request.POST.get("Input Type") == "Decimal":
            context["output"] = True
            try:
                context["decSelected"] = "selected"
                context["binaryOutput"] = format(int(input, 10), 'b')
                context["hexOutput"] = hex(int(input))
                context["decimalOutput"] = input
                context["asciiOutput"] = chr(int(input, 10))
            except:
                context["error"] = "Error - data was too large or incorrect"
        elif request.POST.get("Input Type") == "Ascii":
            context["output"] = True
            try:
                context["ascSelected"] = "selected"
                context["binaryOutput"] = format(ord(input), 'b')
                context["hexOutput"] = format(ord(input), 'x')
                context["decimalOutput"] = ord(input)
                context["asciiOutput"] = input
            except:
                context["error"] = "Error - data was too large or incorrect"
        else:
            context["output"] = False
        
        context["input"] = input
    return render(request, 'base/general_conversion.html', context)

def XorCalculator(request):
    context = {}
    if request.method == "POST":
        input1 = request.POST.get("input1")
        input2 = request.POST.get("input2")
        input1 = input1.split(" ")
        output = ""
        for i in range(0, len(input1)):
            if input1[i] == " ":
                continue
            try:
                output += str(int(input1[i]) ^ int(input2))
                output += " "
            except:
                output += " "
                context["error"] = "Error - encountered problem whilst calculating"
        context["output"] = output
        context["input1"] = request.POST.get("input1")
        context["input2"] = request.POST.get("input2")
    return render(request, 'base/xor_calculator.html', context)