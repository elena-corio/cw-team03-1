def add_properties(brep, module, designer):
    brep["properties"] = {
        "Module": module,
        "Designer": designer}
    return brep
    