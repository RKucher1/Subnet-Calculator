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
- **Terminal or File Output**: Print results to terminal for quick analysis or save to file for documentation
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
python subnet.py <input_file> <prefix> [output_file] [--exclude <exclusion_file>]
```

### Parameters

- `<input_file>`: Path to the file containing IP addresses (one per line)
- `<prefix>`: CIDR prefix length (16 or 24)
- `[output_file]` (optional): Path where the output will be written. If omitted, results print to terminal
- `--exclude <exclusion_file>` (optional): Path to file containing IPs to exclude

### Examples

#### Example 1: Print /24 subnets to terminal

```bash
python subnet.py network.txt 24
```

#### Example 2: Group IPs into /16 subnets and save to file

```bash
python subnet.py network.txt 16 output.txt
```

#### Example 3: Print /24 subnets to terminal with exclusions

```bash
python subnet.py network.txt 24 --exclude exclusions.txt
```

#### Example 4: Save /16 subnets to file with exclusions

```bash
python subnet.py network.txt 16 output.txt --exclude exclusions.txt
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

## Output Format

The output (either to terminal or file) will contain CIDR blocks with host counts:

```
10.0.0.0/24 - Hosts: 2
192.168.1.0/24 - Hosts: 2
192.168.2.0/24 - Hosts: 1

Total Subnets: 3
Total Hosts: 5
```

When printing to terminal (no output file specified), the results are displayed directly to stdout.
When an output file is specified, the results are written to the file and a summary is printed to the terminal.

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
- **Quick Analysis**: View subnet groupings instantly in the terminal without creating files
- **Penetration Testing**: Quickly organize target IPs by subnet during engagements without leaving artifacts

## How It Works

1. Reads all IP addresses from the input file
2. Sorts the IP addresses numerically
3. Applies exclusions (if specified)
4. Groups IPs based on the specified prefix (/16 or /24)
5. Counts hosts in each subnet range
6. Outputs the results to terminal or file (if specified) with summary statistics

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
