# DirectCostItem2

Direct Cost Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**direct_cost_date** | **date** | Date | [optional] 
**employee_id** | **int** | ID of the Employee tied to the Direct Cost Item | [optional] 
**invoice_number** | **str** | Unique identifier for a Direct Cost Item of type invoice. Is required only if &#x60;direct_cost_type&#x60; is set to &#x60;invoice&#x60;. | 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**payment_date** | **date** | Payment Date | [optional] 
**received_date** | **date** | Received Date | [optional] 
**status** | **str** | Status | [optional] 
**terms** | **str** | The agreed upon Terms for the date of payment | [optional] 
**vendor_id** | **int** | Vendor ID | 
**direct_cost_type** | **str** | Type | 

## Example

```python
from procore_sdk.models.direct_cost_item2 import DirectCostItem2

# TODO update the JSON string below
json = "{}"
# create an instance of DirectCostItem2 from a JSON string
direct_cost_item2_instance = DirectCostItem2.from_json(json)
# print the JSON string representation of the object
print(DirectCostItem2.to_json())

# convert the object into a dict
direct_cost_item2_dict = direct_cost_item2_instance.to_dict()
# create an instance of DirectCostItem2 from a dict
direct_cost_item2_from_dict = DirectCostItem2.from_dict(direct_cost_item2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


