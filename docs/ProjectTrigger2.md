# ProjectTrigger2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID. You must supply either a company_id or project_id. | 
**triggers** | **List[int]** |  | 

## Example

```python
from procore_sdk.models.project_trigger2 import ProjectTrigger2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTrigger2 from a JSON string
project_trigger2_instance = ProjectTrigger2.from_json(json)
# print the JSON string representation of the object
print(ProjectTrigger2.to_json())

# convert the object into a dict
project_trigger2_dict = project_trigger2_instance.to_dict()
# create an instance of ProjectTrigger2 from a dict
project_trigger2_from_dict = ProjectTrigger2.from_dict(project_trigger2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


