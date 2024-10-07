# RestV10TimecardEntriesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Timecard entry id | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Timecard entry date | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Timecard entry description | [optional] 
**hours** | **str** | Timecard entry hours | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**origin_id** | **int** | ID of related external data | [optional] 
**origin_data** | **str** | Value of related external data | [optional] 
**updated_at** | **datetime** | Timecard entry updated at | [optional] 
**automatically_split_timecard_entries** | [**List[TimecardEntry6]**](TimecardEntry6.md) | Timecard entries returned with associated object as part of overtime_management | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_timecard_entries_get200_response_inner import RestV10TimecardEntriesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TimecardEntriesGet200ResponseInner from a JSON string
rest_v10_timecard_entries_get200_response_inner_instance = RestV10TimecardEntriesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10TimecardEntriesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_timecard_entries_get200_response_inner_dict = rest_v10_timecard_entries_get200_response_inner_instance.to_dict()
# create an instance of RestV10TimecardEntriesGet200ResponseInner from a dict
rest_v10_timecard_entries_get200_response_inner_from_dict = RestV10TimecardEntriesGet200ResponseInner.from_dict(rest_v10_timecard_entries_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


