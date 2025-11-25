import ipaddress
import sys

def load_exclusions(exclusion_file_path):
    # Load IPs from the exclusion file
    with open(exclusion_file_path, 'r') as f:
        return set(ipaddress.IPv4Address(line.strip()) for line in f if line.strip())

def generate_cidr_notation_with_counts(input_file_path, output_file_path, prefix, exclusion_file_path=None):
    # Read IP addresses from the main file and sort them
    with open(input_file_path, 'r') as f:
        ip_addresses = sorted([ipaddress.IPv4Address(line.strip()) for line in f if line.strip()])

    # Load and apply exclusions if an exclusion file is provided
    if exclusion_file_path:
        exclusions = load_exclusions(exclusion_file_path)
        ip_addresses = [ip for ip in ip_addresses if ip not in exclusions]

    # Group IPs by the specified prefix (/16 or /24)
    grouped_ips = {}
    for ip in ip_addresses:
        # Define the grouping key based on the specified prefix
        if prefix == 16:
            grouping_key = f"{ip.packed[0]}.{ip.packed[1]}.0.0/16"
        elif prefix == 24:
            grouping_key = f"{ip.packed[0]}.{ip.packed[1]}.{ip.packed[2]}.0/24"

        if grouping_key not in grouped_ips:
            grouped_ips[grouping_key] = []
        grouped_ips[grouping_key].append(ip)

    # Initialize counters for total hosts and total subnets
    total_hosts = 0
    total_subnets = 0

    # Prepare output lines
    output_lines = []
    for prefix_key, ips in grouped_ips.items():
        host_count = len(ips)  # Count the hosts in this range
        total_hosts += host_count
        total_subnets += 1
        output_lines.append(f"{prefix_key} - Hosts: {host_count}\n")

    # Add totals at the end
    output_lines.append(f"\nTotal Subnets: {total_subnets}\n")
    output_lines.append(f"Total Hosts: {total_hosts}\n")

    # Write to file or print to terminal
    if output_file_path:
        with open(output_file_path, 'w') as f:
            f.writelines(output_lines)
        print(f"All IPs grouped into /{prefix} CIDR notation with host counts written to {output_file_path}")
        print(f"Total Subnets: {total_subnets}, Total Hosts: {total_hosts}")
    else:
        # Print to terminal
        for line in output_lines:
            print(line, end=''))

# Main function to handle command-line arguments
if __name__ == "__main__":
    # Parse arguments
    if len(sys.argv) < 3:
        print("Usage: python subnet.py <input_file_path> <prefix> [output_file_path] [--exclude <exception_file_path>]")
        print("Examples:")
        print("  python subnet.py network.txt 16")
        print("  python subnet.py network.txt 24 output.txt")
        print("  python subnet.py network.txt 16 --exclude exclusions.txt")
        print("  python subnet.py network.txt 24 output.txt --exclude exclusions.txt")
        sys.exit(1)

    # Assign command-line arguments
    input_file_path = sys.argv[1]
    try:
        prefix = int(sys.argv[2])
    except ValueError:
        print("Prefix must be an integer (16 or 24).")
        sys.exit(1)

    # Parse optional arguments
    output_file_path = None
    exclusion_file_path = None

    # Check remaining arguments
    i = 3
    while i < len(sys.argv):
        if sys.argv[i] == '--exclude':
            if i + 1 < len(sys.argv):
                exclusion_file_path = sys.argv[i + 1]
                i += 2
            else:
                print("Error: --exclude requires a file path")
                sys.exit(1)
        elif output_file_path is None and not sys.argv[i].startswith('--'):
            output_file_path = sys.argv[i]
            i += 1
        else:
            print(f"Error: Unknown argument '{sys.argv[i]}'")
            sys.exit(1)

    # Run the function with specified arguments
    generate_cidr_notation_with_counts(input_file_path, output_file_path, prefix, exclusion_file_path)
