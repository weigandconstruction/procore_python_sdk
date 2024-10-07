# ProjectOffice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Office ID | [optional] 
**name** | **str** | Office name | [optional] 

## Example

```python
from procore_sdk.models.project_office import ProjectOffice

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOffice from a JSON string
project_office_instance = ProjectOffice.from_json(json)
# print the JSON string representation of the object
print(ProjectOffice.to_json())

# convert the object into a dict
project_office_dict = project_office_instance.to_dict()
# create an instance of ProjectOffice from a dict
project_office_from_dict = ProjectOffice.from_dict(project_office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


