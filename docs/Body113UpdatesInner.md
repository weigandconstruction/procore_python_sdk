# Body113UpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Calendar Item to be updated | [optional] 
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
from procore_sdk.models.body113_updates_inner import Body113UpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body113UpdatesInner from a JSON string
body113_updates_inner_instance = Body113UpdatesInner.from_json(json)
# print the JSON string representation of the object
print(Body113UpdatesInner.to_json())

# convert the object into a dict
body113_updates_inner_dict = body113_updates_inner_instance.to_dict()
# create an instance of Body113UpdatesInner from a dict
body113_updates_inner_from_dict = Body113UpdatesInner.from_dict(body113_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


