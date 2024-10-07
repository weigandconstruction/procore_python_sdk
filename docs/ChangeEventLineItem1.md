# ChangeEventLineItem1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**wbs_code_id** | [**ChangeEventLineItem1WbsCodeId**](ChangeEventLineItem1WbsCodeId.md) |  | [optional] 
**description** | **str** | Description | [optional] 
**uom** | **str** | Unit of Measure | [optional] 
**estimated_cost_amount** | **float** | Estimated Cost Amount | [optional] 
**estimated_cost_quantity** | **float** | Estimated Cost Quantity | [optional] 
**estimated_cost_unit_cost** | **float** | Estimated Cost Unit Cost | [optional] 
**estimated_cost_calculation_strategy** | **str** | Estimated Cost Calculation Strategy. Controls whether estimated_cost_amount is calculated from the quantity and unit_cost attributes or set manually to a provided value. | [optional] 
**line_item_type_id** | **int** | Line Item Type ID | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**proposed_vendor_id** | **int** | Proposed Vendor ID | [optional] 
**proposed_contract_id** | **int** | Proposed Contract ID | [optional] 
**commitment_contract_line_item_id** | **int** | Commitment Contract Line Item ID | [optional] 

## Example

```python
from procore_sdk.models.change_event_line_item1 import ChangeEventLineItem1

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEventLineItem1 from a JSON string
change_event_line_item1_instance = ChangeEventLineItem1.from_json(json)
# print the JSON string representation of the object
print(ChangeEventLineItem1.to_json())

# convert the object into a dict
change_event_line_item1_dict = change_event_line_item1_instance.to_dict()
# create an instance of ChangeEventLineItem1 from a dict
change_event_line_item1_from_dict = ChangeEventLineItem1.from_dict(change_event_line_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


