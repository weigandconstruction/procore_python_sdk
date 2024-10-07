# GenericToolItem1ScheduleImpact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Schedule impact status | [optional] 
**value** | **float** | Schedule impact value | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item1_schedule_impact import GenericToolItem1ScheduleImpact

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItem1ScheduleImpact from a JSON string
generic_tool_item1_schedule_impact_instance = GenericToolItem1ScheduleImpact.from_json(json)
# print the JSON string representation of the object
print(GenericToolItem1ScheduleImpact.to_json())

# convert the object into a dict
generic_tool_item1_schedule_impact_dict = generic_tool_item1_schedule_impact_instance.to_dict()
# create an instance of GenericToolItem1ScheduleImpact from a dict
generic_tool_item1_schedule_impact_from_dict = GenericToolItem1ScheduleImpact.from_dict(generic_tool_item1_schedule_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


