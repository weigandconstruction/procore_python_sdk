# LineItemType2

Line Item Type object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Line Item Type name | [optional] 
**csv_import_code** | **str** | Abbreviation code | [optional] 
**base_type** | **str** | Base type | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.line_item_type2 import LineItemType2

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemType2 from a JSON string
line_item_type2_instance = LineItemType2.from_json(json)
# print the JSON string representation of the object
print(LineItemType2.to_json())

# convert the object into a dict
line_item_type2_dict = line_item_type2_instance.to_dict()
# create an instance of LineItemType2 from a dict
line_item_type2_from_dict = LineItemType2.from_dict(line_item_type2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


