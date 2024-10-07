# Body146


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uid** | **str** | Third party application UID | 
**project_id** | **int** | Project ID. Note: Only one of project_id or company_id is required. | 
**company_id** | **int** | Company ID. Note: Only one of project_id or company_id is required. | 
**app_installation** | [**Body146AppInstallation**](Body146AppInstallation.md) |  | 

## Example

```python
from procore_sdk.models.body146 import Body146

# TODO update the JSON string below
json = "{}"
# create an instance of Body146 from a JSON string
body146_instance = Body146.from_json(json)
# print the JSON string representation of the object
print(Body146.to_json())

# convert the object into a dict
body146_dict = body146_instance.to_dict()
# create an instance of Body146 from a dict
body146_from_dict = Body146.from_dict(body146_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


