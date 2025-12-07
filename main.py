import re

def parseJSON(jsonString):
    string = re.sub(r'\s', '', jsonString)
    stack = []
    obj = None
    key = ""
    value = ""
    i = 0
    while i < len(string):
        if string[i] == "{":
            if obj is None:
                obj = {}
            else:
                stack.append(obj)
                obj[key] = {}
                obj = obj[key]
                key = ""
        elif string[i] == "}":
            if len(stack) > 0:
                obj = stack.pop()
        elif string[i] == '"' and string[i - 1] != ":" and string[i + 1] != "}":
            c = 1
            while string[i + c] != "}" and string[i + c] != ":" and string[i + c] != '"':
                key += string[i + c]
                c += 1
            i += c
            c = 1
        elif string[i] == ":" and string[i + 1] != "{":
            c = 1
            while string[i + c] != "," and string[i + c] != "}" and i + c < len(string):
                value += string[i + c]
                c += 1
            i += c
            c = 1
            if value == "true":
                value = True
            elif value == "false":
                value = False
            elif value.isdigit():
                value = int(value)
            else:
                value = value[1:-1]
            obj[key] = value
            key = ""
            value = ""
        i += 1
    
    return obj

jsonString = '''
{

     "age": 22,
     "score": 99,
     "name": "Anna",
  "school": {
     "name": "university",
     "address": {
        "street": "Azatutyan",
        "number": 24
     }
  }
}
'''
parsedJSON = parseJSON(jsonString)
print(parsedJSON)

