# ProjectTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 
**api_version** | **str** | API Version | 
**trigger** | [**CompanyTriggerTrigger**](CompanyTriggerTrigger.md) |  | 

## Example

```python
from procore_sdk.models.project_trigger import ProjectTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTrigger from a JSON string
project_trigger_instance = ProjectTrigger.from_json(json)
# print the JSON string representation of the object
print(ProjectTrigger.to_json())

# convert the object into a dict
project_trigger_dict = project_trigger_instance.to_dict()
# create an instance of ProjectTrigger from a dict
project_trigger_from_dict = ProjectTrigger.from_dict(project_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


