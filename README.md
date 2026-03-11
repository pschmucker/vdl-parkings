# VDL Parkings Home Assistant custom integration

Custom component to track availability of public parkings in Luxembourg (VDL) via the official JSON API.


## Disclaimer

> [!WARNING]
> 🚧 **Beta version** - This integration is under active development 🚧
>
> - Features may change/break between updates
> - Use for testing only, **at your own risk**
> - Backup your configuration before installing
> - [Report issues](https://github.com/pschmucker/vdl-parkings/issues)


## Installation

- Place the `custom_components/vdl_parkings` folder in your `config` directory.
- Restart Home Assistant.
- Add integration via UI (search for *VDL Parkings*).

Configuration options allow selecting which parkings to monitor.


## Features

- `sensor` entities for total capacity, available spaces, occupied places
- `binary_sensor` entities for open, full, out of service
- `zone` for geolocation
