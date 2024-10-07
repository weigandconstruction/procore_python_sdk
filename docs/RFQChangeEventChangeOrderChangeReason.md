# RFQChangeEventChangeOrderChangeReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**company_id** | **int** | Company ID | [optional] 
**change_reason** | **str** | Reason for change | [optional] 
**show_in_select** | **bool** | Show in select | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_event_change_order_change_reason import RFQChangeEventChangeOrderChangeReason

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeEventChangeOrderChangeReason from a JSON string
rfq_change_event_change_order_change_reason_instance = RFQChangeEventChangeOrderChangeReason.from_json(json)
# print the JSON string representation of the object
print(RFQChangeEventChangeOrderChangeReason.to_json())

# convert the object into a dict
rfq_change_event_change_order_change_reason_dict = rfq_change_event_change_order_change_reason_instance.to_dict()
# create an instance of RFQChangeEventChangeOrderChangeReason from a dict
rfq_change_event_change_order_change_reason_from_dict = RFQChangeEventChangeOrderChangeReason.from_dict(rfq_change_event_change_order_change_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


