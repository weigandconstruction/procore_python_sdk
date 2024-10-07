# RFQChangeEventChangeEventStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**mapped_to_status** | **str** | Internal status to which the Change Event Status maps | [optional] 
**show_in_select** | **bool** | Whether Change Event is available for GUI selection | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_event_change_event_status import RFQChangeEventChangeEventStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeEventChangeEventStatus from a JSON string
rfq_change_event_change_event_status_instance = RFQChangeEventChangeEventStatus.from_json(json)
# print the JSON string representation of the object
print(RFQChangeEventChangeEventStatus.to_json())

# convert the object into a dict
rfq_change_event_change_event_status_dict = rfq_change_event_change_event_status_instance.to_dict()
# create an instance of RFQChangeEventChangeEventStatus from a dict
rfq_change_event_change_event_status_from_dict = RFQChangeEventChangeEventStatus.from_dict(rfq_change_event_change_event_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


