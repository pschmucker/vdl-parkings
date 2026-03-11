"""Sensors for VDL Parkings integration."""

from homeassistant.components.sensor import (
    SensorEntity,
    SensorStateClass,
)
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, CONF_PARKINGS


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensors for VDL Parkings integration."""

    coordinator = hass.data[DOMAIN][entry.entry_id]
    selected = entry.data[CONF_PARKINGS]
    entities = []

    for parking_id in selected:
        device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id, parking_id)},
            name=coordinator.data[parking_id]["name"],
            entry_type="service",
            manufacturer="VDL",
            model="Parking",
        )

        entities.append(ParkingAvailableSpaces(coordinator, parking_id, device_info))
        entities.append(ParkingTotalCapacity(coordinator, parking_id, device_info))
        entities.append(ParkingOccupiedSpaces(coordinator, parking_id, device_info))
        entities.append(ParkingOccupancyRate(coordinator, parking_id, device_info))

    async_add_entities(entities)


class ParkingAvailableSpaces(CoordinatorEntity, SensorEntity):
    """Sensor for available parking spaces."""

    _attr_translation_key = "available_spaces"
    _attr_has_entity_name = True
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_entity_registry_enabled_default = True

    def __init__(self, coordinator, parking_id, device_info):
        super().__init__(coordinator)
        self.parking_id = parking_id
        self._device_info = device_info

    @property
    def device_info(self):
        return self._device_info

    @property
    def unique_id(self):
        return f"vdl_parking_{self.parking_id}_available_spaces"

    @property
    def native_value(self):
        return self.coordinator.data[self.parking_id]["available_spaces"]


class ParkingTotalCapacity(CoordinatorEntity, SensorEntity):
    """Sensor for total parking capacity."""

    _attr_translation_key = "total_capacity"
    _attr_has_entity_name = True
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_entity_registry_enabled_default = True

    def __init__(self, coordinator, parking_id, device_info):
        super().__init__(coordinator)
        self.parking_id = parking_id
        self._device_info = device_info

    @property
    def device_info(self):
        return self._device_info

    @property
    def unique_id(self):
        return f"vdl_parking_{self.parking_id}_total_capacity"

    @property
    def native_value(self):
        return self.coordinator.data[self.parking_id]["total_capacity"]


class ParkingOccupiedSpaces(CoordinatorEntity, SensorEntity):
    """Sensor for occupied parking spaces."""

    _attr_translation_key = "occupied_spaces"
    _attr_has_entity_name = True
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_entity_registry_enabled_default = True

    def __init__(self, coordinator, parking_id, device_info):
        super().__init__(coordinator)
        self.parking_id = parking_id
        self._device_info = device_info

    @property
    def device_info(self):
        return self._device_info

    @property
    def unique_id(self):
        return f"vdl_parking_{self.parking_id}_occupied_spaces"

    @property
    def native_value(self):
        return self.coordinator.data[self.parking_id]["occupied_spaces"]


class ParkingOccupancyRate(CoordinatorEntity, SensorEntity):
    """Sensor for parking occupancy rate."""

    _attr_translation_key = "occupancy_rate"
    _attr_has_entity_name = True
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = "%"
    _attr_entity_registry_enabled_default = True

    def __init__(self, coordinator, parking_id, device_info):
        super().__init__(coordinator)
        self.parking_id = parking_id
        self._device_info = device_info

    @property
    def device_info(self):
        return self._device_info

    @property
    def unique_id(self):
        return f"vdl_parking_{self.parking_id}_occupancy_rate"

    @property
    def native_value(self):
        return self.coordinator.data[self.parking_id]["occupancy_rate"]
