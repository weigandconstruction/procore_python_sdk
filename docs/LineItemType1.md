# LineItemType1

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
from procore_sdk.models.line_item_type1 import LineItemType1

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemType1 from a JSON string
line_item_type1_instance = LineItemType1.from_json(json)
# print the JSON string representation of the object
print(LineItemType1.to_json())

# convert the object into a dict
line_item_type1_dict = line_item_type1_instance.to_dict()
# create an instance of LineItemType1 from a dict
line_item_type1_from_dict = LineItemType1.from_dict(line_item_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


