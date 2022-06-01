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

## Model Comparison Class

class ModelComparison():
    '''
    This Class can be used to compare multiple modelversions 
    and to get an overview of the C-Flux routes and 
    the corresponding fva
    input  = list of models
    '''

    def __init__(self, modelDict: "modelDict",  **kwargs):
        self.modelDict = modelDict
        #self.generate()

    # collect the objects of interest


    def multiModellSummary(self,solution=None,sortKrit='flux', fvaDIr=None, nrRea=5 ,):
        dfList, keyList = [], []
        # implement sort arguments as variable sortArgument, direction
        for model in self.modelDict.keys(): 
            customDF = self.modelDict[model].summary(solution=solution,fva=fvaDIr).to_DataFrame_custom()
            theMatrix   = [
        customDF['uptake'].sort_values(sortKrit, ascending=False).iloc[0:nrRea].reset_index(drop=True),
        customDF['secretion'].sort_values(sortKrit, ascending=False).iloc[0:nrRea].reset_index(drop=True)
                            ] 
        
            modelFrame=pd.concat(
                [pd.concat(theMatrix,
                keys=['Uptake', 'Secretion'], axis=1)],
                keys=[model]
                ) 
            dfList.append(modelFrame)
            keyList.append(model)

        return pd.concat(dfList,axis=0)
    
    