import fastapi

router = fastapi.APIRouter()


@router.get("/sections/{id}")
async def read_section():
    return {}


@router.get("/sections/{id}")
async def read_section_content_blocks():
    return {}


@router.get("/content-blocks/{id}")
async def read_content_block():
    return {}
