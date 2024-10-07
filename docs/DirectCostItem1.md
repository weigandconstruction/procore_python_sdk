# DirectCostItem1

Direct Cost Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**employee_id** | **int** | Employee ID tied to the Direct Cost Item | [optional] 
**direct_cost_date** | **date** | Date | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**payment_date** | **date** | Payment Date | [optional] 
**received_date** | **date** | Received Date | [optional] 
**status** | **str** | Status | [optional] 
**terms** | **str** | The agreed upon Terms for the date of payment | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**line_items** | [**List[DirectCostLineItem2]**](DirectCostLineItem2.md) | Line items that should be assoicated with the direct cost item. | [optional] 

## Example

```python
from procore_sdk.models.direct_cost_item1 import DirectCostItem1

# TODO update the JSON string below
json = "{}"
# create an instance of DirectCostItem1 from a JSON string
direct_cost_item1_instance = DirectCostItem1.from_json(json)
# print the JSON string representation of the object
print(DirectCostItem1.to_json())

# convert the object into a dict
direct_cost_item1_dict = direct_cost_item1_instance.to_dict()
# create an instance of DirectCostItem1 from a dict
direct_cost_item1_from_dict = DirectCostItem1.from_dict(direct_cost_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


