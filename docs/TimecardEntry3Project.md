# TimecardEntry3Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the project. | [optional] 
**name** | **str** | Project Display Name (could include Project Number) | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry3_project import TimecardEntry3Project

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry3Project from a JSON string
timecard_entry3_project_instance = TimecardEntry3Project.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry3Project.to_json())

# convert the object into a dict
timecard_entry3_project_dict = timecard_entry3_project_instance.to_dict()
# create an instance of TimecardEntry3Project from a dict
timecard_entry3_project_from_dict = TimecardEntry3Project.from_dict(timecard_entry3_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


