"""The VDL Parkings integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import VdlParkingCoordinator
from .zone import create_parking_zones, remove_parking_zones


PLATFORMS = ["binary_sensor", "sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Async setup of the VDL Parkings integration from config entry."""

    coordinator = VdlParkingCoordinator(hass)

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await create_parking_zones(hass, coordinator, entry)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Async unload of the VDL Parkings integration config entry."""

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        await remove_parking_zones(hass, entry)

        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
