

from Tab_CrossSection import LoadTabElements as CSI
from Tab_Home import LoadTabElements as HI
from Tab_LayUp import LoadTabElements as LUI
from Tab_Materials import LoadTabElements as MI

class connectTabs:
    def __init__(self):
        CSI()
        HI()
        LUI()
        MI()
        pass