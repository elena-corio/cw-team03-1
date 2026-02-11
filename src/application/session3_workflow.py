from specklepy.transports.server import ServerTransport
from adapters.get_latest_version import get_latest_version
from adapters.get_client import get_client
from adapters.receive_data import receive_data
from adapters.send_data import send_data
from adapters.create_version import create_version
from domain.create_data_structure import create_data_structure
from domain.modify_geometry import modify_geometry
from config import PROJECT_ID


def run_receive_and_send_data_workflow():
    client  = get_client()
    #Receive data
    transport = ServerTransport(stream_id=PROJECT_ID, client=client)
    version = get_latest_version(client)
    received_data = receive_data(version, transport)

    # Process data
    old_breps = received_data.elements[0].elements
    new_brep = modify_geometry(old_breps[0])
    data = create_data_structure(old_breps, new_brep)

    # Send data
    object_id = send_data(transport, data)
    create_version(client, object_id)