def isDuplicated(Array):
    if len(Array) == 0:
        return "Null"
    saveIndex = {}
    result = []
    for i in range(len(Array)): 
        try:
            saveIndex[Array[i]]['index'].append(i)
            saveIndex[Array[i]]['count'] = len(saveIndex[Array[i]]['index'])
        except:
            saveIndex[Array[i]] = {'index':[i]}
            saveIndex[Array[i]]['count'] = len(saveIndex[Array[i]]['index'])
    for j in saveIndex:
        if saveIndex[j]['count'] > 1:
            result.append(f"{j} , index : {saveIndex[j]['index']} , count : {saveIndex[j]['count']}")
    if len(result) == 0:
        return False
    return result