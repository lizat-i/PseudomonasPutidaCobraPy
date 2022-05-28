import pandas as pd

def reformatHTML(solutionHTLM):
  return pd.DataFrame

def createOutput(model):
  df2 = pd.DataFrame(
    {
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo",
    }
)
  return df2

def ImportFunction(nameList):
    mainPATH                        = '/Users/ivanlizat/Documents/devel/folderForGit/PseudomonasPutidaCobraPy'
    relativModelPATH = mainPATH + '/MatlabExportedModels'
    modelDict = {}
    for name in nameList:
        modelDict[ "{0}".format(name.removesuffix(".xml"))] = pyf.cobra.io.read_sbml_model(
            relativModelPATH + '/' + str(name))
    return modelDict

def helloW():
  print(pyf.func2.addForHello())