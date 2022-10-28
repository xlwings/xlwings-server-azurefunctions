import json
import os

import azure.functions as func
import xlwings as xw


def main(req: func.HttpRequest) -> func.HttpResponse:

    if req.headers.get("Authorization") != os.environ["XLWINGS_API_KEY"]:
        return func.HttpResponse("Unauthorized", status_code=401, mimetype="text/html")

    req_body = req.get_json()
    book = xw.Book(json=req_body)

    sheet = book.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"

    return func.HttpResponse(
        json.dumps(book.json()),
        status_code=200,
        mimetype="application/json",
    )
