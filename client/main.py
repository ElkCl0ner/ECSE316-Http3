import struct
import random
import socket

def buildRequest():
    ### QUIC HEADER ###

    # Generate Connection ID
    connection_id = random.randint(0, 2**64)

    # Quic version
    quic_version = "Q025"

    # Skip diversification nonce

    # Packet number
    packet_number = 1

    # Build packet
    packet = struct.pack('>H', )
    packet += struct.pack('>Q', connection_id)
    packet += struct.pack('', quic_version)
    packet += struct.pack('', packet_number)

    ### FRAME 1 - STREAM: GET REQUEST ###


    ### Frame 2 - STREAM: GET REQUEST ###


def main():
    
    # Build request
    request = buildRequest()

    # Send request

    # Receive response

        # Send ACK

        # Terminate connection (if all data received)

if __name__ == "__main__":
    main()
