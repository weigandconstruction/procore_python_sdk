# Body112CalendarItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_id** | **int** | ID of the assigned user for the Calendar Item | [optional] 
**color** | **str** | Calendar Item color (as a hex triplet) | [optional] 
**description** | **str** | Calendar Item description | [optional] 
**finish** | **date** | The finish date of the Calendar Item | [optional] 
**name** | **str** | Calendar Item name | [optional] 
**percentage** | **int** | Calendar Item completion percentage | [optional] 
**private** | **bool** | Calendar Item private status | [optional] 
**start** | **date** | The start date of the Calendar Item | [optional] 

## Example

```python
from procore_sdk.models.body112_calendar_item import Body112CalendarItem

# TODO update the JSON string below
json = "{}"
# create an instance of Body112CalendarItem from a JSON string
body112_calendar_item_instance = Body112CalendarItem.from_json(json)
# print the JSON string representation of the object
print(Body112CalendarItem.to_json())

# convert the object into a dict
body112_calendar_item_dict = body112_calendar_item_instance.to_dict()
# create an instance of Body112CalendarItem from a dict
body112_calendar_item_from_dict = Body112CalendarItem.from_dict(body112_calendar_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


