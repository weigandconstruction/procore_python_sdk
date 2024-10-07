# RFIBodyRfiScheduleImpact

The Schedule Impact of the RFI

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The Status of the Schedule Impact | [optional] 
**value** | **int** | The Value in days of the Schedule Impact | [optional] 

## Example

```python
from procore_sdk.models.rfi_body_rfi_schedule_impact import RFIBodyRfiScheduleImpact

# TODO update the JSON string below
json = "{}"
# create an instance of RFIBodyRfiScheduleImpact from a JSON string
rfi_body_rfi_schedule_impact_instance = RFIBodyRfiScheduleImpact.from_json(json)
# print the JSON string representation of the object
print(RFIBodyRfiScheduleImpact.to_json())

# convert the object into a dict
rfi_body_rfi_schedule_impact_dict = rfi_body_rfi_schedule_impact_instance.to_dict()
# create an instance of RFIBodyRfiScheduleImpact from a dict
rfi_body_rfi_schedule_impact_from_dict = RFIBodyRfiScheduleImpact.from_dict(rfi_body_rfi_schedule_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


