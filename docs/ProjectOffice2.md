# ProjectOffice2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Office | [optional] 
**name** | **str** | The name for the Office | [optional] 

## Example

```python
from procore_sdk.models.project_office2 import ProjectOffice2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOffice2 from a JSON string
project_office2_instance = ProjectOffice2.from_json(json)
# print the JSON string representation of the object
print(ProjectOffice2.to_json())

# convert the object into a dict
project_office2_dict = project_office2_instance.to_dict()
# create an instance of ProjectOffice2 from a dict
project_office2_from_dict = ProjectOffice2.from_dict(project_office2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


