# TotalInspections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_in_schedule** | **int** | Total inspections number calculated. | [optional] 

## Example

```python
from procore_sdk.models.total_inspections import TotalInspections

# TODO update the JSON string below
json = "{}"
# create an instance of TotalInspections from a JSON string
total_inspections_instance = TotalInspections.from_json(json)
# print the JSON string representation of the object
print(TotalInspections.to_json())

# convert the object into a dict
total_inspections_dict = total_inspections_instance.to_dict()
# create an instance of TotalInspections from a dict
total_inspections_from_dict = TotalInspections.from_dict(total_inspections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


