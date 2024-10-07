# OtherHoursProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the project | [optional] 
**name** | **str** | Name of the project | [optional] 

## Example

```python
from procore_sdk.models.other_hours_project import OtherHoursProject

# TODO update the JSON string below
json = "{}"
# create an instance of OtherHoursProject from a JSON string
other_hours_project_instance = OtherHoursProject.from_json(json)
# print the JSON string representation of the object
print(OtherHoursProject.to_json())

# convert the object into a dict
other_hours_project_dict = other_hours_project_instance.to_dict()
# create an instance of OtherHoursProject from a dict
other_hours_project_from_dict = OtherHoursProject.from_dict(other_hours_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


