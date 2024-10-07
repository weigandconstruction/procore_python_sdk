# RestV10TimecardEntriesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Timecard Entry belongs to | 
**timecard_entry** | [**TimecardEntry7**](TimecardEntry7.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_timecard_entries_post_request import RestV10TimecardEntriesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TimecardEntriesPostRequest from a JSON string
rest_v10_timecard_entries_post_request_instance = RestV10TimecardEntriesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10TimecardEntriesPostRequest.to_json())

# convert the object into a dict
rest_v10_timecard_entries_post_request_dict = rest_v10_timecard_entries_post_request_instance.to_dict()
# create an instance of RestV10TimecardEntriesPostRequest from a dict
rest_v10_timecard_entries_post_request_from_dict = RestV10TimecardEntriesPostRequest.from_dict(rest_v10_timecard_entries_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


