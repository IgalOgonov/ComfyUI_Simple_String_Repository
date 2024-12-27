from .util import Util

class SimpleStringRepositorySmall:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
                "delimiter": ([",", " "], {}),
            },
            "optional": {
                "target1": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength1": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random1": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target2": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength2": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random2": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target3": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength3": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random3": ("INT", {"default":-1,"min": -1,"max": 1000})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("parsed_string",)
    CATEGORY = "utils"
    FUNCTION = "exec"
    OUTPUT_NODE = True
    
    def IS_CHANGED(self, string, delimiter, target1=None, strength1=None, random1=None, target2=None, strength2=None, random2=None, 
            target3=None, strength3=None, random3=None):
        parsedInputs = [
            {"t":target1,"s":strength1,"r":random1},
            {"t":target2,"s":strength2,"r":random2},
            {"t":target3,"s":strength3,"r":random3}
        ]
        return (True, float("NaN"))[Util.areThereTargetsWithRandomness(parsedInputs)]

    #Main Function
    def exec(self, string, delimiter, target1=None, strength1=None, random1=None, target2=None, strength2=None, random2=None, 
            target3=None, strength3=None, random3=None):
        
        #Parse inputs for clarity
        parsedInputs = [
            {"t":target1,"s":strength1,"r":random1},
            {"t":target2,"s":strength2,"r":random2},
            {"t":target3,"s":strength3,"r":random3}
        ]
        return Util.common_string_repo_function(string,delimiter,parsedInputs)

class SimpleStringRepositorySmallCompact:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
                "delimiter": ([",", " "], {}),
            },
            "optional": {
                "target1": ("STRING", {"default":'0,1,-1'}),
                "target2": ("STRING", {"default":'0,1,-1'}),
                "target3": ("STRING", {"default":'0,1,-1'})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("parsed_string",)
    CATEGORY = "utils"
    FUNCTION = "exec"
    OUTPUT_NODE = True
    
    def IS_CHANGED(self, string, delimiter, target1=None, target2=None, target3=None):
        targets = [target1,target2,target3]
        return (True, float("NaN"))[Util.areThereTargetsWithRandomness(Util.parseCompactInputs(targets))]

    #Main Function
    def exec(self, string, delimiter, target1=None, target2=None, target3=None):
        targets = [target1,target2,target3]
        return Util.common_string_repo_function(string,delimiter,Util.parseCompactInputs(targets))

class SimpleStringRepository:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
                "delimiter": ([",", " "], {}),
            },
            "optional": {
                "target1": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength1": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random1": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target2": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength2": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random2": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target3": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength3": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random3": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target4": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength4": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random4": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target5": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength5": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random5": ("INT", {"default":-1,"min": -1,"max": 1000}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("parsed_string",)
    CATEGORY = "utils"
    FUNCTION = "exec"
    OUTPUT_NODE = True
    
    def IS_CHANGED(self, string, delimiter, target1=None, strength1=None, random1=None, target2=None, strength2=None, random2=None, 
            target3=None, strength3=None, random3=None, target4=None, strength4=None, random4=None, target5=None, strength5=None, random5=None):
        parsedInputs = [
            {"t":target1,"s":strength1,"r":random1},
            {"t":target2,"s":strength2,"r":random2},
            {"t":target3,"s":strength3,"r":random3},
            {"t":target4,"s":strength4,"r":random4},
            {"t":target5,"s":strength5,"r":random5}
        ]
        return (True, float("NaN"))[Util.areThereTargetsWithRandomness(parsedInputs)]

    #Main Function
    def exec(self, string, delimiter, target1=None, strength1=None, random1=None, target2=None, strength2=None, random2=None, 
            target3=None, strength3=None, random3=None, target4=None, strength4=None, random4=None, target5=None, strength5=None, random5=None):
        
        #Parse inputs for clarity
        parsedInputs = [
            {"t":target1,"s":strength1,"r":random1},
            {"t":target2,"s":strength2,"r":random2},
            {"t":target3,"s":strength3,"r":random3},
            {"t":target4,"s":strength4,"r":random4},
            {"t":target5,"s":strength5,"r":random5}
        ]
        return Util.common_string_repo_function(string,delimiter,parsedInputs)

class SimpleStringRepositoryCompact:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
                "delimiter": ([",", " "], {}),
            },
            "optional": {
                "target1": ("STRING", {"default":'0,1,-1'}),
                "target2": ("STRING", {"default":'0,1,-1'}),
                "target3": ("STRING", {"default":'0,1,-1'}),
                "target4": ("STRING", {"default":'0,1,-1'}),
                "target5": ("STRING", {"default":'0,1,-1'})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("parsed_string",)
    CATEGORY = "utils"
    FUNCTION = "exec"
    OUTPUT_NODE = True
    
    def IS_CHANGED(self, string, delimiter, target1=None, target2=None, target3=None, target4=None, target5=None):
        targets = [target1,target2,target3,target4,target5]
        return (True, float("NaN"))[Util.areThereTargetsWithRandomness(Util.parseCompactInputs(targets))]

    #Main Function
    def exec(self, string, delimiter, target1=None, target2=None, target3=None, target4=None, target5=None):
        targets = [target1,target2,target3,target4,target5]
        return Util.common_string_repo_function(string,delimiter,Util.parseCompactInputs(targets))

class SimpleStringRepositoryLarge:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
                "delimiter": ([",", " "], {}),
            },
            "optional": {
                "target1": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength1": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random1": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target2": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength2": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random2": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target3": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength3": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random3": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target4": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength4": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random4": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target5": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength5": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random5": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target6": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength6": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random6": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target7": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength7": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random7": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target8": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength8": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random8": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target9": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength9": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random9": ("INT", {"default":-1,"min": -1,"max": 1000}),
                "target10": ("INT", {"default":None,"min": 0,"max": 100000000}),
                "strength10": ("FLOAT", {"default":1.0,"min": 0,"max": 10}),
                "random10": ("INT", {"default":-1,"min": -1,"max": 1000}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("parsed_string",)
    CATEGORY = "utils"
    FUNCTION = "exec"
    OUTPUT_NODE = True
    
    def IS_CHANGED(self, string, delimiter, target1=None, strength1=None, random1=None, target2=None, strength2=None, random2=None, 
            target3=None, strength3=None, random3=None, target4=None, strength4=None, random4=None, target5=None, strength5=None, random5=None, 
            target6=None, strength6=None, random6=None, target7=None, strength7=None, random7=None, 
            target8=None, strength8=None, random8=None, target9=None, strength9=None, random9=None, target10=None, strength10=None, random10=None):
        parsedInputs = [
            {"t":target1,"s":strength1,"r":random1},
            {"t":target2,"s":strength2,"r":random2},
            {"t":target3,"s":strength3,"r":random3},
            {"t":target4,"s":strength4,"r":random4},
            {"t":target5,"s":strength5,"r":random5},
            {"t":target6,"s":strength6,"r":random6},
            {"t":target7,"s":strength7,"r":random7},
            {"t":target8,"s":strength8,"r":random8},
            {"t":target9,"s":strength9,"r":random9},
            {"t":target10,"s":strength10,"r":random10}
        ]
        return (True, float("NaN"))[Util.areThereTargetsWithRandomness(parsedInputs)]
        

    #Main Function
    def exec(self, string, delimiter, target1=None, strength1=None, random1=None, target2=None, strength2=None, random2=None, 
            target3=None, strength3=None, random3=None, target4=None, strength4=None, random4=None, target5=None, strength5=None, random5=None, 
            target6=None, strength6=None, random6=None, target7=None, strength7=None, random7=None, 
            target8=None, strength8=None, random8=None, target9=None, strength9=None, random9=None, target10=None, strength10=None, random10=None):
        
        #Parse inputs for clarity
        parsedInputs = [
            {"t":target1,"s":strength1,"r":random1},
            {"t":target2,"s":strength2,"r":random2},
            {"t":target3,"s":strength3,"r":random3},
            {"t":target4,"s":strength4,"r":random4},
            {"t":target5,"s":strength5,"r":random5},
            {"t":target6,"s":strength6,"r":random6},
            {"t":target7,"s":strength7,"r":random7},
            {"t":target8,"s":strength8,"r":random8},
            {"t":target9,"s":strength9,"r":random9},
            {"t":target10,"s":strength10,"r":random10}
        ]
        return Util.common_string_repo_function(string,delimiter,parsedInputs)

class SimpleStringRepositoryLargeCompact:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
                "delimiter": ([",", " "], {}),
            },
            "optional": {
                "target1": ("STRING", {"default":'0,1,-1'}),
                "target2": ("STRING", {"default":'0,1,-1'}),
                "target3": ("STRING", {"default":'0,1,-1'}),
                "target4": ("STRING", {"default":'0,1,-1'}),
                "target5": ("STRING", {"default":'0,1,-1'}),
                "target6": ("STRING", {"default":'0,1,-1'}),
                "target7": ("STRING", {"default":'0,1,-1'}),
                "target8": ("STRING", {"default":'0,1,-1'}),
                "target9": ("STRING", {"default":'0,1,-1'}),
                "target10": ("STRING", {"default":'0,1,-1'})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("parsed_string",)
    CATEGORY = "utils"
    FUNCTION = "exec"
    OUTPUT_NODE = True
    
    def IS_CHANGED(self, string, delimiter, target1=None, target2=None, target3=None, target4=None, target5=None, 
                    target6=None, target7=None, target8=None, target9=None, target10=None):
        targets = [target1,target2,target3,target4,target5,target6,target7,target8,target9,target10]
        return (True, float("NaN"))[Util.areThereTargetsWithRandomness(Util.parseCompactInputs(targets))]

    #Main Function
    def exec(self, string, delimiter, target1=None, target2=None, target3=None, target4=None, target5=None, 
            target6=None, target7=None, target8=None, target9=None, target10=None):
        targets = [target1,target2,target3,target4,target5,target6,target7,target8,target9,target10]
        return Util.common_string_repo_function(string,delimiter,Util.parseCompactInputs(targets))