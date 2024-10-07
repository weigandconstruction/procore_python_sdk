# TimecardEntry6


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

## Example

```python
from procore_sdk.models.timecard_entry6 import TimecardEntry6

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry6 from a JSON string
timecard_entry6_instance = TimecardEntry6.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry6.to_json())

# convert the object into a dict
timecard_entry6_dict = timecard_entry6_instance.to_dict()
# create an instance of TimecardEntry6 from a dict
timecard_entry6_from_dict = TimecardEntry6.from_dict(timecard_entry6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


