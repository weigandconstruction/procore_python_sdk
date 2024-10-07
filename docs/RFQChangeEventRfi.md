# RFQChangeEventRfi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Title | [optional] 
**number** | **int** | Number | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**status** | **str** | Status | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_event_rfi import RFQChangeEventRfi

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeEventRfi from a JSON string
rfq_change_event_rfi_instance = RFQChangeEventRfi.from_json(json)
# print the JSON string representation of the object
print(RFQChangeEventRfi.to_json())

# convert the object into a dict
rfq_change_event_rfi_dict = rfq_change_event_rfi_instance.to_dict()
# create an instance of RFQChangeEventRfi from a dict
rfq_change_event_rfi_from_dict = RFQChangeEventRfi.from_dict(rfq_change_event_rfi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


