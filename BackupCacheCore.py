import hou

def childrenOfNode(node):
    result = []
    if node != None:
        for n in node.children():
            result.append(n)
            result += childrenOfNode(n)
    return result
def fileParmOfNode(node):
    result = []
    if node != None:
        for parm in node.parms():
            if parm.parmTemplate().type() == hou.parmTemplateType.String:
                if parm.parmTemplate().stringType() == hou.stringParmType.FileReference:
                    result.append(parm)
    return result

def getAllCachePath():
    roots = ['/ch', '/img', '/mat', '/obj', '/out', '/shop', '/stage', '/tasks', '/vex']
    nodes = []
    for root in roots:
        nodes.extend(childrenOfNode(hou.node(root)))
    fileParms = []
    for node in nodes:
        fileParms.extend(fileParmOfNode(node))
    paths = []
    for parm in fileParms:
        if parm.evalAsString() != '':
            paths.append(parm.evalAsString())
    inHIPpath = []
    for path in paths:
        hip = '/'.join(hou.hipFile.path().split('/')[0:-1])
        if hip in path:
            if path not in inHIPpath:
                inHIPpath.append(path)
    return inHIPpath
    
paths = getAllCachePath()