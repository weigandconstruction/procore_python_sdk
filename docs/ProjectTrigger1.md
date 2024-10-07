# ProjectTrigger1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 
**api_version** | **str** | API Version | 
**triggers** | [**List[CompanyTriggerTrigger]**](CompanyTriggerTrigger.md) |  | 

## Example

```python
from procore_sdk.models.project_trigger1 import ProjectTrigger1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTrigger1 from a JSON string
project_trigger1_instance = ProjectTrigger1.from_json(json)
# print the JSON string representation of the object
print(ProjectTrigger1.to_json())

# convert the object into a dict
project_trigger1_dict = project_trigger1_instance.to_dict()
# create an instance of ProjectTrigger1 from a dict
project_trigger1_from_dict = ProjectTrigger1.from_dict(project_trigger1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


