# TimecardEntry8Crew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**company_id** | **int** |  | [optional] 
**employees** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**lead** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Created at | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry8_crew import TimecardEntry8Crew

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry8Crew from a JSON string
timecard_entry8_crew_instance = TimecardEntry8Crew.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry8Crew.to_json())

# convert the object into a dict
timecard_entry8_crew_dict = timecard_entry8_crew_instance.to_dict()
# create an instance of TimecardEntry8Crew from a dict
timecard_entry8_crew_from_dict = TimecardEntry8Crew.from_dict(timecard_entry8_crew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


