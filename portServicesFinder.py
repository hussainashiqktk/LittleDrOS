import socket
import psutil

# Create a dictionary that will store the mapping of port numbers to service names
port_service_mapping = {}

# Iterate over all open connections
for conn in psutil.net_connections(kind='inet'):
    # Get the local address, which is a tuple (ip_address, port)
    local_address = conn.laddr

    # If the connection is not listening, skip it
    if not conn.status == 'LISTEN':
        continue

    # Get the port number from the local address
    port = local_address.port

    # Use the getservbyport() function from the socket module to get the service name for the port
    service_name = socket.getservbyport(port)

    # Add the port number and service name to the dictionary
    port_service_mapping[port] = service_name

# Print the dictionary
print(port_service_mapping)
