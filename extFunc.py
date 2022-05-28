import pandas as pd
import cobra

## Function imports models as name model file pairs

def ImportFunction(nameList):
    mainPATH                        = '/Users/ivanlizat/Documents/devel/folderForGit/PseudomonasPutidaCobraPy'
    relativModelPATH = mainPATH + '/MatlabExportedModels'
    modelDict = {}
    for name in nameList:
        modelDict[ "{0}".format(name.removesuffix(".xml"))] = cobra.io.read_sbml_model(
            relativModelPATH + '/' + str(name))
    return modelDict
