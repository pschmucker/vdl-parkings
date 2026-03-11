"""Diagnostics for VDL Parkings integration."""


async def async_get_config_entry_diagnostics(hass, entry):
    """Return diagnostics for a config entry."""

    coordinator = hass.data["vdl_parkings"][entry.entry_id]

    return coordinator.data
