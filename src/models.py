"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,super-init-not-called,unused-argument

import datetime
import typing

import sqlalchemy
from sqlalchemy import orm

from open_alchemy import models

Base = models.Base  # type: ignore


class _MeasurementDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    lat: float
    long: float
    time: str
    variable: str
    value: float
    location_id: int
    source_id: int


class MeasurementDict(_MeasurementDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int
    weather_station_id: typing.Optional[int]


class TMeasurement(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: Identifikacioni broj (interni ključ)
        lat: Geografska širina
        long: Geografska dužina
        time: Vreme merenja
        variable: Naziv meteorološke promenljive
        value: Vrednost meteorološke promenljive
        location_id: Identifikacioni broj lokacije
        source_id: Identifikacioni broj izvora merenja
        weather_station_id: Identifikacioni broj meteorološke stanice

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    lat: 'sqlalchemy.Column[float]'
    long: 'sqlalchemy.Column[float]'
    time: 'sqlalchemy.Column[datetime.datetime]'
    variable: 'sqlalchemy.Column[str]'
    value: 'sqlalchemy.Column[float]'
    location_id: 'sqlalchemy.Column[int]'
    source_id: 'sqlalchemy.Column[int]'
    weather_station_id: 'sqlalchemy.Column[typing.Optional[int]]'

    def __init__(self, lat: float, long: float, time: datetime.datetime, variable: str, value: float, location_id: int, source_id: int, id: typing.Optional[int] = None, weather_station_id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            lat: Geografska širina
            long: Geografska dužina
            time: Vreme merenja
            variable: Naziv meteorološke promenljive
            value: Vrednost meteorološke promenljive
            location_id: Identifikacioni broj lokacije
            source_id: Identifikacioni broj izvora merenja
            weather_station_id: Identifikacioni broj meteorološke stanice

        """
        ...

    @classmethod
    def from_dict(cls, lat: float, long: float, time: datetime.datetime, variable: str, value: float, location_id: int, source_id: int, id: typing.Optional[int] = None, weather_station_id: typing.Optional[int] = None) -> "TMeasurement":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            lat: Geografska širina
            long: Geografska dužina
            time: Vreme merenja
            variable: Naziv meteorološke promenljive
            value: Vrednost meteorološke promenljive
            location_id: Identifikacioni broj lokacije
            source_id: Identifikacioni broj izvora merenja
            weather_station_id: Identifikacioni broj meteorološke stanice

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMeasurement":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MeasurementDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Measurement: typing.Type[TMeasurement] = models.Measurement  # type: ignore


class _LocationDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    name: str
    country: str
    type: str
    latitude: float
    longitude: float


class LocationDict(_LocationDictBase, total=False):
    """TypedDict for properties that are not required."""

    elevation: typing.Optional[float]


class TLocation(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv lokacije
        country: Država lokacije
        type: Tip lokacije (grad, selo, planina, jezero, reka, itd.)
        latitude: Geografska širina
        longitude: Geografska dužina
        elevation: Nadmorska visina (u metrima)

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    country: 'sqlalchemy.Column[str]'
    type: 'sqlalchemy.Column[str]'
    latitude: 'sqlalchemy.Column[float]'
    longitude: 'sqlalchemy.Column[float]'
    elevation: 'sqlalchemy.Column[typing.Optional[float]]'

    def __init__(self, id: int, name: str, country: str, type: str, latitude: float, longitude: float, elevation: typing.Optional[float] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv lokacije
            country: Država lokacije
            type: Tip lokacije (grad, selo, planina, jezero, reka, itd.)
            latitude: Geografska širina
            longitude: Geografska dužina
            elevation: Nadmorska visina (u metrima)

        """
        ...

    @classmethod
    def from_dict(cls, id: int, name: str, country: str, type: str, latitude: float, longitude: float, elevation: typing.Optional[float] = None) -> "TLocation":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv lokacije
            country: Država lokacije
            type: Tip lokacije (grad, selo, planina, jezero, reka, itd.)
            latitude: Geografska širina
            longitude: Geografska dužina
            elevation: Nadmorska visina (u metrima)

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TLocation":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> LocationDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Location: typing.Type[TLocation] = models.Location  # type: ignore


class VariableDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    name: str
    unit: str


class TVariable(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Meteorološka promenljiva

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv meteorološke varijable
        unit: Jedinica merenja

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    unit: 'sqlalchemy.Column[str]'

    def __init__(self, id: int, name: str, unit: str) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteorološke varijable
            unit: Jedinica merenja

        """
        ...

    @classmethod
    def from_dict(cls, id: int, name: str, unit: str) -> "TVariable":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv meteorološke varijable
            unit: Jedinica merenja

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TVariable":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> VariableDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Variable: typing.Type[TVariable] = models.Variable  # type: ignore


class SourceDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    code: str
    name: str


class TSource(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Naziv izvora

    Attrs:
        id: Identifikacioni broj (kluč)
        code: Kod (skraćeni naziv)
        name: Naziv izvora

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    code: 'sqlalchemy.Column[str]'
    name: 'sqlalchemy.Column[str]'

    def __init__(self, id: int, code: str, name: str) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (kluč)
            code: Kod (skraćeni naziv)
            name: Naziv izvora

        """
        ...

    @classmethod
    def from_dict(cls, id: int, code: str, name: str) -> "TSource":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (kluč)
            code: Kod (skraćeni naziv)
            name: Naziv izvora

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TSource":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> SourceDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Source: typing.Type[TSource] = models.Source  # type: ignore


class _MeasurementSourceDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    latitude: float
    longitude: float
    code: str
    measurement_type: str


class MeasurementSourceDict(_MeasurementSourceDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TMeasurementSource(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: Identifikacioni broj (interni ključ)
        name: Naziv izvora merenja
        latitude: Geografska širina
        longitude: Geografska dužina
        code: Kod (skraćeni naziv izvora)
        measurement_type: Tip merenja (mesto, satelit, senzor itd.)

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    latitude: 'sqlalchemy.Column[float]'
    longitude: 'sqlalchemy.Column[float]'
    code: 'sqlalchemy.Column[str]'
    measurement_type: 'sqlalchemy.Column[str]'

    def __init__(self, name: str, latitude: float, longitude: float, code: str, measurement_type: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv izvora merenja
            latitude: Geografska širina
            longitude: Geografska dužina
            code: Kod (skraćeni naziv izvora)
            measurement_type: Tip merenja (mesto, satelit, senzor itd.)

        """
        ...

    @classmethod
    def from_dict(cls, name: str, latitude: float, longitude: float, code: str, measurement_type: str, id: typing.Optional[int] = None) -> "TMeasurementSource":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj (interni ključ)
            name: Naziv izvora merenja
            latitude: Geografska širina
            longitude: Geografska dužina
            code: Kod (skraćeni naziv izvora)
            measurement_type: Tip merenja (mesto, satelit, senzor itd.)

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TMeasurementSource":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> MeasurementSourceDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


MeasurementSource: typing.Type[TMeasurementSource] = models.MeasurementSource  # type: ignore


class _WeatherStationDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    location_id: int
    type: str
    capacity: int


class WeatherStationDict(_WeatherStationDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TWeatherStation(typing.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        id: Identifikacioni broj meteorološke stanice (interni ključ)
        name: Naziv meteorološke stanice
        location_id: Identifikacioni broj lokacije gde se nalazi stanica
        type: Tip meteorološke stanice
        capacity: Kapacitet stanice (broj merenja po jedinici vremena, npr.
            merenja po satu)

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    location_id: 'sqlalchemy.Column[int]'
    type: 'sqlalchemy.Column[str]'
    capacity: 'sqlalchemy.Column[int]'

    def __init__(self, name: str, location_id: int, type: str, capacity: int, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: Identifikacioni broj meteorološke stanice (interni ključ)
            name: Naziv meteorološke stanice
            location_id: Identifikacioni broj lokacije gde se nalazi stanica
            type: Tip meteorološke stanice
            capacity: Kapacitet stanice (broj merenja po jedinici vremena, npr.
                merenja po satu)

        """
        ...

    @classmethod
    def from_dict(cls, name: str, location_id: int, type: str, capacity: int, id: typing.Optional[int] = None) -> "TWeatherStation":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: Identifikacioni broj meteorološke stanice (interni ključ)
            name: Naziv meteorološke stanice
            location_id: Identifikacioni broj lokacije gde se nalazi stanica
            type: Tip meteorološke stanice
            capacity: Kapacitet stanice (broj merenja po jedinici vremena, npr.
                merenja po satu)

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWeatherStation":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WeatherStationDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


WeatherStation: typing.Type[TWeatherStation] = models.WeatherStation  # type: ignore
