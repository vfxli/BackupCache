

from PySide2 import QtWidgets
import BackupCacheCore

class ViewerStateBrowser(QtWidgets.QFrame):
    def __init__(self,parent=None):
        super(ViewerStateBrowser, self).__init__(parent)

        #scene setup
        self._scene_viewer = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
        self._currentState = None

        vbox  = QtWidgets.QVBoxLayout()
    
        RefreshBtn = QtWidgets.QPushButton('Refresh')
        vbox.addWidget(RefreshBtn)
        paths = BackupCacheCore.paths
        for path in paths:
            title  = QtWidgets.QLabel(path)
            size = QtWidgets.QLabel('10G')
            hbox = QtWidgets.QHBoxLayout()
            hbox.addWidget(title)
            hbox.addWidget(size)
            vbox.addLayout(hbox)

        self.setLayout(vbox)