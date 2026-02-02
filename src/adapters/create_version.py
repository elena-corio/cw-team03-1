from config import PROJECT_ID
from config import MODEL_NAME
from specklepy.core.api.inputs.version_inputs import CreateVersionInput
from specklepy.core.api.inputs.model_inputs import CreateModelInput

def create_model_and_version(client, object_id):
    # Create a model
    model_input = CreateModelInput(
        project_id=PROJECT_ID,
        name=MODEL_NAME,
        description="This is my first model"
    )
    model = client.model.create(model_input)
    
    # Create a version
    version_input = CreateVersionInput(
        project_id=PROJECT_ID,
        model_id=model.id,
        object_id=object_id,
    )
    version = client.version.create(version_input)

    return version

    print(f"✓ Created model: {model.id}")
    print(f"✓ Created version: {version.id}")