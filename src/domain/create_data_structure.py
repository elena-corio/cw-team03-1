#from specklepy.objects.models.collections import Collection
from specklepy.objects import Base
from domain.add_properties import add_properties


def create_data_structure(old_breps, new_brep):
    # Create new Collections
    old_modules = Base()
    old_modules.name = "Old Modules"
    new_module = Base()
    new_module.name = "New Module"
    speckle_model = Base()
    speckle_model.name = "Speckle Model"
    
    # Add properties
    speckle_model["properties"] = {"Tower": "Team_03.1"}
    module_01 = add_properties(old_breps[0], "01", "Symon Kipkemei")
    module_03 = add_properties(old_breps[1], "03", "Symon Kipkemei")
    module_02 = add_properties(new_brep, "02", "Elena Corio")
    
    #Add Elements to Collections
    old_modules.elements = [module_01, module_03]
    new_module.elements = [module_02]
    speckle_model.elements = [old_modules, new_module]

    return speckle_model
