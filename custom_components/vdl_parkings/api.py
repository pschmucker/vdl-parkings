"""VDL API module for fetching parking data."""

import logging
import aiohttp


_LOGGER = logging.getLogger(__name__)

API_URL = "https://www.vdl.lu/fr/parking/data.json"


# pylint: disable=too-few-public-methods
class VdlParkingApi:
    """API client for fetching parking data from the VDL API."""

    async def fetch(self):
        """Fetch parking data from the VDL API."""

        async with aiohttp.ClientSession() as session:

            async with session.get(API_URL) as response:

                # Print status code, content type, and response text for debugging
                content_type = response.headers.get("Content-Type", "")
                text = await response.text()

                _LOGGER.debug("Response: %s; %s; %s", response.status, content_type, text[:500])

                response.raise_for_status()

                return await response.json()
