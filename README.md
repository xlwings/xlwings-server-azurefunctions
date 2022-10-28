# xlwings Server with Azure Functions

## Prerequisites

Follow this tutorial:  
https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python

This repo has chosen the project name `hello`.

## Local Development

* Add xlwings to `requirements.txt`
* Run `xlwings license update -k my-license-key`, replacing `my-license-key` with your xlwings PRO (trial) license key
* `local.settings.json`: add `"XLWINGS_API_KEY": "DEVELOPMENT"` under `"Values"`
* Open` __init__.py` and hit `F5` to run it: this will print a URL on localhost that you can use from Excel/Google Sheets

## Deployment

After deploying the app following the official tutorial, you must set the following environment variables in the Azure web console:

* Select your app under the `Function App` Azure Service. Then go to `Configuration` > `Application settings` > `+ New application setting`.

    * Add `XLWINGS_LICENSE_KEY` (Name) `your-license-key` (value). Confirm with `OK`.
    * Add `XLWINGS_API_KEY` (Name) `a-random-key` (value). Confirm with `OK`.
  
  Then hit `Save` and `Continue`. This will restart your function app.
