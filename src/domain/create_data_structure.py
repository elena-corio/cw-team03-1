from specklepy.objects.models.collections import Collection


def create_data_structure(old_breps, new_brep):
    # Create new Collections
    old_modules = Collection(name="Old Modules")
    new_module = Collection(name="New Module")
    speckle_model = Collection(name="Speckle Model")
    
    #Add Elements to Collections
    old_modules.elements = old_breps
    new_module.elements = [new_brep]
    speckle_model.elements = [old_modules, new_module]

    return speckle_model
