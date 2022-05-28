'''
def mySummaryFunc(comparison,nrRea=3):
    dfListUp, dfListSec, keyList = [], [], []
    
    for model in comparison.modelDict.keys():
        #modelFrame  = pd.DataFrame(theMatrix , np.linspace(1,nrRea,nrRea), groups)
        theUpMatrix     =      comp.dataFrameDict[model]['uptake'   ].iloc[0:3]
        theSecMatrix    =      comp.dataFrameDict[model]['secretion'].iloc[0:3]
        #modelFrame=pd.concat(
        #    [pd.concat(theMatrix,
        #    keys=['Uptake', 'Secretion'], axis=1)],
        #    keys=[model]
        #) 
        dfListUp.append(theUpMatrix)
        dfListSec.append(theSecMatrix)
        keyList.append(model)
        
    return pd.concat(dfListUp,axis=1,keys=keyList), pd.concat(dfListSec,axis=1,keys=keyList,ignore_index=True)
'''