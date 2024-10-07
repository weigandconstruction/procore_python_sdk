# DirectCostItem3

Direct Cost Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**description** | **str** | Description | [optional] 
**direct_cost_date** | **date** | Date | [optional] 
**employee_id** | **int** | Employee ID | [optional] 
**invoice_number** | **str** | Unique identifier for a Direct Cost Item of type invoice | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**payment_date** | **date** | Payment Date | [optional] 
**received_date** | **date** | Received Date | [optional] 
**status** | **str** | Status | [optional] 
**terms** | **str** | The agreed upon Terms for the date of payment | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**direct_cost_type** | **str** | Type. Note: Can only be set when creating a direct cost item. | [optional] 

## Example

```python
from procore_sdk.models.direct_cost_item3 import DirectCostItem3

# TODO update the JSON string below
json = "{}"
# create an instance of DirectCostItem3 from a JSON string
direct_cost_item3_instance = DirectCostItem3.from_json(json)
# print the JSON string representation of the object
print(DirectCostItem3.to_json())

# convert the object into a dict
direct_cost_item3_dict = direct_cost_item3_instance.to_dict()
# create an instance of DirectCostItem3 from a dict
direct_cost_item3_from_dict = DirectCostItem3.from_dict(direct_cost_item3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


