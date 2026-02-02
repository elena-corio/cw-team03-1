#from specklepy.objects.models.collections import Collection
from specklepy.objects import Base


def create_data_structure(old_breps, new_brep):
    # Create new Collections
    old_modules = Base()
    old_modules.name = "Old Modules"
    new_module = Base()
    new_module.name = "New Module"
    speckle_model = Base()
    speckle_model.name = "Speckle Model"
    
    #Add Elements to Collections
    old_modules.elements = old_breps
    new_module.elements = [new_brep]
    speckle_model.elements = [old_modules, new_module]

    return speckle_model
