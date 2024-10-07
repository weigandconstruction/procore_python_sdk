# InspectionTypeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inspection_type** | [**InspectionType3**](InspectionType3.md) |  | 

## Example

```python
from procore_sdk.models.inspection_type_body import InspectionTypeBody

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionTypeBody from a JSON string
inspection_type_body_instance = InspectionTypeBody.from_json(json)
# print the JSON string representation of the object
print(InspectionTypeBody.to_json())

# convert the object into a dict
inspection_type_body_dict = inspection_type_body_instance.to_dict()
# create an instance of InspectionTypeBody from a dict
inspection_type_body_from_dict = InspectionTypeBody.from_dict(inspection_type_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


