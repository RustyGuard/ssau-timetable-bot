import json
import logging
import os

from api import SsauAPI

_institutes = None
api = SsauAPI()


async def get_facilities() -> dict[str, int]:

    global _institutes
    if _institutes is None:
        filename = 'data/facilities.json'

        if os.path.isfile(filename):
            with open(filename) as json_file:
                _institutes = json.load(json_file)
        else:
            _institutes = await api.get_institutes_and_faculties()
            with open(filename, 'w') as outfile:
                json.dump(_institutes, outfile)

    return _institutes


async def get_groups(institute: str, course: int) -> dict[str, int]:
    institutes = await get_facilities()

    filename = f'data/groups-{institutes[institute]}-{course}.json'
    if os.path.isfile(filename):
        with open(filename) as json_file:
            groups = json.load(json_file)
    else:
        groups = await api.get_groups(institutes[institute], course)
        with open(filename, 'w') as outfile:
            json.dump(_institutes, outfile)

    logging.info(groups)
    return groups