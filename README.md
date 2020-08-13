---
page_type: sample
description: "This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux."
languages:
- python
products:
- azure
- azure-app-service
---

# Python Flask sample for Azure App Service (Linux)

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux.

For more information, please see the [Python on App Service quickstart](https://docs.microsoft.com/azure/app-service/containers/quickstart-python).

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Dependencies:

Install dependencies: `pip install -r requirements.txt`

## Running: 

To execute the app, run the following commands:
```
export FLASK_APP=application.py
flask run
```

## Tests:

- Run Test: `python -m pytest`

- Run Coverage: `python -m coverage xml test_flask.py` 
