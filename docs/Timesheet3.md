# Timesheet3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**var_date** | **date** | Timesheet date | [optional] 
**number** | **int** | Timesheet number | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**name** | **str** | Timesheet name | [optional] 
**status** | **str** | The approval status of the Timesheet | [optional] 

## Example

```python
from procore_sdk.models.timesheet3 import Timesheet3

# TODO update the JSON string below
json = "{}"
# create an instance of Timesheet3 from a JSON string
timesheet3_instance = Timesheet3.from_json(json)
# print the JSON string representation of the object
print(Timesheet3.to_json())

# convert the object into a dict
timesheet3_dict = timesheet3_instance.to_dict()
# create an instance of Timesheet3 from a dict
timesheet3_from_dict = Timesheet3.from_dict(timesheet3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


