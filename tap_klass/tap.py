"""klass tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_klass import streams


class Tapklass(Tap):
    """klass tap class."""

    name = "tap-klass"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "classifications",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "name", 
                        th.StringType, 
                        required=True, 
                        description="Given name of the classification"
                    ),
                    th.Property(
                        "id", 
                        th.StringType, 
                        required=True
                    ),
                    th.Property(
                        "valid_at", 
                        th.StringType
                    ),
                    th.Property(
                        "valid_from", 
                        th.StringType
                    ),
                    th.Property(
                        "valid_to", 
                        th.StringType
                    ),
                    th.Property(
                        "language",
                        th.StringType,
                        default="nb",
                        allowed_values=["nb", "nn", "en"],
                    )
                )
            )
        )
    ).to_dict()

    def discover_streams(self) -> list[streams.klassStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """

        for classification in self.config["classifications"]:
            yield streams.ClassificationStream(
                tap=self,
                classification=classification
            )


if __name__ == "__main__":
    Tapklass.cli()
