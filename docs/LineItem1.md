# LineItem1

The Line Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the line item | [optional] 
**amount** | **str** | Amount | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**description** | **str** | Description | [optional] 
**extended_type** | **str** | Extended type | [optional] 
**quantity** | **str** | Quantity | [optional] 
**line_item_type_id** | **int** | Line Item Type ID | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**tax_code_id** | **int** | Tax Code ID | [optional] 
**unit_cost** | **str** | Unit cost | [optional] 
**uom** | **str** | Unit of measure | [optional] 
**wbs_code_id** | **int** | WBS code ID | [optional] 

## Example

```python
from procore_sdk.models.line_item1 import LineItem1

# TODO update the JSON string below
json = "{}"
# create an instance of LineItem1 from a JSON string
line_item1_instance = LineItem1.from_json(json)
# print the JSON string representation of the object
print(LineItem1.to_json())

# convert the object into a dict
line_item1_dict = line_item1_instance.to_dict()
# create an instance of LineItem1 from a dict
line_item1_from_dict = LineItem1.from_dict(line_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


