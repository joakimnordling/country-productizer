from typing import List, Optional

from pydantic import BaseModel, Field, constr
from stringcase import camelcase


class CamelCaseModel(BaseModel):
    class Config:
        alias_generator = camelcase
        allow_population_by_field_name = True


class HealthResponse(CamelCaseModel):
    status: bool


class BasicCountryInfoRequest(CamelCaseModel):
    code: str = Field(
        ...,
        title="Code",
        description="ISO 3166-1 alpha-2 code for the country",
        example="FI",
        min_length=2,
        max_length=2,
    )


class Capital(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name of the capital of the Country",
        example="Helsinki",
    )
    lat: float = Field(
        ...,
        title="Latitude",
        description="The latitude coordinate of the Capital",
        ge=-90.0,
        le=90.0,
        example=60.170833,
    )
    lon: float = Field(
        ...,
        title="Longitude",
        description="The longitude coordinate of the Capital",
        ge=-180.0,
        le=180.0,
        example=24.9375,
    )


class BasicCountryInfoResponse(CamelCaseModel):
    code: str = Field(
        ...,
        title="Code",
        description="ISO 3166-1 alpha-2 code for the country",
        example="FI",
        min_length=2,
        max_length=2,
    )
    name: str = Field(
        ...,
        title="Name",
        description="The name of the country",
        example="Finland",
    )
    area: float = Field(
        ...,
        title="Area",
        description="The area of the country in km^2",
        example=338455,
    )
    languages: List[constr(min_length=2, max_length=2)] = Field(
        ...,
        title="Official languages",
        description="ISO 639-1 language codes for the official languages",
        example=["fi", "sv"],
    )
    capital: Optional[Capital] = Field(
        None,
        title="Capital",
        description="The capital of the country, legislative if multiple",
    )
