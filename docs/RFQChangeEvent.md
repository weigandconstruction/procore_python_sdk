# RFQChangeEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**number** | **int** | Number with alpha characters stripped out | [optional] 
**alphanumeric_number** | **str** | Number including alpha characters | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**title** | **str** | Title | [optional] 
**description** | **str** | Description | [optional] 
**status** | **str** | Status | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**event_type** | **str** | Event type | [optional] 
**event_scope** | **str** | Event scope | [optional] 
**change_event_origin_id** | **int** | Origin ID | [optional] 
**change_event_origin_type** | **str** | Origin type | [optional] 
**rfi** | [**RFQChangeEventRfi**](RFQChangeEventRfi.md) |  | [optional] 
**change_event_line_items** | [**List[RFQChangeEventChangeEventLineItemsInner]**](RFQChangeEventChangeEventLineItemsInner.md) |  | [optional] 
**change_order_change_reason** | [**RFQChangeEventChangeOrderChangeReason**](RFQChangeEventChangeOrderChangeReason.md) |  | [optional] 
**change_event_status** | [**RFQChangeEventChangeEventStatus**](RFQChangeEventChangeEventStatus.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RFQQuoteAttachmentsInner]**](RFQQuoteAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_event import RFQChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeEvent from a JSON string
rfq_change_event_instance = RFQChangeEvent.from_json(json)
# print the JSON string representation of the object
print(RFQChangeEvent.to_json())

# convert the object into a dict
rfq_change_event_dict = rfq_change_event_instance.to_dict()
# create an instance of RFQChangeEvent from a dict
rfq_change_event_from_dict = RFQChangeEvent.from_dict(rfq_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


