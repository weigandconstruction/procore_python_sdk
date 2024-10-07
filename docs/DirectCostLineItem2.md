# DirectCostLineItem2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the line item (only required when updating) | [optional] 
**manual_amount** | **float** | Amount | [optional] 
**wbs_code_id** | **int** | WBS Code ID (required when creating new line items on the direct cost) | [optional] 
**description** | **str** | Description | [optional] 
**direct_cost_id** | **int** | Direct Cost ID | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**quantity** | **float** | Quantity of described item | [optional] 
**ref** | **str** | The reference, if any, passed in upon item creation and is not persisted. | [optional] 
**unit_cost** | **float** | Unit cost of described item | [optional] 
**uom** | **str** | Unit of measure of the described item | [optional] 

## Example

```python
from procore_sdk.models.direct_cost_line_item2 import DirectCostLineItem2

# TODO update the JSON string below
json = "{}"
# create an instance of DirectCostLineItem2 from a JSON string
direct_cost_line_item2_instance = DirectCostLineItem2.from_json(json)
# print the JSON string representation of the object
print(DirectCostLineItem2.to_json())

# convert the object into a dict
direct_cost_line_item2_dict = direct_cost_line_item2_instance.to_dict()
# create an instance of DirectCostLineItem2 from a dict
direct_cost_line_item2_from_dict = DirectCostLineItem2.from_dict(direct_cost_line_item2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


