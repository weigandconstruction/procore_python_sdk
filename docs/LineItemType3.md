# LineItemType3

Line Item Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line Item Type ID | [optional] 
**name** | **str** | Line Item Type name | [optional] 
**code** | **str** | Code | [optional] 
**base_type** | **str** | Base type | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.line_item_type3 import LineItemType3

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemType3 from a JSON string
line_item_type3_instance = LineItemType3.from_json(json)
# print the JSON string representation of the object
print(LineItemType3.to_json())

# convert the object into a dict
line_item_type3_dict = line_item_type3_instance.to_dict()
# create an instance of LineItemType3 from a dict
line_item_type3_from_dict = LineItemType3.from_dict(line_item_type3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


