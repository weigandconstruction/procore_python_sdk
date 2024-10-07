# ScheduleDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**substantial_completion_date** | **date** | Substantial completion date | [optional] 
**finish_variance** | **str** | Finish variance | [optional] 
**percentage_complete** | **int** | Percentage complete | [optional] 

## Example

```python
from procore_sdk.models.schedule_dates import ScheduleDates

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDates from a JSON string
schedule_dates_instance = ScheduleDates.from_json(json)
# print the JSON string representation of the object
print(ScheduleDates.to_json())

# convert the object into a dict
schedule_dates_dict = schedule_dates_instance.to_dict()
# create an instance of ScheduleDates from a dict
schedule_dates_from_dict = ScheduleDates.from_dict(schedule_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


