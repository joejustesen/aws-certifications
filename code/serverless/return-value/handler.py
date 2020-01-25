import json
import traceback
import os


def is_production():
    return "ATLAS_STAGE" in os.environ and os.environ["ATLAS_STAGE"] == "production"


def format_error(ex):
    if is_production():
        return {
            "errorMessage": str(ex),
        }
    else:
        return {
            "errorMessage": str(ex),
            "errorType": ex.__class__.__qualname__,
            "stackTrace": traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__),
        }


def http_empty(event, context):
    return {"statusCode": 200, "body": json.dumps({"value": 100})}


def http_error(event, context):
    try:
        raise ValueError("this is an error message")
    except Exception as ex:
        return {"statusCode": 400, "body": json.dumps(format_error(ex))}


if __name__ == "__main__":
    rtn = http_error({}, None)
    print(rtn)
