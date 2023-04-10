"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_coingecko.tap import TapCoingecko


SAMPLE_CONFIG = {
    "start_date":  (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
    "tokens": "ethereum,decentraland,dai",
    "api_url": "https://api.coingecko.com/api/v3",
    "wait_time_between_requests": 5,
    "token_mapping": {
        "decentraland": "MANA",
        "ethereum": "ETH",
        "dai": "DAI",
    }
}


# Run standard built-in tap tests from the SDK:
TestTapcoingecko = get_tap_test_class(
    tap_class=TapCoingecko,
    config=SAMPLE_CONFIG,
    include_tap_tests=False,
    include_stream_tests=False,
)


# TODO: Create additional tests as appropriate for your tap.
