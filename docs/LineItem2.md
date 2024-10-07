# LineItem2

Line Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount | [optional] 
**wbs_code_id** | **int** | WBS Code ID | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**description** | **str** | Description | [optional] 
**direct_cost_id** | **int** | Direct Cost ID | [optional] 
**extended_type** | **str** | Calculated amount from quantity and unit cost or manually entered amount | [optional] 
**quantity** | **float** | Quantity of described item | [optional] 
**line_item_type_id** | **int** | Line Item Type ID | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**unit_cost** | **float** | Unit cost of described item | [optional] 
**uom** | **str** | Unit of measure of the described item | [optional] 

## Example

```python
from procore_sdk.models.line_item2 import LineItem2

# TODO update the JSON string below
json = "{}"
# create an instance of LineItem2 from a JSON string
line_item2_instance = LineItem2.from_json(json)
# print the JSON string representation of the object
print(LineItem2.to_json())

# convert the object into a dict
line_item2_dict = line_item2_instance.to_dict()
# create an instance of LineItem2 from a dict
line_item2_from_dict = LineItem2.from_dict(line_item2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


