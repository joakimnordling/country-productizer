from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.datasource import get_data
from app.models import BasicCountryInfoRequest, BasicCountryInfoResponse

router = APIRouter()


@router.post(
    "/test/ioxio-dataspace-guides/Country/BasicInfo",
    summary="Basic Country Info",
    description="Data Product for basic country info",
    response_model=BasicCountryInfoResponse,
)
async def data_product(params: BasicCountryInfoRequest):
    try:
        data = await get_data(params.code)
    except KeyError:
        raise HTTPException(404, "Country not found")

    return BasicCountryInfoResponse(**data)
