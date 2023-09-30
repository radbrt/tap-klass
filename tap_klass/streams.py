"""Stream type classes for tap-klass."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_klass.client import klassStream


# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class ClassificationStream(klassStream):
    """Define custom stream."""

    def __init__(self, *args, **kwargs):
        """Custom init to store config"""

        self.classification = kwargs.pop("classification")

        super().__init__(*args, **kwargs)


    @property
    def name(self) -> str:
        """Return a unique ID for this stream."""
        return self.classification.get("name")

    @property
    def path(self) -> str:
        """Return the API path for this stream."""

        if self.classification.get("valid_at"):
            argument = f"codesAt.json?date={self.classification.get('valid_at')}"
        elif self.classification.get("valid_from") and self.classification.get("valid_to"):
            argument = f"codes.json?from={self.classification.get('valid_from')}&to={self.classification.get('valid_to')}"
        else:
            raise ValueError("Missing valid_at or valid_from and valid_to")
        
        argument = f"{argument}&language={self.classification.get('language')}"

        return f"/classifications/{self.classification.get('id')}/{argument}"



    primary_keys: t.ClassVar[list[str]] = ["code"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "code",
            th.StringType,
            description="The code of the item in the classification",
        ),
        th.Property(
            "parentCode",
            th.StringType,
            description="For hierarcical classifications, the code of the parent classification",
        ),
        th.Property(
            "level",
            th.StringType,
            description="For hierarcical classifications, the level of the classification",
        ),
        th.Property(
            "shortName", 
            th.StringType,
            description="The short name of the item"
        ),
        th.Property(
            "presentationName", 
            th.StringType,
            description="The presentation name of the item"
        ),
        th.Property(
            "validFrom",
            th.DateType,
            description="Item valid from date ISO 8601",
        ),
        th.Property(
            "validTo", 
            th.StringType,
            description="Item valid to date ISO 8601"
            ),
        th.Property(
            "notes",
            th.StringType,
            description="Notes about the item"
        ),
        th.Property(
            "validFromInRequestedRange",
            th.StringType,
            description="Item valid from date ISO 8601"
        ),
        th.Property(
            "validToInRequestedRange",
            th.StringType,
            description="Item valid to date ISO 8601"
        ),
    ).to_dict()


