# TimecardEntry2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Timecard entry id | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Timecard entry date | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Timecard entry description | [optional] 
**billable** | **bool** | Timecard entry billable status | [optional] 
**hours** | **str** | Timecard entry hours | [optional] 
**updated_at** | **datetime** | Timecard entry updated at | [optional] 
**timecard_type** | **str** | Timecard entry time type | [optional] 
**cost_code** | **str** | Timecard entry cost code | [optional] 
**origin_id** | **int** | ID of related external data | [optional] 
**origin_data** | **str** | Value of related external data | [optional] 
**timesheet_status** | [**Timesheet2**](Timesheet2.md) |  | [optional] 
**full_cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**party** | [**Party**](Party.md) |  | [optional] 
**timecard_time_type** | [**TimecardTimeType3**](TimecardTimeType3.md) |  | [optional] 
**line_item_type_id** | **int** | The ID of the Line Item Type of the Timecard Entry | [optional] 

## Example

```python
from procore_sdk.models.timecard_entry2 import TimecardEntry2

# TODO update the JSON string below
json = "{}"
# create an instance of TimecardEntry2 from a JSON string
timecard_entry2_instance = TimecardEntry2.from_json(json)
# print the JSON string representation of the object
print(TimecardEntry2.to_json())

# convert the object into a dict
timecard_entry2_dict = timecard_entry2_instance.to_dict()
# create an instance of TimecardEntry2 from a dict
timecard_entry2_from_dict = TimecardEntry2.from_dict(timecard_entry2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


