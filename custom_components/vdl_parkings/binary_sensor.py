"""Binary sensors for VDL Parkings integration."""

from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorDeviceClass
)
from homeassistant.helpers.entity import (
    DeviceInfo,
    EntityCategory
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, CONF_PARKINGS


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up binary sensors for VDL Parkings integration."""

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

        entities.append(ParkingFull(coordinator, parking_id, device_info))
        entities.append(ParkingOpen(coordinator, parking_id, device_info))
        entities.append(ParkingOutOfService(coordinator, parking_id, device_info))

    async_add_entities(entities)


class ParkingOpen(CoordinatorEntity, BinarySensorEntity):
    """Binary sensor to indicate if parking is open."""

    _attr_translation_key = "open"
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.OPENING
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
        return f"vdl_parking_{self.parking_id}_open"

    @property
    def is_on(self):
        return self.coordinator.data[self.parking_id]["open"]


class ParkingFull(CoordinatorEntity, BinarySensorEntity):
    """Binary sensor to indicate if parking is full."""

    _attr_translation_key = "full"
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.PROBLEM
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
        return f"vdl_parking_{self.parking_id}_full"

    @property
    def is_on(self):
        return self.coordinator.data[self.parking_id]["full"]


class ParkingOutOfService(CoordinatorEntity, BinarySensorEntity):
    """Binary sensor to indicate if parking is out of service."""

    _attr_translation_key = "out_of_service"
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.PROBLEM
    _attr_entity_registry_enabled_default = True
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator, parking_id, device_info):
        super().__init__(coordinator)
        self.parking_id = parking_id
        self._device_info = device_info

    @property
    def device_info(self):
        return self._device_info

    @property
    def unique_id(self):
        return f"vdl_parking_{self.parking_id}_out_of_service"

    @property
    def is_on(self):
        return self.coordinator.data[self.parking_id]["out_of_service"]
