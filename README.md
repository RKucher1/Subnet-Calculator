# Subnet Calculator

A Python tool that groups IP addresses into CIDR notation blocks (/16 or /24 subnets) with host counting capabilities and exclusion support.

## Overview

This subnet calculator reads a list of IP addresses from a file, groups them into specified CIDR blocks (either /16 or /24), and generates a summary report showing:
- Each unique subnet with its host count
- Total number of subnets
- Total number of hosts

The tool also supports excluding specific IP addresses from the grouping process, making it useful for network analysis and planning.

## Features

- **Flexible CIDR Grouping**: Group IP addresses into /16 or /24 CIDR blocks
- **IP Exclusion Support**: Exclude specific IPs from the grouping using an exclusion file
- **Automatic Sorting**: IPs are automatically sorted before processing
- **Summary Statistics**: Provides total subnet count and total host count
- **Per-Subnet Host Counts**: Shows the number of hosts in each subnet range

## Requirements

- Python 3.x
- No external dependencies (uses standard library only)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/RKucher1/Subnet-Calculator.git
cd Subnet-Calculator
```

2. Ensure Python 3 is installed:
```bash
python3 --version
```

## Usage

### Basic Syntax

```bash
python subnet.py <input_file> <output_file> <prefix> [--exclude <exclusion_file>]
```

### Parameters

- `<input_file>`: Path to the file containing IP addresses (one per line)
- `<output_file>`: Path where the output will be written
- `<prefix>`: CIDR prefix length (16 or 24)
- `--exclude <exclusion_file>` (optional): Path to file containing IPs to exclude

### Examples

#### Example 1: Group IPs into /24 subnets

```bash
python subnet.py network.txt output.txt 24
```

#### Example 2: Group IPs into /16 subnets

```bash
python subnet.py network.txt output.txt 16
```

#### Example 3: Group IPs with exclusions

```bash
python subnet.py network.txt output.txt 24 --exclude exclusions.txt
```

## Input File Format

The input file should contain one IP address per line:

```
192.168.1.10
192.168.1.20
192.168.2.5
10.0.0.1
10.0.0.2
```

## Output File Format

The output file will contain CIDR blocks with host counts:

```
10.0.0.0/24 - Hosts: 2
192.168.1.0/24 - Hosts: 2
192.168.2.0/24 - Hosts: 1

Total Subnets: 3
Total Hosts: 5
```

## Exclusion File Format

The exclusion file should contain one IP address per line (same format as input file):

```
192.168.1.10
10.0.0.1
```

## Use Cases

- **Network Planning**: Identify how IP addresses are distributed across subnets
- **IP Inventory**: Analyze existing IP address allocations
- **Subnet Optimization**: Determine optimal subnet sizing based on actual usage
- **Security Analysis**: Identify IP ranges for firewall rules or access controls
- **Documentation**: Generate subnet documentation from IP lists

## How It Works

1. Reads all IP addresses from the input file
2. Sorts the IP addresses numerically
3. Applies exclusions (if specified)
4. Groups IPs based on the specified prefix (/16 or /24)
5. Counts hosts in each subnet range
6. Writes the results to the output file with summary statistics

## CIDR Notation

- **/16 subnet**: Groups by the first two octets (e.g., 192.168.0.0/16 covers 192.168.0.0 - 192.168.255.255)
- **/24 subnet**: Groups by the first three octets (e.g., 192.168.1.0/24 covers 192.168.1.0 - 192.168.1.255)

## Error Handling

The script will exit with an error message if:
- Incorrect number of arguments are provided
- The prefix is not an integer
- Input files cannot be read
- IP addresses are malformed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

RKucher1
