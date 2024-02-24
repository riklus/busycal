import os
import re

import httpx
from flask import request, abort, Response

from busycal import app

BUSYCAL_TOKEN = os.getenv("BUSYCAL_TOKEN")
RE_TRANSPARENT = re.compile(r"^\bTRANSP:TRANSPARENT\b", flags=re.MULTILINE)


@app.route("/")
async def ical():
    ical = request.args.get("ical")
    token = request.args.get("token")

    if BUSYCAL_TOKEN and token != BUSYCAL_TOKEN:
        abort(403)

    async with httpx.AsyncClient() as client:
        res = await client.get(ical)

    busy = RE_TRANSPARENT.sub(r"TRANSP:OPAQUE", res.text)

    return Response(busy, mimetype="text/plain")
