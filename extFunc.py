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

    def __init__(self, modelDict: "modelDict", **kwargs):
        self.modelDict = modelDict
        self.solutionDict = {}
        self.summaryDict = {}
        self.dataFrameDict = {}
        self.generate()

    # collect the objects of interest
    def generate(self):
        for model in self.modelDict.keys():
            self.solutionDict[model] = self.modelDict[model].optimize()
            self.summaryDict[model] = self.modelDict[model].summary(
                solution=self.solutionDict[model], fva=.99)
            self.dataFrameDict[model] = {
                "uptake":   pd.read_html(self.summaryDict[model].to_html())[0].sort_values('C-Flux', ascending=False),
                "secretion":   pd.read_html(self.summaryDict[model].to_html())[1].sort_values('C-Flux', ascending=False)
            }

    def mySummary(self,nrRea=3,sortArgument=None,direction = None):
        dfList, keyList = [], []
        # implement sort arguments as variable sortArgument, direction
        for model in self.modelDict.keys(): 
            theMatrix   = [
                self.dataFrameDict[model]['uptake'].iloc[0:nrRea].reset_index(drop=True),
                self.dataFrameDict[model]['secretion'].iloc[0:nrRea].reset_index(drop=True) 
                ] 
        
            modelFrame=pd.concat(
                [pd.concat(theMatrix,
                keys=['Uptake', 'Secretion'], axis=1)],
                keys=[model]
                ) 
            dfList.append(modelFrame)
            keyList.append(model)

        return pd.concat(dfList,axis=0)