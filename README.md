# Disk Partition Manager

A professional terminal-based disk partition utility built with Python and Textual, providing an intuitive interface for Windows disk management operations.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

Disk Partition Manager is a modern, user-friendly wrapper around Windows' native `diskpart` utility. It features a clean terminal user interface built with Textual, making complex disk operations accessible through simple menu navigation.

### Key Features

- **🖥️ Interactive TUI**: Clean, professional terminal interface
- **💾 Disk Management**: List, clean, and partition disk drives
- **🔒 Safe Operations**: Clear prompts and confirmation workflows
- **⚡ Quick Setup**: Single-file executable with batch launcher
- **🎯 Windows Native**: Leverages Windows diskpart for reliable operations

## Screenshots

```
Microsoft Disk Partition Utility
Created by Hardik Kawale

> List Disks
> Clean Disk
> Create Partition
> Exit
```

## Prerequisites

- **Operating System**: Windows 10/11 or Windows Server 2016+
- **Python**: Version 3.8 or higher
- **Privileges**: Administrator rights (required for disk operations)
- **Dependencies**: Textual library

## Installation

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hardik-369/Disk_tool.git
   cd Disk_tool
   ```

2. **Install dependencies**:
   ```bash
   pip install textual
   ```

3. **Run as Administrator**:
   ```bash
   # Using the batch launcher
   run.bat

   # Or directly with Python
   python disk_tool.py
   ```

### Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
pip install textual
python disk_tool.py
```

## Usage

### Main Menu Options

| Option | Description |
|--------|-------------|
| **List Disks** | Display all available disk drives with detailed information |
| **Clean Disk** | Completely wipe a selected disk (⚠️ **Data Loss Warning**) |
| **Create Partition** | Create new primary partition with NTFS formatting |
| **Exit** | Safely close the application |

### Operation Workflows

#### Listing Disks
1. Select "List Disks" from main menu
2. View comprehensive disk information
3. Note disk numbers for subsequent operations

#### Cleaning a Disk
⚠️ **WARNING**: This operation will permanently erase ALL data on the selected disk.

1. Select "Clean Disk"
2. Enter the disk number (from disk list)
3. Confirm operation
4. Monitor progress and results

#### Creating Partitions
1. Select "Create Partition"
2. Specify target disk number
3. Enter partition size in MB
4. Automatic NTFS formatting and drive letter assignment

## File Structure

```
disk-partition-manager/
├── disk_tool.py          # Main application file
├── disk_tool.bat              # Windows batch launcher
├── README.md            # This documentation

```

## Technical Details

### Architecture

The application follows a modular screen-based architecture:

- **MainMenu**: Primary navigation interface
- **ListDisksScreen**: Disk enumeration and display
- **CleanDiskScreen**: Disk wiping operations
- **CreatePartitionScreen**: Partition creation workflow
- **ResultScreen**: Operation results and feedback

### Dependencies

```python
textual>=0.40.0  # Modern TUI framework
```

### Diskpart Integration

The tool generates temporary diskpart scripts for each operation, ensuring:
- Atomic operations
- Error handling
- Output capture
- Clean script management

## Security Considerations

- **Administrator Privileges**: Required for all disk operations
- **Data Loss Prevention**: Clear warnings before destructive operations
- **Input Validation**: Disk numbers and sizes are validated
- **Temporary Files**: Scripts are automatically cleaned up

## Error Handling

The application includes comprehensive error handling for:
- Invalid disk numbers
- Insufficient permissions
- Diskpart execution failures
- File system errors
- Input validation errors

## Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
git clone https://github.com/yourusername/disk-partition-manager.git
cd disk-partition-manager
python -m venv dev-env
dev-env\Scripts\activate
pip install textual pytest black flake8
```

### Code Standards

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for all functions
- Write unit tests for new features

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| "Access Denied" | Run as Administrator |
| "Python not found" | Ensure Python is in system PATH |
| "Textual not found" | Install with `pip install textual` |
| "Disk not accessible" | Check disk connection and permissions |

### Debug Mode

Enable verbose output:
```bash
python disk_tool.py --debug
```

## Changelog

### v1.0.0 (Current)
- Initial release
- Basic disk operations (list, clean, partition)
- Textual-based TUI
- Windows batch launcher

## Roadmap

- [ ] Linux/macOS support
- [ ] Advanced partition types (GPT, extended)
- [ ] Disk health monitoring
- [ ] Configuration file support
- [ ] Logging system
- [ ] Multi-disk operations

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Hardik Kawale**
- GitHub: [@hardikkawale](https://github.com/hardikkawale)
- Email: your.email@example.com

## Acknowledgments

- [Textual](https://github.com/Textualize/textual) - Modern Python TUI framework
- Microsoft Diskpart - Windows disk partitioning utility
- Python Community - For excellent documentation and support

## Disclaimer

This software is provided "AS IS" without warranty. Users are responsible for data backup before performing disk operations. The author is not liable for any data loss or system damage resulting from the use of this software.

---

⭐ **Star this repository if it helped you!**

**Made with ❤️ by Hardik Kawale**
