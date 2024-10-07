# RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response


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
**timesheet_status** | **str** | Deprecated. Reference status property. | [optional] 
**full_cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**timecard_time_type** | [**TimecardTimeType**](TimecardTimeType.md) |  | [optional] 
**line_item_type_id** | **int** | The ID of the Line Item Type of the Timecard Entry | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**automatically_split_timecard_entries** | [**List[TimecardEntry]**](TimecardEntry.md) | Timecard entries returned with associated object as part of overtime_management | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_project_timecard_entries_post200_response import RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response from a JSON string
rest_v11_projects_project_id_project_timecard_entries_post200_response_instance = RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_project_timecard_entries_post200_response_dict = rest_v11_projects_project_id_project_timecard_entries_post200_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response from a dict
rest_v11_projects_project_id_project_timecard_entries_post200_response_from_dict = RestV11ProjectsProjectIdProjectTimecardEntriesPost200Response.from_dict(rest_v11_projects_project_id_project_timecard_entries_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


