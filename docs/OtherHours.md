# OtherHours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hours** | **int** | Number of hours worked that week on the project | [optional] 
**project** | [**OtherHoursProject**](OtherHoursProject.md) |  | [optional] 

## Example

```python
from procore_sdk.models.other_hours import OtherHours

# TODO update the JSON string below
json = "{}"
# create an instance of OtherHours from a JSON string
other_hours_instance = OtherHours.from_json(json)
# print the JSON string representation of the object
print(OtherHours.to_json())

# convert the object into a dict
other_hours_dict = other_hours_instance.to_dict()
# create an instance of OtherHours from a dict
other_hours_from_dict = OtherHours.from_dict(other_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


