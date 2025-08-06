import serial

# === Configure your serial port ===
port = 'COM8'         # Replace with your COM port (e.g., 'COM4', '/dev/ttyUSB0')
baudrate = 115200     # Must match your FPGA UART baud rate

# Open serial port
ser = serial.Serial(port, baudrate, timeout=1)

print(f"Listening on {port} at {baudrate} baud...\n")

try:
    while True:
        if ser.in_waiting:
            byte = ser.read()  # Read 1 byte
            value = int.from_bytes(byte, byteorder='big')  # Convert to integer
            print(f"Received: 0x{value:02X} ({value})")
except KeyboardInterrupt:
    print("\nStopped by user.")
    ser.close()


