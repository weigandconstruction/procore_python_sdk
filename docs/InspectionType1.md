# InspectionType1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.inspection_type1 import InspectionType1

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionType1 from a JSON string
inspection_type1_instance = InspectionType1.from_json(json)
# print the JSON string representation of the object
print(InspectionType1.to_json())

# convert the object into a dict
inspection_type1_dict = inspection_type1_instance.to_dict()
# create an instance of InspectionType1 from a dict
inspection_type1_from_dict = InspectionType1.from_dict(inspection_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


