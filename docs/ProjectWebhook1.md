# ProjectWebhook1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 
**hook** | [**CompanyWebhook1Hook**](CompanyWebhook1Hook.md) |  | 

## Example

```python
from procore_sdk.models.project_webhook1 import ProjectWebhook1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectWebhook1 from a JSON string
project_webhook1_instance = ProjectWebhook1.from_json(json)
# print the JSON string representation of the object
print(ProjectWebhook1.to_json())

# convert the object into a dict
project_webhook1_dict = project_webhook1_instance.to_dict()
# create an instance of ProjectWebhook1 from a dict
project_webhook1_from_dict = ProjectWebhook1.from_dict(project_webhook1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


