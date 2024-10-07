# InspectionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.inspection_type import InspectionType

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionType from a JSON string
inspection_type_instance = InspectionType.from_json(json)
# print the JSON string representation of the object
print(InspectionType.to_json())

# convert the object into a dict
inspection_type_dict = inspection_type_instance.to_dict()
# create an instance of InspectionType from a dict
inspection_type_from_dict = InspectionType.from_dict(inspection_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


