# TimecardEntry3SubJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**code** | **str** | Unique code in the scope of a Project | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry3_sub_job import TimecardEntry3SubJob

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry3SubJob from a JSON string
timecard_entry3_sub_job_instance = TimecardEntry3SubJob.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry3SubJob.to_json())

# convert the object into a dict
timecard_entry3_sub_job_dict = timecard_entry3_sub_job_instance.to_dict()
# create an instance of TimecardEntry3SubJob from a dict
timecard_entry3_sub_job_from_dict = TimecardEntry3SubJob.from_dict(timecard_entry3_sub_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


