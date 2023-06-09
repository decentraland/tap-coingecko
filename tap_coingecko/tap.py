"""Coingecko tap class."""
from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_coingecko.streams import CoingeckoStream

STREAM_TYPES = [CoingeckoStream]


class TapCoingecko(Tap):
    """Coingecko tap class."""

    name = "tap-coingecko"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "tokens",
            th.StringType,
            required=True,
            description="The name of the tokens to import",
            default="ethereum",
        ),
        th.Property(
            "api_url",
            th.StringType,
            required=True,
            description="Coingecko's api url",
            default="https://api.coingecko.com/api/v3",
        ),
        th.Property(
            "start_date",
            th.StringType,
            required=True,
            description="First date to obtain token data price for",
            default="2022-03-01",
        ),
        th.Property(
            "wait_time_between_requests",
            th.IntegerType,
            required=True,
            description="Number of seconds to wait between requests",
            default=5,
        ),
        th.Property(
            "token_mapping",
            th.ObjectType(additional_properties=True),
            required=False,
            description="Mapping of token names to coingecko's token names",
            default={
                "decentraland": "MANA",
                "ethereum": "ETH",
                "dai": "DAI",
                "matic-network": "MATIC",
                "bitcoin": "BTC",
                "binancecoin": "BNB",
                "tether": "USDT",
                "usd-coin": "USDC",
            },
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
