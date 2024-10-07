# DirectCostLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_amount** | **float** | Amount | [optional] 
**wbs_code_id** | **int** | WBS Code ID | 
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
from procore_sdk.models.direct_cost_line_item import DirectCostLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of DirectCostLineItem from a JSON string
direct_cost_line_item_instance = DirectCostLineItem.from_json(json)
# print the JSON string representation of the object
print(DirectCostLineItem.to_json())

# convert the object into a dict
direct_cost_line_item_dict = direct_cost_line_item_instance.to_dict()
# create an instance of DirectCostLineItem from a dict
direct_cost_line_item_from_dict = DirectCostLineItem.from_dict(direct_cost_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


