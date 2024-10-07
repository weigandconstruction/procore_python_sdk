# LineItemType

Line Item Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the Line Item Type | [optional] 
**name** | **str** | Name for the Line Item Type | [optional] 
**code** | **str** | Code for the Line Item Type | [optional] 
**base_type** | **str** | Base type | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.line_item_type import LineItemType

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemType from a JSON string
line_item_type_instance = LineItemType.from_json(json)
# print the JSON string representation of the object
print(LineItemType.to_json())

# convert the object into a dict
line_item_type_dict = line_item_type_instance.to_dict()
# create an instance of LineItemType from a dict
line_item_type_from_dict = LineItemType.from_dict(line_item_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


