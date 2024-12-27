import re
import random

class Util:
    @staticmethod
    def var_dump(var, prefix=''):
        """
        You know you're a php developer when the first thing you ask for
        when learning a new language is 'Where's var_dump?????'
        """
        my_type = '[' + var.__class__.__name__ + '(' + str(len(var)) + ')]:'
        print(prefix, my_type, sep='')
        prefix += '    '
        for i in var:
            if type(i) in (list, tuple, dict, set):
                Util.var_dump(i, prefix)
            else:
                if isinstance(var, dict):
                    print(prefix, i, ': (', var[i].__class__.__name__, ') ', var[i], sep='')
                else:
                    print(prefix, '(', i.__class__.__name__, ') ', i, sep='')

    @staticmethod
    def removing_leading_whitespaces(text):
        """
        Remove leading whitespaces
        """
        return re.sub(r"^\s+","",text)

    @staticmethod
    def areThereTargetsWithRandomness(inputs):
        for tuple in inputs:
            if(tuple["r"] == -1 and tuple["t"] != None):
                return True
        return False

    @staticmethod
    def parseCompactInputs(inputs):
        newInputs = []
        for string in inputs:
            parsedString = string.split(',')
            newTuple = {
                "t":int(parsedString[0])
            }
            
            if(len(parsedString) >= 2):
                newTuple["s"] = float(parsedString[1])
            else:
                newTuple["s"] = 1.0
            
            if(len(parsedString) >= 3):
                newTuple["r"] = int(parsedString[2])
            else:
                newTuple["r"] = -1
                
            newInputs.append(newTuple)
        return newInputs

    @staticmethod
    def common_string_repo_function(string, delimiter, inputs):
        """
        Common function which is actually the string repo main function.
        The classes are just wrappers around it with a different number of similar inputs. 
        """
        orphanStrings = []
        newDict = {}
        parsingIndex = 0
        parsedString = string.splitlines()

        # Parse all strings, separated by newline. 
        # A properly formatted string should either have ALL strings with unique numeric identifiers, or none at all.
        # Strings without a leading number will be assigned one based on their line number.
        # In case of a mix of both, unexpected behavior may occur - strings without an identifier will be assigned one, and subsequent duplicate numeric identifiers are ignored.
        for line in parsedString:

            existingId = None
            currentString = None
            parsingIndex += 1
            
            parsedLine = line.split(".")
            if(len(parsedLine) != 1):
                existingId = parsedLine[0]
                currentString = parsedLine[1]
            else:
                currentString = parsedLine[0]
            
            Util.removing_leading_whitespaces(currentString)
            
            if(not existingId):
                existingId = parsingIndex
                
            existingId = int(existingId)
            
            if existingId in newDict:
                orphanStrings.extend((currentString,))
            else:
                newDict[existingId] = currentString
                

        # Debug:
        # print("Dict:")
        # for k,v in newDict.items():
        #     print(k, "corresponds to", v)
        # print("Orphans:")
        # for v in orphanStrings:
        #     print(v)
            

        #Parse all inputs
        finalString = ''
        for tuple in inputs:
            
            #Target does not exist!
            if(tuple["t"] not in newDict):
                # Debug:
                #print("target", tuple["t"], "does not exist!")
                continue
            
            #Target exists!
            baseStr = newDict[tuple["t"]]
            
            #Handle randomness, if applicable
            if(re.fullmatch("^{.+}$",baseStr)):
                baseStr = baseStr[1:][:-1]
                baseStr = baseStr.split("|")
                
                if(tuple["r"] == -1):
                    tuple["r"] = random.randint(0, len(baseStr)-1)
                if(tuple["r"] >= len(baseStr)):
                    # Debug:
                    #print("Random string ", tuple["r"], "in target",tuple["t"],baseStr, "does not exist!")
                    continue
                baseStr = baseStr[tuple["r"]]
                
            #Handle Strength
            if(not tuple["s"]):
                # Debug:
                #print("Target",tuple["t"], "Has strength 0")
                continue
            elif(tuple["s"] != 1):
                tuple["s"] = round(tuple["s"],2)
                baseStr = f'({baseStr}:{tuple["s"]})'
            
            finalString += baseStr + delimiter
            
        finalString = finalString[:-1]
        # Debug:
        #print(finalString)
        return {"ui": {"text": (finalString,)}, "result": (finalString,)}