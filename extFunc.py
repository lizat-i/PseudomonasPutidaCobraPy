import pandas as pd
import cobra
import random
import numpy as np

## Function imports models as name model file pairs

def ImportFunction(nameList):
   # mainPATH                        = '/home/ivan/Documents/devel/PseudomonasPutidaCobraPy'
    mainPATH                        = '/Users/ivanlizat/Documents/devel/folderForGit/PseudomonasPutidaCobraPy'
    relativModelPATH = mainPATH + '/MatlabExportedModels'
    modelDict = {}
    for name in nameList:
        modelDict[ "{0}".format(name.removesuffix(".xml"))] = setDemandReactions(
            reset_max_min(cobra.io.read_sbml_model(
            relativModelPATH + '/' + str(name)
                            )))
    return modelDict

def reset_max_min(model):
    for reaction in model.reactions:
        if abs(reaction.lower_bound)>1000:
            reaction.lower_bound= 1000*np.sign(reaction.lower_bound)
        if abs(reaction.upper_bound)>1000:
            reaction.upper_bound =  1000*np.sign(reaction.upper_bound)
    return model

def setDemandReactions(model,key=1):
    for reaction in model.demands:
        essentialDemand = ['DM_5drib_c', 'DM_amob_c', 
                           'DM_acmum6p_c','DM_ppi50_c',
                           'DM_acgam_c','DM_doxopa_c','DM_tripeptide_c']
        if reaction.id not in essentialDemand:
            reaction.lower_bound = 0
            reaction.upper_bound = 0         
    if key ==1:
        list1 = ['DM_C80aPHA_c','DM_C60aPHA_c','DM_C120aPHA_c','DM_C100aPHA_c',
                 'DM_C80pPHA_c','DM_C60pPHA_c','DM_C120pPHA_c','DM_C100pPHA_c'
                ]
        for reaction in model.reactions:
            if reaction.id in list1:
                reaction.lower_bound = 0
                reaction.upper_bound = 1000
                
    return model


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
    
    def singleModellSummary(self,solutionDict,sortKrit='C-Flux', fvaDIr=None, nrRea=5 ,resetIndexQual=True):
        dfList, keyList = [], []
        model = random.choice(list(self.modelDict.values()))
        # implement sort arguments as variable sortArgument, direction
        for sol in solutionDict.keys(): 
            customDF = model.summary(solution=solutionDict[sol],fva=fvaDIr).to_DataFrame_custom()
            if resetIndexQual==True:
                theMatrix   = [
            customDF['uptake'].sort_values(sortKrit,key=abs ,ascending=False).iloc[0:nrRea].reset_index(drop=True),
            customDF['secretion'].sort_values(sortKrit,key=abs ,ascending=False).iloc[0:nrRea].reset_index(drop=True)
                                ] 
            else:
                theMatrix   = [
                    customDF['uptake'].sort_values(sortKrit,key=abs ,ascending=False),
                    customDF['secretion'].sort_values(sortKrit,key=abs ,ascending=False)
                ]
                

            modelFrame=pd.concat(
                [pd.concat(theMatrix,
                keys=['Uptake', 'Secretion'], axis=1)],
                keys=[sol]
                ) 
            dfList.append(modelFrame)
            keyList.append(model)
            
        return pd.concat(dfList,axis=0) 
    