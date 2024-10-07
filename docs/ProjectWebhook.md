# ProjectWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 
**hook** | [**CompanyWebhookHook**](CompanyWebhookHook.md) |  | 

## Example

```python
from procore_sdk.models.project_webhook import ProjectWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectWebhook from a JSON string
project_webhook_instance = ProjectWebhook.from_json(json)
# print the JSON string representation of the object
print(ProjectWebhook.to_json())

# convert the object into a dict
project_webhook_dict = project_webhook_instance.to_dict()
# create an instance of ProjectWebhook from a dict
project_webhook_from_dict = ProjectWebhook.from_dict(project_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


